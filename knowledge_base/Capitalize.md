---
input_types:
- String
- Boolean
output_type: String
purpose:
- String Manipulation
---
# Operator: Capitalize
---
### **Description**
Converts the first character of a string to uppercase
---
### **Syntax**
```
: Capitalize(<string>, [<capitalize each word (default is false)>])
```
---
### **Examples**
```
. Capitalize("something")
```
**Result:** `the string "Something"`
```
. Capitalize("first last", true)
```
**Result:** `the string "First Last"`
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 1
- **Max Operands:** 2
- **Idempotent:** true