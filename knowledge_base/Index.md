---
input_types:
- Collection<Any>
- Number
- Expression
output_type: Any
purpose:
- Collection Manipulation
- Data Access
---
# Operator: Index
---
### **Description**
Retrieves an element from an array or collection parameter at the requested index
---
### **Syntax**
```
: Index(<Collection>, <Index value>, [<expression to evaluate>])
ex1. Index([1, 5], 1) returns 5
ex2. Index(Products, 2, ProductScore) returns the value of member ProductScore present at index 2 in the list of Products
```
---
### **Examples**
No examples provided.
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 2
- **Max Operands:** 3
- **Idempotent:** false