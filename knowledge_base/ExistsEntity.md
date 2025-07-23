---
input_types:
- EntityType
- Expression
output_type: Boolean
purpose:
- Data Access
- Entity Manipulation
- Logical
---
# Operator: ExistsEntity
---
### **Description**
Checks if an entity exists in the database
---
### **Syntax**
```
: ExistsEntity(<entity type>, [<filter expression>])
```
---
### **Examples**
```
. ExistsEntity(Product, id = 50)
```
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 2
- **Max Operands:** 2
- **Idempotent:** false