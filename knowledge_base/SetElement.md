---
input_types:
- Collection
- Number
- Any
output_type: Collection
purpose:
- Collection Manipulation
---
# Operator: SetElement
---
### **Description**
Changes an element from a collection at a specified index
---
### **Syntax**
Not specified.
---
### **Examples**
```
. SetElement([3, 1, 5], 1, 5)
```
**Result:** `the collection [3, 5, 5]`
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 3
- **Max Operands:** 3
- **Idempotent:** true