---
input_types: []
output_type: Collection
purpose:
- Data Access
- Data Transformation
---
# Operator: ReadHtmlText
---
### **Description**
Reads nodes from a Html source based on the provided xpath
---
### **Syntax**
```
: ReadHtmlText()
```
---
### **Examples**
```
. ReadHtml("<html><body><div id="1">name 1</div><div id="2">name 2</div></body></html>", "//div", ReadHtmlText)
```
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 0
- **Max Operands:** 0
- **Idempotent:** false