---
input_types:
- Any
- Boolean
output_type: String
purpose:
- Control Flow
---
# Operator: SetNextState
---
### **Description**
Specifies the next state the workflow should go to (returns the state id)
---
### **Syntax**
```
: SetNextState(<state id / state name>, [<set next state until decision moment (default is false)>])
```
---
### **Examples**
No examples provided.
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 1
- **Max Operands:** 2
- **Idempotent:** false