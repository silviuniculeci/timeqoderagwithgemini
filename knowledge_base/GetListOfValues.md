---
input_types:
- Number
output_type: Collection<Any>
purpose:
- Data Access
---
# Operator: GetListOfValues
---
### **Description**
Retrieves the list of values associated to an id
---
### **Syntax**
```
: GetListOfValues<key-value list id>)
```
---
### **Examples**
```
. GetListOfValues(10)
```
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 1
- **Max Operands:** 1
- **Idempotent:** false