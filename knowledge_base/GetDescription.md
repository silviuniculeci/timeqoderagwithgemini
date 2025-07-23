---
input_types:
- Any
- String
output_type: String
purpose:
- Data Access
- Entity Manipulation
---
# Operator: GetDescription
---
### **Description**
Retrieves the description for the current value of a parameter
---
### **Syntax**
```
: GetDescription(<parameter>, [<culture code>])
```
---
### **Examples**
```
. GetDescription(Status)
```
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 1
- **Max Operands:** 2
- **Idempotent:** false