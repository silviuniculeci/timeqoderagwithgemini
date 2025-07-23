---
input_types:
- Any
- Number
output_type: Any
purpose:
- Utility
---
# Operator: Clone
---
### **Description**
Clones an object
---
### **Syntax**
```
: Clone(<value to clone>, [<levels - default is unlimited>])
```
---
### **Examples**
```
. Clone([3, 1, 5])
```
**Result:** `another identical array [3,1,5]`
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 1
- **Max Operands:** 2
- **Idempotent:** true