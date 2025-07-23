---
input_types:
- Collection<Any>
- Expression
output_type: Collection<Any>
purpose:
- Collection Manipulation
- Data Transformation
---
# Operator: Distinct
---
### **Description**
Iterates through a collection, and removes the duplicates based on the selected key
---
### **Syntax**
```
: Distinct(<collection>, [<key selector>], [<iteration expression>], [<duplicate item iteration expression>], [<new item expression>])
note 1: the output of the iteration expression is added to the output collection
note 2: for the duplicate item expression CurrentValue returns the existing item and CurrentValue(1) returns the current duplicate item from collection
note 3: if the duplicate expression returns a non null value then this value will replace the existing one
note 4: for the new item expression CurrentValue returns the output of the iteration expression and CurrentValue(1) returns the current item from collection
```
---
### **Examples**
```
: Distinct([1,2,2], CurrentValue)
```
**Result:** `the array [1, 2]`
```
. Distinct(Customers, customerEmail, customerEmail)
```
**Result:** `the customers unique emails`
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 1
- **Max Operands:** 5
- **Idempotent:** false