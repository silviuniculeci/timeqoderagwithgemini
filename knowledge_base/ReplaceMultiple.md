---
input_types:
- String
- Collection
- String
output_type: String
purpose:
- String Manipulation
---
# Operator: ReplaceMultiple
---
### **Description**
Replaces all occurrences of multiples string with another (last operand) in the first operand
---
### **Syntax**
Not specified.
---
### **Examples**
```
. ReplaceMultiple("Trap 1", " ", "r", "")
```
**Result:** `"Tap1"`
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 1
- **Max Operands:** 65535
- **Idempotent:** true