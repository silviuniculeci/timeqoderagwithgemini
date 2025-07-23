---
input_types:
- Any
- Collection<Any>
output_type: Boolean
purpose:
- Logical
- Collection Manipulation
---
# Operator: In
---
### **Description**
Checks if the a value is present in the list of values
---
### **Syntax**
```
: <value> In <list of values>
```
---
### **Examples**
```
. 5 in [2, 7, 5, 3]
```
**Result:** `true`
---
### **Technical Details**
- **Type:** Infix Operator
- **Min Operands:** 2
- **Max Operands:** 2
- **Idempotent:** false