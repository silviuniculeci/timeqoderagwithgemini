---
input_types:
- String
- String
output_type: Boolean
purpose:
- Logical
- String Manipulation
---
# Operator: Like
---
### **Description**
Matches a string to a pattern
---
### **Syntax**
```
: <string> Like <pattern>
```
---
### **Examples**
```
. "abdc" Like "%bdc" return true
```
---
### **Technical Details**
- **Type:** Infix Operator
- **Min Operands:** 2
- **Max Operands:** 2
- **Idempotent:** true