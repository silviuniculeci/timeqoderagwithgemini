---
input_types:
- Boolean
output_type: String
purpose:
- Error Handling
---
# Operator: LastError
---
### **Description**
Retrieves the last generated error message from using a Try operator
---
### **Syntax**
```
: LastError([<get top error message (default: true)>])
```
---
### **Examples**
```
. Try(Index([1, 2], -1), LastError)
```
**Result:** `the error message generated by trying to access an incorrect index`
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 0
- **Max Operands:** 1
- **Idempotent:** false