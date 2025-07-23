---
input_types:
- Number
output_type: Number
purpose:
- Control Flow
- Utility
---
# Operator: CurrentIndex
---
### **Description**
Returns current index inside an iteration operator
---
### **Syntax**
```
: CurrentIndex([<nesting level>])
```
---
### **Examples**
```
. Iterate(["A","Z"], CurrentIndex)
```
**Result:** `the array of integers [0, 1]`
```
. Iterate(Table(2, [1, 2, 3, 4]), Iterate(CurrentValue, CurrentIndex(1)))
```
**Result:** `the matrix [[0, 0], [1, 1]]`
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 0
- **Max Operands:** 1
- **Idempotent:** false