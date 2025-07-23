---
input_types:
- Any
- String
- String
output_type: String
purpose:
- Data Transformation
- Utility
---
# Operator: ToStr
---
### **Description**
Converts an expression to string
---
### **Syntax**
```
: ToStr(<operand>, [<format / separator>], [<culture code (default is platform setting)>])
ex1. ToStr(15) returns "15"
ex2. ToStr([1,2,3], "-") returns "1-2-3"
ex3. ToStr(Date, "dd.MM.yyyy")
ex4. ToStr(Date, "dddd", "ro-RO") returns the name of the current day in Romanian language
```
---
### **Examples**
No examples provided.
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 1
- **Max Operands:** 3
- **Idempotent:** true