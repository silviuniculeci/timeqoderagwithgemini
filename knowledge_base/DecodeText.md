---
input_types:
- Collection<Number>
- String
output_type: String
purpose:
- Data Transformation
- String Manipulation
---
# Operator: DecodeText
---
### **Description**
Decodes data to string
---
### **Syntax**
```
: DecodeText(<input data>, [<encoding: UTF8 (default), Unicode, ASCII, Base64, HexString>])
```
---
### **Examples**
```
. DecodeText([79, 75], "UTF8")
```
**Result:** `"OK"`
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 1
- **Max Operands:** 2
- **Idempotent:** true