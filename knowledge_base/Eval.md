---
input_types:
- Expression
output_type: Any
purpose:
- Control Flow
- Utility
---
# Operator: Eval
---
### **Description**
Evaluates a list of subexpressions and returns the value of the last one
---
### **Syntax**
```
: (<subexpression 1>, [<subexpression 2>], ...)
```
---
### **Examples**
```
. (1 + 2, 10)
```
**Result:** `10`
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 1
- **Max Operands:** 65535
- **Idempotent:** true