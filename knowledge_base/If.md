---
input_types:
- Boolean
- Any
- Any
output_type: Any
purpose:
- Control Flow
- Logical
---
# Operator: If
---
### **Description**
If the first operand is true returns second operand else returns the third operand
---
### **Syntax**
```
: If(<condition>, <true expression>, [<false expression>])
```
```
If(<condition 1>, <true expression 1>, <condition 2>, <true expression 2>, ...,<condition n>, <true expression n> [<false expression n>])
The operator can be used with two operands only and returns null when the condition is false
```
---
### **Examples**
```
. If(1 > 2, 5, 6)
```
**Result:** `6`
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 2
- **Max Operands:** 65
- **Idempotent:** true