---
input_types:
- Collection<Any>
- Expression
output_type: Boolean
purpose:
- Logical
- Collection Manipulation
---
# Operator: Any
---
### **Description**
Checks if any item in a collection (collection or array) matches the specified condition
---
### **Syntax**
```
: Any(<collection>, <condition>)
```
---
### **Examples**
```
: Any([2,3,4], CurrentValue = 2) evaluates to true
```
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 2
- **Max Operands:** 2
- **Idempotent:** false