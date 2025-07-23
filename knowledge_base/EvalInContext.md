---
input_types:
- Any
- Expression
output_type: Any
purpose:
- Control Flow
- Utility
---
# Operator: EvalInContext
---
### **Description**
Sets current value with the value of the first argument expression, evaluates the rest of arguments and returns the value of the last argument expression
---
### **Syntax**
```
: EvalInContext(<current value to set>, <expression 1 to evaluate>, [<expression N to evaluate>])
```
---
### **Examples**
```
. EvalInContext(1, CurrentValue)
```
**Result:** `1`
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 2
- **Max Operands:** 1024
- **Idempotent:** false