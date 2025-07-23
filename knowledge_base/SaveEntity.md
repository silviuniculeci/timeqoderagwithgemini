---
input_types:
- Any
- Collection
output_type: Any
purpose:
- Data Access
- Entity Manipulation
---
# Operator: SaveEntity
---
### **Description**
Saves an entity or a list of entities to database. The operator returns the key value of the saved entity (when saving a list of entities returns a collection of keys)
---
### **Syntax**
```
: SaveEntity(<entity or list of entities>, [<force insert> / <update field 1>], [<update field 2>], ...)
ex1. SaveEntity(Product)
ex2. SaveEntity(Product, Id, Description)
```
---
### **Examples**
No examples provided.
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 1
- **Max Operands:** 1024
- **Idempotent:** false