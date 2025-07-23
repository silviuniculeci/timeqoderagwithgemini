---
input_types:
- String
- String
output_type: Boolean
purpose:
- String Manipulation
- Logical
---
# Operator: Match_RegEx
---
### **Description**
Checks if a string (first operand) matches a specific pattern (second operand)
---
### **Syntax**
Not specified.
---
### **Examples**
```
. Match_RegEx("Test2","[A-Za-z0-9]+")
```
**Result:** `true`
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 2
- **Max Operands:** 2
- **Idempotent:** true