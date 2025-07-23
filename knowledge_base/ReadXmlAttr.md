---
input_types:
- String
- String
output_type: String
purpose:
- Data Access
- Data Transformation
---
# Operator: ReadXmlAttr
---
### **Description**
Reads the attribute value from an xml node
---
### **Syntax**
```
: ReadXmlAttr(<attribute name>, [<namespace uri>])
```
---
### **Examples**
```
. ReadXml('<root><item id="1"/><item id="2"/></root>', '/root/item', Null, ReadXmlAttr('id'))
returns an array of strings containing the value of id attribute for all item nodes
```
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 1
- **Max Operands:** 2
- **Idempotent:** false