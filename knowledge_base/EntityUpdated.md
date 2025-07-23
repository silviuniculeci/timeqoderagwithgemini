---
input_types:
- Entity
- Collection<Entity>
- String
output_type: Boolean
purpose:
- Entity Manipulation
- Logical
---
# Operator: EntityUpdated
---
### **Description**
Checks if an entity instance is updated (contains pending changes)
---
### **Syntax**
```
: EntityUpdated(<entity value / collection of entities>, [<entity member name])
```
---
### **Examples**
```
. EntityUpdated(SelectedProduct)
```
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 1
- **Max Operands:** 2
- **Idempotent:** false