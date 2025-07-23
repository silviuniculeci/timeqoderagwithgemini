---
input_types:
- String
output_type: Any
purpose:
- Control Flow
- Utility
---
# Operator: FireEvent
---
### **Description**
Triggers an event from current view
---
### **Syntax**
```
: FireEvent(<event name>)
```
---
### **Examples**
```
. FireEvent("refreshData") triggers the event named refreshData
```
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 1
- **Max Operands:** 1
- **Idempotent:** false