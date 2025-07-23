---
input_types:
- String
- String
- Collection<Any>
- Expression
output_type: Any
purpose:
- Data Access
- String Manipulation
---
# Operator: ReadFirstXml
---
### **Description**
Reads first matched node from an xml document
---
### **Syntax**
```
: ReadFirstXml(<xml document>, <nodes selector (xpath)>, [<collection of namespace pairs (alias-URI)>], [<xml read subexpression 1>])
```
---
### **Examples**
```
. ReadFirstXml('<root><item id="1"/><item id="2"/></root>', '/root/item', Null, ReadXmlAttr('id'))
```
**Result:** `the string "1"`
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 2
- **Max Operands:** 4
- **Idempotent:** false