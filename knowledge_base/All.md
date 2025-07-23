---
input_types:
- Collection<Any>
- Expression
output_type: Boolean
purpose:
- Logical
- Collection Manipulation
---
# Operator: All
---
### **Description**
Checks if all items in a collection (collection or array) match the specified condition
---
### **Syntax**
```
: All(<collection>, <condition>)
```
---
### **Examples**
```
: All([2,4,8], CurrentValue % 2 = 0) evaluates to true
```
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 2
- **Max Operands:** 2
- **Idempotent:** false