---
input_types:
- Number
- Collection<Any>
output_type: Collection<Collection<Any>>
purpose:
- Data Transformation
- Collection Manipulation
---
# Operator: Table
---
### **Description**
Returns a matrix from a collection by considering a specified number of sequential values as a row
---
### **Syntax**
```
: Table(<columns count>, <collection of values>)
```
---
### **Examples**
```
. Table(2, [1, "item 1", 2, "item 2"]) will return a matrix with two rows and two columns
```
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 2
- **Max Operands:** 2
- **Idempotent:** true