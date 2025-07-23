---
input_types:
- Number
- Collection<Number>
output_type: Number
purpose:
- Aggregation
- Mathematical
---
# Operator: Max
---
### **Description**
Returns the maximum of the input operands (scalars or arrays)
---
### **Syntax**
```
: Max(<operand 1>, [<operand 2>], [... <operand n>])
ex1. Max(1, 5, 2) returns 5
ex2. Max([3, 5, 2], 6) returns 6
```
---
### **Examples**
No examples provided.
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 1
- **Max Operands:** 65535
- **Idempotent:** true