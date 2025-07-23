---
input_types:
- Collection<Any>
- Any
- Boolean
output_type: Collection<Any>
purpose:
- Collection Manipulation
---
# Operator: Sort
---
### **Description**
Returns a sorted list parameter - the list can be sorted ascending or descending
---
### **Syntax**
```
: Sort(<collection>, [<key selector (only for lists of entities) / keys collection>], [<sort descending (default is ascending)>])
```
---
### **Examples**
```
. Sort(RecommendedProducts, productHitCount, True)
```
**Result:** `a list of products ordered descending by productHitCount`
```
. Sort([1, 3, 2], Null, True)
```
**Result:** `the array {3, 2, 1}`
```
. Sort([2, 1, 3], Null, False)
```
**Result:** `the array {1, 2, 3}`
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 2
- **Max Operands:** 3
- **Idempotent:** true