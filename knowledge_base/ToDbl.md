---
input_types:
- Any
- String
output_type: Number
purpose:
- Data Transformation
- Utility
---
# Operator: ToDbl
---
### **Description**
Converts the operand to double
---
### **Syntax**
```
: ToDbl(<value to convert>, [<culture name - if nothing is provided it uses the current culture>])
ex1. ToDbl("15.3")
ex2. ToDbl("3.1415", "en-US")
```
---
### **Examples**
No examples provided.
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 1
- **Max Operands:** 2
- **Idempotent:** true