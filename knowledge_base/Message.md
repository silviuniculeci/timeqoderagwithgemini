---
input_types:
- String
- String
- Boolean
output_type: 'Null'
purpose:
- Utility
---
# Operator: Message
---
### **Description**
Generates a message that will be displayed to the user
---
### **Syntax**
```
: Message(<message id / message identifier / message text>, [<message type: Info (default), Warning, Error, System>], [<display message in popup (default is false)>])
```
---
### **Examples**
```
. Message("The client was modified", Info)
```
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 1
- **Max Operands:** 3
- **Idempotent:** false