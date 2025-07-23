---
input_types: []
output_type: String
purpose:
- Data Access
- Data Transformation
---
# Operator: ReadXmlValue
---
### **Description**
Reads the content of an xml node
---
### **Syntax**
```
: ReadXmlValue([<node selector 1 (xpath)>], [node selector 2 (xpath)>], ...)
```
---
### **Examples**
```
. ReadXml('<root><item>1</item><item>2</item></root>', '/root/item', Null, ReadXmlValue())
returns an array of strings containing the value of item node for all nodes in the root node
```
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 0
- **Max Operands:** 65535
- **Idempotent:** false