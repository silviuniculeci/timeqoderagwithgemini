---
input_types:
- Any
output_type: Entity
purpose:
- Utility
- Data Access
---
# Operator: CurrentFilter
---
### **Description**
Returns the current filter for the specified parameter reference as an object with properties: Value (the currently selected value), Term (text to be searched for), PageSize (number of max items to retrieve), Skip (number of items to skip)
---
### **Syntax**
```
: CurrentFilter(<parameter reference>)
```
---
### **Examples**
```
. CurrentFilter(ClientId)
```
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 1
- **Max Operands:** 1
- **Idempotent:** false