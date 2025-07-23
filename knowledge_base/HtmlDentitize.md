---
input_types:
- String
output_type: String
purpose:
- String Manipulation
- Data Transformation
---
# Operator: HtmlDentitize
---
### **Description**
Converts an Html string to string
---
### **Syntax**
```
: HtmlDentitize(<html string>)
```
---
### **Examples**
```
. HtmlDentitize("this &amp; that")
```
**Result:** `the string "this & that"`
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 1
- **Max Operands:** 1
- **Idempotent:** false