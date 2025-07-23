---
input_types:
- Any
- Any
- Boolean
output_type: Number
purpose:
- Collection Manipulation
- String Manipulation
- Data Access
---
# Operator: IndexOf
---
### **Description**
Finds the index of an element or string (second operand) inside a collection or string (first operand)
returns -1 if element was not found
---
### **Syntax**
```
: IndexOf(<collection / string where to search>, <element / string to search for>, [<search backwards>])
ex1. IndexOf([1, 3, 5], 3) returns 1
ex2. IndexOf("individual","i", true) returns 5
```
---
### **Examples**
No examples provided.
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 2
- **Max Operands:** 3
- **Idempotent:** true