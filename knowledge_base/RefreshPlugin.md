---
input_types:
- String
- Boolean
output_type: Boolean
purpose:
- Plugin & Integration
---
# Operator: RefreshPlugin
---
### **Description**
Refreshes a plugin's output
---
### **Syntax**
```
: RefreshPlugin(<plugin id / identifier>, [<refresh all calls of plugin (Default: True)>])
```
---
### **Examples**
```
. RefreshPlugin(10, True) refreshes all outputs of plugin with id 10
```
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 1
- **Max Operands:** 2
- **Idempotent:** false