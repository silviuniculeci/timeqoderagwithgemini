---
input_types:
- String
output_type: Collection<Number>
purpose:
- Data Transformation
- String Manipulation
---
# Operator: EncodeText
---
### **Description**
Encodes from string to data
---
### **Syntax**
```
: EncodeText(<input text>, [<encoding - UTF8 (default), Unicode, ASCII, Base64, HexString>])
```
---
### **Examples**
```
. EncodeText("OK", "UTF8")
```
**Result:** `[79, 75]`
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 1
- **Max Operands:** 2
- **Idempotent:** true