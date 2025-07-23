---
input_types:
- Expression
output_type: String
purpose:
- Plugin & Integration
- Data Access
---
# Operator: BusinessCentralFilter
---
### **Description**
Generates Business Central filter clause (can be used only with OData ReadMultiple plugin)
---
### **Syntax**
```
: BusinessCentralFilter(<filter clause>)
operators: <, <=, <>, =, >, >=, And, EndsWith, In, InList, IsNotNull, IsNull, Like, Lower, Or, StartsWith, Upper
```
---
### **Examples**
```
. BusinessCentralFilter(BC.No > 1500 And (StartsWith(BC.Description, "MLP") Or BC.No = 1600))
```
**Result:** `the string "(No gt 1500 and (startsWith(Description, "'MLP'")) or No eq 1600)"`
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 1
- **Max Operands:** 1
- **Idempotent:** false