---
input_types:
- Collection
- Expression
output_type: Collection
purpose:
- Collection Manipulation
---
# Operator: RemoveMultiple
---
### **Description**
Removes multiple items from a collection (collection parameter or array)
---
### **Syntax**
```
: RemoveMultiple(<collection>, [<condition - if no condition is provided removes all elements>])
ex1: RemoveMultiple([2, 3, 4], CurrentValue % 2 = 0) returns the array with elements: 3
ex2: RemoveMultiple([2, 3, 4] returns an empty array
```
---
### **Examples**
No examples provided.
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 1
- **Max Operands:** 2
- **Idempotent:** false