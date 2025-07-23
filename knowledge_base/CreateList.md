---
input_types:
- EntityType
- Collection<Collection<Any>>
- String
output_type: Collection<Entity>
purpose:
- Entity Manipulation
- Collection Manipulation
---
# Operator: CreateList
---
### **Description**
Creates a multi-valued parameter from a matrix by mapping columns from the matrix to members of the entity type
---
### **Syntax**
```
: CreateList(<entity type>, [<matrix>], [<member1>], [<member2>], ...)
```
---
### **Examples**
```
. CreateList(OptionsType, Table(2, [1, "Option 1", 2, "Option 2"]), Id, Description)
```
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 1
- **Max Operands:** 1024
- **Idempotent:** false