---
input_types:
- Collection
- Any
- Expression
output_type: Collection
purpose:
- Collection Manipulation
---
# Operator: RemoveItem
---
### **Description**
Removes an item from a collection (collection parameter or array)
---
### **Syntax**
```
: RemoveItem(<collection>, [<index - if none provided it removes the last element>], [<condition - pass null for index to use condition>])
```
```
: RemoveItem(<map>, <key>)
ex1: RemoveItem([2, 3, 4], 1) returns the array with elements: 2, 4
ex2: RemoveItem([2, 3, 4]) returns array with elements: 2, 3
ex3: RemoveItem([2, 3, 4], Null, CurrentValue = 2) returns array with elements: 3, 4
ex4: (@myMap := Map(), AddItem(@myMap, Date, Year(Date)), RemoveItem(@myMap, Year(Date)))
```
---
### **Examples**
No examples provided.
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 1
- **Max Operands:** 3
- **Idempotent:** false