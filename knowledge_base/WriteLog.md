---
input_types:
- String
- String
- String
- String
output_type: 'Null'
purpose:
- Utility
- Plugin & Integration
---
# Operator: WriteLog
---
### **Description**
Writes a message to the log file
---
### **Syntax**
```
: WriteLog(<operation name>, [<details>], [<level (Info, Error, Warning)>], [<error / error message>])
ex1. WriteLog("UpdateOrder", "id:1")
ex1. WriteLog("UpdateOrder", "id:1", "Warning")
ex2. WriteLog("UpdateOrder", "id:1", "Error", "error message")
```
---
### **Examples**
No examples provided.
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 1
- **Max Operands:** 4
- **Idempotent:** false