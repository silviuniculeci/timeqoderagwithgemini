---
input_types:
- Collection
- Boolean
- Boolean
- Boolean
output_type: Boolean
purpose:
- Data Access
- Entity Manipulation
---
# Operator: SaveEntities
---
### **Description**
Saves a list of entities to database. The operator saves the data in batches thus being more efficient in saving large number of entities than saving them one by one using the SaveEntity operator)
---
### **Syntax**
```
: SaveEntities(<list of entities>, [<autosave relations (default is false)>], [<use transaction (default is true)>], [<force insert (default false)>])
```
---
### **Examples**
```
. SaveEntities(Products)
```
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 1
- **Max Operands:** 4
- **Idempotent:** false