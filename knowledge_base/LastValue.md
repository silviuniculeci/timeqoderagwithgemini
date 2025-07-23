---
input_types: []
output_type: Any
purpose:
- Control Flow
- Utility
---
# Operator: LastValue
---
### **Description**
Returns the previous value inside an iteration operator (last value is null for first operation)
---
### **Syntax**
Not specified.
---
### **Examples**
```
. IterateAndOutput([1, 2, 3], IsNull(LastValue, 0) + CurrentValue)
```
**Result:** `the array {1, 3, 5}`
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 0
- **Max Operands:** 0
- **Idempotent:** false