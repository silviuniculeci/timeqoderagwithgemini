---
input_types:
- String
- String
- String
output_type: String
purpose:
- String Manipulation
---
# Operator: RegEx
---
### **Description**
Extracts matched pattern (second operand) from a string(first operand)
---
### **Syntax**
```
: RegEx(<source text>, <regular expression>, [<operating mode (default: merged)>])
modes: merged (all groups from all matches), collection (collection of all matches), groups (collection of matches with a sublist of group values), detailedGroups
```
---
### **Examples**
```
. RegEx("Test2","[A-Za-z]+")
```
**Result:** `"Test"`
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 2
- **Max Operands:** 3
- **Idempotent:** true