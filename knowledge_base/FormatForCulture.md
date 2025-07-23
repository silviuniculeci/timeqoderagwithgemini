---
input_types:
- String
- Boolean
- String
- Any
- Collection<Any>
output_type: String
purpose:
- String Manipulation
- Utility
---
# Operator: FormatForCulture
---
### **Description**
Replaces the items in the text template with the string representation of the corresponding objects using a specific culture.
syntax1: FormatForCulture([<culture code>], <use system culture>, <text template>, <1st parameter>, [<2nd parameter], ...[<nth parameter>])
syntax2: FormatForCulture([<culture code>], <use system culture>, <text template>, <collection of parameters>)
---
### **Syntax**
Not specified.
---
### **Examples**
```
. FormatForCulture("de-DE", true, "There {0} weights {1} grams", "apple", 95.6)
```
**Result:** `'There apple weights 95,6 grams'`
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 4
- **Max Operands:** 1024
- **Idempotent:** true