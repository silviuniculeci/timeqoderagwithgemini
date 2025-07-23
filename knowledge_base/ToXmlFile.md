---
input_types:
- String
- String
- Any
output_type: Boolean
purpose:
- Plugin & Integration
- Data Transformation
---
# Operator: ToXmlFile
---
### **Description**
Generates an xml document in a local file
---
### **Syntax**
```
: ToXmlFile(<file name>, <xml node>, [<inner xml 1>], [<inner xml 2>], ...)
```
---
### **Examples**
```
. ToXmlFile('d:\temp\output.xml', 'root', Iterate(Table(2, [1, 'value 1', 2, 'value 2']), ToXml('item', ToXmlAttr(['id', 'value'], CurrentValue))))
writes the xml <root><item id="1" value="value 1"/><item id="2" value="value 2"/></root> to the local file output.xml
```
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 2
- **Max Operands:** 65535
- **Idempotent:** false