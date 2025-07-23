---
input_types:
- Collection<Any>
output_type: Collection<Any>
purpose:
- Collection Manipulation
---
# Operator: Concat
---
### **Description**
Concatenates two or more arrays
---
### **Syntax**
```
: Concat(<collection 1>, <collection 2>,...)
```
---
### **Examples**
```
. Concat([1, 5], [2], [4])
```
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 1
- **Max Operands:** 65535
- **Idempotent:** true