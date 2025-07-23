---
input_types:
- String
output_type: Any
purpose:
- Error Handling
---
# Operator: Error
---
### **Description**
Generates an exception error
---
### **Syntax**
```
: Error([<error message (if no message is provided then it generates the last error if there is one otherwise it returns null)>])
ex1. Error("Invalid date")
generates an exception error containing the message "Invalid date"
ex2. Error() generates the last error exception
```
---
### **Examples**
No examples provided.
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 0
- **Max Operands:** 1
- **Idempotent:** false