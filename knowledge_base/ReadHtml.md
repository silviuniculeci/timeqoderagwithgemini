---
input_types:
- String
- String
- Expression
output_type: Collection<Any>
purpose:
- Data Access
- String Manipulation
- Collection Manipulation
---
# Operator: ReadHtml
---
### **Description**
Reads nodes from Html based on the provided xpath
---
### **Syntax**
```
: ReadHtml(<html source>, <nodes selector (xpath)>, <inner expression>)
```
---
### **Examples**
```
. ReadHtml("<html><body><div id="1">name 1</div><div id="2">name 2</div></body></html>", "//div", ReadHtmlContent)
```
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 3
- **Max Operands:** 3
- **Idempotent:** false