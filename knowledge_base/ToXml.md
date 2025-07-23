---
input_types:
- String
- Any
output_type: String
purpose:
- Data Transformation
- Utility
---
# Operator: ToXml
---
### **Description**
Generates an xml document in memory
---
### **Syntax**
```
: ToXml(<xml node>, [<inner xml 1>], [<inner xml 2>], ...)
```
---
### **Examples**
```
. ToXml('root', Iterate(Table(2, [1, 'value 1', 2, 'value 2']), ToXml('item', ToXmlAttr(['id', 'value'], CurrentValue))))
returns a string containing the xml <root><item id="1" value="value 1"/><item id="2" value="value 2"/></root>
```
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 1
- **Max Operands:** 65535
- **Idempotent:** false