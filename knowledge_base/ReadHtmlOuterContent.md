---
input_types: []
output_type: Collection
purpose:
- Data Access
- Data Transformation
---
# Operator: ReadHtmlOuterContent
---
### **Description**
Reads nodes from a Html source based on the provided xpath
---
### **Syntax**
```
: ReadHtmlContent()
```
---
### **Examples**
```
. ReadHtml("<html><body><div><p>name 1</p></div><div><p>name 2</p></div></body></html>", "//div", ReadHtmlOuterContent)
```
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 0
- **Max Operands:** 0
- **Idempotent:** false