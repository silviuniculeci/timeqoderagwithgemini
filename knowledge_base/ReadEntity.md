---
input_types:
- EntityType
- Expression
output_type: Entity
purpose:
- Data Access
- Entity Manipulation
---
# Operator: ReadEntity
---
### **Description**
Reads an entity from database
---
### **Syntax**
```
: ReadEntity(<entity type>, [<filter expression>])
```
---
### **Examples**
```
. ReadEntity(Product, id = 2)
```
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 1
- **Max Operands:** 2
- **Idempotent:** false