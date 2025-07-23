---
input_types:
- String
- Collection<String>
output_type: Boolean
purpose:
- Logical
- Data Access
---
# Operator: HasPermission
---
### **Description**
Checks if the current user has a certain permission
---
### **Syntax**
```
: HasPermission(<permission name / id>, [<additional permission name / id 1>, <additional permission name / id 2>, ...])
```
---
### **Examples**
```
. HasPermission("Administrator") checks if the current user has the Administrator permission
```
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 1
- **Max Operands:** 2147483647
- **Idempotent:** false