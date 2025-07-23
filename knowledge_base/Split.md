---
input_types:
- String
- String
output_type: Collection<String>
purpose:
- String Manipulation
---
# Operator: Split
---
### **Description**
Splits a string by the specified separator
---
### **Syntax**
Not specified.
---
### **Examples**
```
. Split("2,3,4", ",")
```
**Result:** `a collection composed of strings "2","3" and "4"`
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 2
- **Max Operands:** 2
- **Idempotent:** true