---
input_types:
- EntityType
- Expression
- String
output_type: Number
purpose:
- Data Access
- Aggregation
---
# Operator: CountEntities
---
### **Description**
Counts the number of entities from database
---
### **Syntax**
```
: CountEntities(<entity type>, [<filter expression>], [<count member>])
```
---
### **Examples**
```
. CountEntities(Product, value > 50)
```
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 1
- **Max Operands:** 3
- **Idempotent:** false