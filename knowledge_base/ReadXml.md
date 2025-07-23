---
input_types:
- String
- String
- Collection
- Expression
output_type: Collection
purpose:
- Data Access
- Data Transformation
---
# Operator: ReadXml
---
### **Description**
Reads matched nodes from an xml document
---
### **Syntax**
```
: ReadXml(<xml document>, <nodes selector (xpath)>, [<collection of namespace pairs Array(alias1, URI1, alias2, URI2, ...)>], [<xml read sub expression 1>])
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
- **Min Operands:** 2
- **Max Operands:** 4
- **Idempotent:** false