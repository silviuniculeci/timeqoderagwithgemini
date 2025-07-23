---
input_types:
- Collection<Any>
- Expression
output_type: Number
purpose:
- Aggregation
- Collection Manipulation
---
# Operator: Count
---
### **Description**
Returns the number of elements from a collection that validate the condition
---
### **Syntax**
```
: Count(<collection>, <filtering condition>)
```
---
### **Examples**
```
: Count([2,3,4], CurrentValue % 2 = 0)
```
**Result:** `2`
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 2
- **Max Operands:** 2
- **Idempotent:** true