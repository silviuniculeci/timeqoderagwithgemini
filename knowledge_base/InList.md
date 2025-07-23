---
input_types:
- Any
- Any
- Collection<Any>
output_type: Boolean
purpose:
- Logical
- Collection Manipulation
---
# Operator: InList
---
### **Description**
Checks if the first operand is present among the others
---
### **Syntax**
```
: InList(<searched value>, <value 1 / collection of values>, [<value 2 / collection of values>], ...)
ex1. InList(1, 3, 2, 1) returns true
ex2. InList(1, [1, 3]) returns true
```
---
### **Examples**
No examples provided.
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 2
- **Max Operands:** 65535
- **Idempotent:** true