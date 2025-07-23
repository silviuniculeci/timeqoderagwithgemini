---
input_types:
- Number
- Number
- Number
output_type: Number
purpose:
- Mathematical
---
# Operator: Round
---
### **Description**
Rounds one number (first operand) by the specified number of decimals(second operand)
---
### **Syntax**
```
: Round(<value>, <decimals>, [<rounding type: 0 - closest number (default), 1 - up, 2 - down>])
```
---
### **Examples**
```
. Round(1.436, 2)
```
**Result:** `1.44`
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 2
- **Max Operands:** 3
- **Idempotent:** true