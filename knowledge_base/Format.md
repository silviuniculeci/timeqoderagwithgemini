---
input_types:
- String
- Any
- Collection<Any>
output_type: String
purpose:
- String Manipulation
---
# Operator: Format
---
### **Description**
Replaces the items in the text template with the string representation of the corresponding objects.
syntax1: Format(<text template>, <1st parameter>, [<2nd parameter], ...[<nth parameter>])
syntax2: Format(<text template>, <collection of parameters>)
---
### **Syntax**
Not specified.
---
### **Examples**
```
. Format("There are {0} elements in the {1} list", 3, "products")
```
**Result:** `'There are 3 elements in the products list'`
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 2
- **Max Operands:** 65535
- **Idempotent:** true