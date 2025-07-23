---
input_types:
- String
output_type: String
purpose:
- Data Access
- String Manipulation
---
# Operator: ReadHtmlAttribute
---
### **Description**
Reads an attribute value from current Html element
---
### **Syntax**
```
: ReadHtmlAttribute(<attribute name>)
```
---
### **Examples**
```
. ReadHtml("<html><body><div id="1"></div><div id="2"></div></body></html>", "/div", ReadHtmlAttribute("id"))
```
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 1
- **Max Operands:** 1
- **Idempotent:** false