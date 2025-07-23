---
input_types:
- Collection<Any>
- Boolean
- Expression
- Any
- Boolean
output_type: Any
purpose:
- Collection Manipulation
- Data Access
---
# Operator: First
---
### **Description**
Returns the first element from a collection that validates the condition
---
### **Syntax**
```
: First(<collection>, [<filtering condition>], [<value selector>], [<default value>], [<search backward>])
```
---
### **Examples**
```
First([2,3,4])
```
**Result:** `2`
```
First([2,3,4], True, CurrentValue > 2)
```
**Result:** `3`
```
First([2,3,4,5,6], CurrentValue % 2 = 1, CurrentValue * 10, 0, true)
```
**Result:** `50`
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 1
- **Max Operands:** 5
- **Idempotent:** false