---
input_types:
- Number
- Any
output_type: Collection<Any>
purpose:
- Collection Manipulation
---
# Operator: InitArray
---
### **Description**
Creates a new array of the specified number of elements all having the value passed as the second operand
---
### **Syntax**
```
: InitArray(<number of elements>, <value of elements>)
```
---
### **Examples**
```
. InitArray(3, 5)
```
**Result:** `a collection with 3 elements all having the value 5`
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 2
- **Max Operands:** 2
- **Idempotent:** false