---
input_types:
- Any
output_type: Collection<Any>
purpose:
- Collection Manipulation
- Utility
---
# Operator: StaticArray
---
### **Description**
Creates a constant collection of values from the list of operands
---
### **Syntax**
```
: StaticArray([<value 1>], [<value 2>], ...)
```
---
### **Examples**
```
. StaticArray(1, 5, 2)
```
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 0
- **Max Operands:** 65535
- **Idempotent:** true