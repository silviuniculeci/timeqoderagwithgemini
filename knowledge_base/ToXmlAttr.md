---
input_types:
- Any
- Any
output_type: String
purpose:
- Data Transformation
- Utility
---
# Operator: ToXmlAttr
---
### **Description**
Generates an xml part containing one or more attributes
---
### **Syntax**
```
: ToXmlAttr(<attribute name / attribute names collection>, <value / values collection>, [<attribute name 2>, <value 2>], ...)
ex1. ToXmlAttr('code', 101, 'name', 'some product') returns a string containing the xml part: code="100" name="product 100"
ex2. ToXmlAttr(['code','name'], [101, 'some product'])
```
---
### **Examples**
No examples provided.
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 2
- **Max Operands:** 65535
- **Idempotent:** false