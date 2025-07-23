---
input_types:
- EntityType
- Expression
- Collection<String>
- Number
- Number
- Boolean
output_type: Collection<Entity>
purpose:
- Data Access
- Entity Manipulation
- Collection Manipulation
---
# Operator: ReadEntities
---
### **Description**
Reads a list of entities from database
---
### **Syntax**
```
: ReadEntities(<entity type>, [<filter expression>], [<order by>], [<top>], [<skip>], [<order ascending (default value is true)>])
```
---
### **Examples**
```
1. ReadEntities(Product, value > 50, value, 10)
```
```
2. ReadEntities(Product, value > 50, [category, value], 10)
```
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 1
- **Max Operands:** 6
- **Idempotent:** false