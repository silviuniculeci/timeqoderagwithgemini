---
input_types:
- Number
output_type: Collection
purpose:
- Data Access
---
# Operator: ReadMoreEntities
---
### **Description**
Starts the reading a list of entities from database
---
### **Syntax**
```
: ReadMoreEntities(<top rows to read>)
```
---
### **Examples**
```
1. StartReadingEntities(Product, value > 50, value, true, @products := ReadMoreEntities(100))
```
```
2. StartReadingEntities(Product, value > 50, [category, value], [true, false], @products := ReadMoreEntities(100))
```
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 1
- **Max Operands:** 1
- **Idempotent:** false