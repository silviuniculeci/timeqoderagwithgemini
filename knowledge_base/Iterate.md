---
input_types:
- Any
- Expression
- Expression
- Boolean
output_type: Any
purpose:
- Control Flow
- Collection Manipulation
---
# Operator: Iterate
---
### **Description**
Iterates over a collection or for a number of times and evaluates the second sub expression returning the value of the last iteration
Optionally the operator accepts a condition used to filter iterations and a flag to perform removal of selected elements (based on the condition) from the source collection
The operator allows for using an expression like <collection / iterations count> In <parameter> that sets the current value on the specified parameter for each iteration
---
### **Syntax**
```
: Iterate(<collection / iterations count> | <collection / iterations count> In <parameter>, <iterator expression>, [<condition>], [<remove from collection (default is false)>])
ex1. (@collection := [1, -2, -3], Iterate(@collection, Index(@collection, CurrentIndex) := Abs(CurrentValue))) makes all the values positive in the collection and returns the value 3
ex2. Iterate([1, 2, 3], CurrentValue + 1, CurrentValue > 1) returns the value 4
ex3. Iterate([1,-2,-3] In @currentNumber, Abs(@currentNumber)) returns the value 3
```
---
### **Examples**
No examples provided.
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 2
- **Max Operands:** 4
- **Idempotent:** false