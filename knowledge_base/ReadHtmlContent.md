---
input_types:
- Boolean
output_type: String
purpose:
- Data Access
- String Manipulation
---
# Operator: ReadHtmlContent
---
### **Description**
Reads nodes from a Html source based on the provided xpath
---
### **Syntax**
```
: ReadHtmlContent([<extract text (default: false)>])
```
---
### **Examples**
```
. ReadHtml("<html><body><div><p>name 1</p></div><div><p>name 2</p></div></body></html>", "//div", ReadHtmlContent)
```
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 0
- **Max Operands:** 1
- **Idempotent:** false