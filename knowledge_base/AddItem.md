---
input_types:
- Collection<Any>
- Any
- Any
output_type: Collection<Any>
purpose:
- Collection Manipulation
---
# Operator: AddItem
---
### **Description**
Adds a new item to a collection or map (collection parameter or map or an array)
syntax1: AddItem(<collection>, <value>, [<index>]) 
syntax2: AddItem(<map>, <value>, <key>)
ex1: AddItem([2,3,4], 0, 1) returns the array [2, 0, 3, 4]
ex2: (@myMap := Map(), AddItem(@myMap, Date, Year(Date))) adds the current date using the current year as key to an existing map
---
### **Syntax**
Not specified.
---
### **Examples**
No examples provided.
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 2
- **Max Operands:** 3
- **Idempotent:** false