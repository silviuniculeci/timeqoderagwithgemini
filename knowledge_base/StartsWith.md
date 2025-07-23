---
input_types:
- String
- String
output_type: Boolean
purpose:
- String Manipulation
- Logical
---
# Operator: StartsWith
---
### **Description**
Checks if a string begins with another string
---
### **Syntax**
```
: StartsWith(<string>, <string to search for>)
```
---
### **Examples**
```
. StartsWith("something", "some")
```
**Result:** `true`
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 2
- **Max Operands:** 2
- **Idempotent:** true