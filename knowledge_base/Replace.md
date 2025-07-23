---
input_types:
- String
- String
- String
output_type: String
purpose:
- String Manipulation
---
# Operator: Replace
---
### **Description**
Replaces all occurrences of one string (second operand) with another (third operand) in the first operand
---
### **Syntax**
Not specified.
---
### **Examples**
```
. Replace("Test 1", " ", "")
```
**Result:** `"Test1"`
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 3
- **Max Operands:** 3
- **Idempotent:** true