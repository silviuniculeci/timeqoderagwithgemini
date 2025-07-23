---
input_types:
- Entity
- EntityType
- Expression
output_type: Number
purpose:
- Data Access
- Entity Manipulation
---
# Operator: DeleteEntity
---
### **Description**
Deletes a single row from database identified by the provided entity instance / deletes multiple rows from database based on a filtering expression. The operator returns the number of deleted rows.
---
### **Syntax**
```
: DeleteEntity(<parameter / entity>, [<filter expression>])
ex1. DeleteEntity(SelectedProduct)
ex2. DeleteEntity(Products, expirationDate > DateAdd(Date, -1, day)
```
---
### **Examples**
No examples provided.
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 1
- **Max Operands:** 2
- **Idempotent:** false