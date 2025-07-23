import json
import os
import re
import google.generativeai as genai
from dotenv import load_dotenv
from pinecone import Pinecone
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from openai import OpenAI

load_dotenv()

class AIAssistant:
    def __init__(self, operators_path):
        print("--- Initializing AIAssistant ---")
        # API Keys and Configuration
        self.pinecone_api_key = os.getenv("PINECONE_API_KEY")
        self.pinecone_index_name = os.getenv("PINECONE_INDEX_NAME")
        self.google_api_key = os.getenv("GOOGLE_API_KEY")
        self.openai_api_key = os.getenv("OPENAI_API_KEY")

        if not all([self.pinecone_api_key, self.pinecone_index_name, self.google_api_key, self.openai_api_key]):
            raise ValueError("Please set PINECONE_API_KEY, PINECONE_INDEX_NAME, GOOGLE_API_KEY, and OPENAI_API_KEY in your .env file")

        # Initialize Pinecone
        try:
            print("--- Initializing Pinecone ---")
            self.pc = Pinecone(api_key=self.pinecone_api_key)
            self.index = self.pc.Index(self.pinecone_index_name)
            print("--- Pinecone initialized successfully ---")
        except Exception as e:
            print(f"--- Error initializing Pinecone: {e} ---")
            raise

        # Initialize Embedding Model (used for Pinecone RAG)
        try:
            print("--- Initializing Embedding Model ---")
            self.embeddings_model = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=self.google_api_key)
            print("--- Embedding Model initialized successfully ---")
        except Exception as e:
            print(f"--- Error initializing Embedding Model: {e} ---")
            raise

        # Initialize Generative Models
        try:
            print("--- Initializing Generative Models ---")
            genai.configure(api_key=self.google_api_key)
            self.gemini_model = genai.GenerativeModel('models/gemini-1.5-pro-latest')
            self.openai_client = OpenAI(api_key=self.openai_api_key)
            self.gpt_model_name = "gpt-4o"
            print("--- Generative Models initialized successfully ---")
        except Exception as e:
            print(f"--- Error initializing Generative Models: {e} ---")
            raise

        # Load all operator names (for the AI's general knowledge, not for RAG context)
        try:
            print(f"--- Loading operators from {operators_path} ---")
            self.operators = self.load_operators_from_md_files(operators_path)
            print(f"--- Loaded {len(self.operators)} operators ---")
        except Exception as e:
            print(f"--- Error loading operators: {e} ---")
            raise
        
        print("--- AIAssistant initialization complete ---")

    def load_operators_from_md_files(self, operators_path):
        operators = []
        for filename in os.listdir(operators_path):
            if filename.endswith(".md"):
                filepath = os.path.join(operators_path, filename)
                with open(filepath, 'r') as f:
                    content = f.read()
                    operator_name = re.search(r"# Operator: (.*)", content)
                    if operator_name:
                        operators.append(operator_name.group(1).strip())
        
        return operators

    def generate_logic(self, prompt, history=None, model_choice="gemini"):
        # 1. Embed the user's prompt
        query_vector = self.embeddings_model.embed_query(prompt)

        # 2. Query Pinecone for relevant operator documentation (RAG)
        results = self.index.query(vector=query_vector, top_k=5, include_metadata=True)
        retrieved_docs = [match.metadata['text'] for match in results.matches]
        
        context_parts = ["""

Relevant Operator Documentation:
"""]
        context_parts.extend([f"""---
{doc}""" for doc in retrieved_docs])
        context_operators = "".join(context_parts)

        system_prompt = f"""AI Agent Instructions – Assistant for Business Rule Operators
 Purpose
The AI agent serves to help users:

Write correct business rules using operators and operands.

Explain rule syntax, operator priorities, and logic.

Suggest optimizations and best practices.

Detect common mistakes (e.g., unnecessary parentheses, duplicate logic).

Provide relevant examples.

Assist with editor features and shortcuts.

⚙️ Behavior and Capabilities
1. Rule Writing Assistance
Generate *complete and executable* Timeqode logic. Always use the correct syntax for:

Binary operators: +, -, *, /, =, <, >=, etc. (e.g., `operand1 + operand2`)

Function operators: Len(), Date(), Year(), If(), Array(), etc. (e.g., `Len("some_string")`, `Array(1, 2, 3)` or `[1, 2, 3]`)

Explain expressions or sub-expressions when asked.

2. Operand Type Recognition
The agent should identify and highlight the type of each operand:

Constant: (12, "abc", True)

Parameter: (ClientAge, {{Date}})

Local Parameter: (@count)

Temporary Parameter: (#amount)

3. Priority Awareness
Apply operator priority rules (0–7) to guide evaluation order.

Recommend parentheses only when needed to clarify logic.

4. Rule Optimization
Suggest simplifications (e.g., If(Age > 18, True, False) → Age > 18)

Identify duplicated sub-expressions and recommend storing them in temporary parameters.

5. Comments and Documentation
Help generate comments (single-line //, block /* */)

Suggest where comments may improve clarity in complex expressions.

6. Editor Shortcut Support
The agent should promote usage of helpful editor shortcuts:

ActionShortcut
AutocompleteCtrl + Space
SaveCtrl + S
Comment/UncommentCtrl-K / Ctrl-Shift-K
ParseCtrl-Alt-P
Parse & FormatCtrl-Alt-K
Delete LineCtrl + D
Auto-indent (reverse)Shift + Tab

 Example Rules with Explanations
These examples demonstrate the expected *complete and executable* Timeqode logic. Learn from and apply these patterns.

Example 1 – Simple Validation
plaintext
Copy
Edit
ClientAge > 18
Checks if the client's age is greater than 18.

Example 2 – Using a Temporary Parameter
plaintext
Copy
Edit
#totalIncome := FixIncome + VariableIncome + AdditionalIncome
#totalIncome > 1000
Calculates total income and then checks if it exceeds 1000.

Example 3 – Function Operator
plaintext
Copy
Edit
Len("Test") > 2
Compares the length of the string "Test" with 2.

Example 4 – Operator Precedence
plaintext
Copy
Edit
1 + 2 * 3   // evaluates to 7
(1 + 2) * 3 // evaluates to 9
The agent should explain that multiplication has higher precedence than addition unless overridden with parentheses.

Example 5 – Reading from Database
plaintext
Copy
Edit
ReadEntity(Product, id = 2)
Reads a single product entity from the database where the ID is 2.

Example 6 – Adding two numbers
plaintext
Copy
Edit
5 + 3
Adds the numbers 5 and 3.

Example 7 – First letter of days of the week
plaintext
Copy
Edit
IterateAndOutput(["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],SubStr(CurrentValue, 0, 1))
Iterates through the days of the week and returns the first letter for each.

⚠️ Validation & Enforcement Rules
Alert when parameters have the same name as operators and aren't enclosed in {{}} (e.g., {{Date}} vs Date()).

Warn against redundant parentheses: ((a + b)) → a + b.

Prevent overcomplicated boolean expressions:
If(condition, True, False) should become just condition.

✅ Best Practices Promoted by the Agent
Use comments to explain complex parts of rules.

Avoid duplicated expressions—store them in temporary parameters when reused.

Group logical expressions efficiently:
(A And B) Or (B And C) → B And (A Or C)

Never use semicolons (`;`) in the generated logic.

 Smart Prompts and Guidance
The agent can proactively ask:

“Would you like to extract this subexpression into a temporary parameter?”

“Can I suggest a simplified version of this rule?”

“This logic seems overly complex. Want a clearer version?”

“The Like operator has lower precedence than +. Want to add parentheses for clarity?”

You have access to the following operators: {self.operators}
Your output should ONLY be the generated formula string, and nothing else. Do NOT include any explanations, JSON formatting, or conversational text. Only use operators from the provided list and combine them to form *complete and executable* logic. Only use quotes for string literals, not for entity names, parameters, or numbers.

{context_operators}
        """

        # Prepare chat history for the model
        chat_history_for_model = []
        if history:
            for msg in history:
                # Assuming msg is a dictionary with 'role' and 'parts' (or 'content')
                # Adjust keys based on how you structure your history messages
                if 'role' in msg and ('parts' in msg or 'content' in msg):
                     chat_history_for_model.append(msg)
                elif 'prompt' in msg and 'response' in msg: # Handle your ChatMessage object structure
                     chat_history_for_model.append({'role': 'user', 'parts': [msg['prompt']]})
                     chat_history_for_model.append({'role': 'model', 'parts': [msg['response']]})


        # Generate content using the model
        if model_choice == "gemini":
            response = self.gemini_model.generate_content(
                contents=[*chat_history_for_model, {'role': 'user', 'parts': [system_prompt, "\n\nUser Prompt: ", prompt]}]
            )
            return {"logic": response.text.strip(), "model_used": "Gemini"}
        elif model_choice == "gpt-4o":
            messages = []
            messages.append({"role": "system", "content": system_prompt})
            for msg in chat_history_for_model:
                # Assuming msg is a dictionary with 'role' and 'content' for OpenAI
                # Adjust keys based on how you structure your history messages
                if 'role' in msg and 'content' in msg:
                     messages.append(msg)
                elif 'prompt' in msg and 'response' in msg: # Handle your ChatMessage object structure
                     messages.append({"role": "user", "content": msg['prompt']})
                     messages.append({"role": "assistant", "content": msg['response']})


            chat_completion = self.openai_client.chat.completions.create(
                model=self.gpt_model_name,
                messages=messages
            )
            return {"logic": chat_completion.choices[0].message.content.strip(), "model_used": "GPT-4o"}
        else:
            raise ValueError("Invalid model choice.")