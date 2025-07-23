---
input_types:
- String
- Any
output_type: Any
purpose:
- Control Flow
- Utility
---
# Operator: EvalRule
---
### **Description**
Evaluates a dynamic rule passed as string and returns its value
---
### **Syntax**
```
: EvalRule(<expression string>, [<input parameter1> := <value1>], [<input parameter2> := <value2>], ...)
```
---
### **Examples**
```
EvalRule("1 + 2")
```
**Result:** `3`
```
EvalRule("@firstNumber + @secondNumber", @firstNumber := 1, @secondNumber := 2)
```
**Result:** `3`
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 1
- **Max Operands:** 1024
- **Idempotent:** false