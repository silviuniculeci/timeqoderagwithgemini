---
input_types:
- String
output_type: String
purpose:
- String Manipulation
- Data Transformation
---
# Operator: ToXmlContent
---
### **Description**
Generates an xml part containing a string
---
### **Syntax**
```
: ToXmlContent(<string content>)
```
---
### **Examples**
```
. ToXmlContent('code > 100')
```
**Result:** `a string containing the xml part: code &gt; 100`
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 1
- **Max Operands:** 1
- **Idempotent:** false