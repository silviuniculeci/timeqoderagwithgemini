---
input_types:
- String
output_type: Boolean
purpose:
- String Manipulation
- Logical
---
# Operator: EndsWith
---
### **Description**
Checks if a string ends with another string
---
### **Syntax**
```
: EndsWith(<string>, <string to search for>)
```
---
### **Examples**
```
. EndsWith("something", "thing")
```
**Result:** `true`
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 2
- **Max Operands:** 2
- **Idempotent:** true