---
input_types:
- Any
- Any
output_type: Any
purpose:
- Logical
- Utility
---
# Operator: IsNull
---
### **Description**
Check for null or returns the first operand if is not null otherwise the second one
---
### **Syntax**
```
: IsNull(<value>, [<default value>])
ex1. IsNull(param, 0) returns 0 if param is null
ex2. IsNull(param) returns true is param is null
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