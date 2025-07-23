---
input_types:
- String
output_type: Boolean
purpose:
- Utility
---
# Operator: CheckIBAN
---
### **Description**
Verifies the validity of an IBAN
---
### **Syntax**
Not specified.
---
### **Examples**
```
. CheckIBAN("RO30INGB0000999900856881")
```
**Result:** `true`
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 1
- **Max Operands:** 1
- **Idempotent:** true