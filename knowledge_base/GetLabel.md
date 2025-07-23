---
input_types:
- String
- String
output_type: String
purpose:
- Data Access
- Entity Manipulation
---
# Operator: GetLabel
---
### **Description**
Retrieves the label for the current identifier
---
### **Syntax**
```
: GetLabel(<identifier>, [<culture code - default current culture>])
```
---
### **Examples**
```
. GetLabel("identifier")
```
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 1
- **Max Operands:** 2
- **Idempotent:** false