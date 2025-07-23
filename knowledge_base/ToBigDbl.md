---
input_types:
- Any
- String
output_type: Number
purpose:
- Data Transformation
- Utility
---
# Operator: ToBigDbl
---
### **Description**
Converts the operand to big decimal
---
### **Syntax**
```
: ToBigDbl(<value to convert>, [<culture name - if nothing is provided it uses the current culture>])
ex1. ToBigDbl("15000000000.13")
ex2. ToBigDbl("35000000000.1415", "en-US")
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