import json
import os
import re
import google.generativeai as genai
from dotenv import load_dotenv
from pinecone import Pinecone
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

class AIAssistant:
    def __init__(self, operators_path):
        # Pinecone Configuration
        self.pinecone_api_key = os.getenv("PINECONE_API_KEY")
        self.pinecone_index_name = os.getenv("PINECONE_INDEX_NAME")
        self.google_api_key = os.getenv("GOOGLE_API_KEY")

        if not self.pinecone_api_key or not self.pinecone_index_name or not self.google_api_key:
            raise ValueError("Please set PINECONE_API_KEY, PINECONE_INDEX_NAME, and GOOGLE_API_KEY in your .env file")

        # Initialize Pinecone
        self.pc = Pinecone(api_key=self.pinecone_api_key)
        self.index = self.pc.Index(self.pinecone_index_name)

        # Initialize Embedding Model
        self.embeddings_model = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=self.google_api_key)

        # Initialize Generative Model
        genai.configure(api_key=self.google_api_key)
        self.model = genai.GenerativeModel('models/gemini-1.5-pro-latest')

        # Load all operator names (for the AI's general knowledge, not for RAG context)
        self.operators = self.load_operators_from_md_files(operators_path)

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

    def generate_logic(self, prompt, history=None):
        # 1. Embed the user's prompt
        query_vector = self.embeddings_model.embed_query(prompt)

        # 2. Query Pinecone for relevant operator documentation (RAG)
        results = self.index.query(vector=query_vector, top_k=5, include_metadata=True)
        retrieved_docs = [match.metadata['text'] for match in results.matches]
        context_operators = "\n\nRelevant Operator Documentation:\n" + "\n---\n".join(retrieved_docs)

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
                chat_history_for_model.append(msg)

        # Generate content using the model
        response = self.model.generate_content(
            contents=[*chat_history_for_model, {'role': 'user', 'parts': [f"{system_prompt}\n\nUser Prompt: {prompt}"]}]
        )

        return {"logic": response.text.strip()}