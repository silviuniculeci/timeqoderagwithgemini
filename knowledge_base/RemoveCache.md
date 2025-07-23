---
input_types:
- String
- Number
output_type: Any
purpose:
- Utility
---
# Operator: RemoveCache
---
### **Description**
Removes some cached data based on a key. The operator returns the removed cache data, if the key was found in cache, otherwise returns null
---
### **Syntax**
```
: RemoveCache(<key>, [<cache type: 0 - module (default), 1 - session, 2 - request, 3 - domain, 4 - global, 5 - localOnDomain, 6 - localOnModule>]])
```
---
### **Examples**
```
: RemoveCache("UsersList") removes from current module's cache some previously cached data with the key "UsersList"
```
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 1
- **Max Operands:** 2
- **Idempotent:** false