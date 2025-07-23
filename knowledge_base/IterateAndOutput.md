---
input_types:
- Any
- Expression
- Expression
- Boolean
output_type: Collection<Any>
purpose:
- Control Flow
- Collection Manipulation
---
# Operator: IterateAndOutput
---
### **Description**
Iterates over a collection / for a requested number of times and evaluates the second sub expression returning an array containing the values of every iteration
Optionally the operator accepts a condition used to filter iterations and a flag to perform removal of selected elements (based on the condition) from the source collection
The operator allows for using an expression like <collection / iterations count> In <parameter> that sets the current value on the specified parameter for each iteration
---
### **Syntax**
```
: IterateAndOutput(<collection / iterations count> | <collection / iterations count> In <parameter>, <iterator expression>, [<condition>], [<remove from collection (default is false)>])
ex1. IterateAndOutput(10, CurrentIndex) returns the array of integers {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
ex2. IterateAndOutput([1, 2, 3], CurrentValue + 1, CurrentValue > 1) returns the array {3, 4}
ex3. IterateAndOutput([1,-2,-3] In @currentNumber, Abs(@currentNumber)) returns the array {1, 2, 3}
ex4. IterateAndOutput([1, 2, 3] In @crtVal, @crtVal + 1, @crtVal > 1) returns the array {3, 4}
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