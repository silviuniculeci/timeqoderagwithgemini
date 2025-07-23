---
input_types:
- String
- String
output_type: Any
purpose:
- Data Access
---
# Operator: ReadConfiguration
---
### **Description**
Reads values from the configuration settings
---
### **Syntax**
```
: ReadConfiguration(<configuration key>, [<configuration sub key>])
```
---
### **Examples**
```
. ReadConfiguration("SMTP", "Email")
```
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 1
- **Max Operands:** 2
- **Idempotent:** true