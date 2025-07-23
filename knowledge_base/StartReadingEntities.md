---
input_types:
- EntityType
- Expression
- Any
- Boolean
- Expression
output_type: Boolean
purpose:
- Data Access
- Entity Manipulation
---
# Operator: StartReadingEntities
---
### **Description**
Starts the reading a list of entities from database
---
### **Syntax**
```
: StartReadingEntities(<entity type>, [<filter expression>], [<order by>], [<order ascending (default value is true)>], [<inner read expression>])
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
- **Min Operands:** 5
- **Max Operands:** 5
- **Idempotent:** false