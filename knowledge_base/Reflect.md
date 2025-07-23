---
input_types:
- Any
- String
- Any
output_type: Any
purpose:
- Utility
---
# Operator: Reflect
---
### **Description**
Returns the requested field/property (third operand) from an object (first operand)
can also access properties with parameters by passing additional arguments
---
### **Syntax**
```
: Reflect(<target object>, <field/property name>, [<property parameter>])
```
---
### **Examples**
```
. Reflect(Date, "Millisecond")
```
**Result:** `current time millisecond`
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 2
- **Max Operands:** 3
- **Idempotent:** true