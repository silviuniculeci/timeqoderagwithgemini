---
input_types:
- String
- String
- Expression
output_type: Any
purpose:
- Data Access
- String Manipulation
---
# Operator: ReadFirstHtml
---
### **Description**
Reads the first node from the source Html based on the provided xpath
---
### **Syntax**
```
: ReadFirstHtml(<html source / null>, <node selector (xpath)>, <inner expression>)
```
---
### **Examples**
```
. ReadFirstHtml("<html><body><div id="1">name 1</div><div id="2">name 2</div></body></html>", "//div[@id='2']", ReadHtmlContent)
```
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 3
- **Max Operands:** 3
- **Idempotent:** false