---
input_types:
- EntityType
- Expression
- Expression
output_type: Number
purpose:
- Entity Manipulation
- Data Access
---
# Operator: UpdateEntity
---
### **Description**
Updates an entity's members directly in the database
---
### **Syntax**
```
: UpdateEntity(<entity type>, [<filter expression>], [<set member expression>], [<set member expression 2>], ...)
```
---
### **Examples**
```
. UpdateEntity(Product, id = 13, isDisable := true)
```
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 3
- **Max Operands:** 1024
- **Idempotent:** false