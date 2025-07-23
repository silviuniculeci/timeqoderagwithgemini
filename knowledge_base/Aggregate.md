---
input_types:
- Collection<Any>
- Expression
- Any
output_type: Any
purpose:
- Aggregation
- Collection Manipulation
---
# Operator: Aggregate
---
### **Description**
Iterates through a collection, evaluates a sub expression for each iteration and returns the value evaluated in the last iteration
---
### **Syntax**
```
: Aggregate(<collection>, <iteration expression>, [<initial value>])
```
---
### **Examples**
```
: Aggregate([1,2,3], LastValue + CurrentValue, 0)
```
**Result:** `6`
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 2
- **Max Operands:** 3
- **Idempotent:** false