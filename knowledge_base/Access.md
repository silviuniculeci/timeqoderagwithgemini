---
input_types:
- Entity
- String
output_type: Any
purpose:
- Data Access
- Entity Manipulation
---
# Operator: .
---
### **Description**
Accesses the value of a member from an entity type value
---
### **Syntax**
Not specified.
---
### **Examples**
```
. ReadEntity(Person, false, id, 10).name
```
---
### **Technical Details**
- **Type:** Infix Operator
- **Min Operands:** 2
- **Max Operands:** 2
- **Idempotent:** false