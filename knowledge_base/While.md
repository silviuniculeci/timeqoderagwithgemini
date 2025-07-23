---
input_types:
- Boolean
- Expression
output_type: Any
purpose:
- Control Flow
---
# Operator: While
---
### **Description**
Evaluates the second operand while the condition (first operand) evaluates to true and returns the value of the last iteration
---
### **Syntax**
Not specified.
---
### **Examples**
```
. While(CurrentIndex < 10, @counter := IsNull(@counter, 0) + CurrentIndex)
```
**Result:** `the sum of numbers from 1 to 10`
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 2
- **Max Operands:** 2
- **Idempotent:** true