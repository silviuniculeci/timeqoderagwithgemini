---
input_types:
- String
- Number
- Number
output_type: String
purpose:
- String Manipulation
---
# Operator: SubStr
---
### **Description**
Extracts a part of a string
---
### **Syntax**
```
: SubStr(<string>, <start index>, [<length>])
observations:
- a negative length represents the length of the string minus the specified length
- a negative start index represents the length of the string minus the specified index
ex1. SubStr("test", 1) returns the string "est"
ex2. SubStr("test", 0, -1) returns the string "tes"
ex3. SubStr("test", -2) returns the string "st"
```
---
### **Examples**
```
. SubStr("test", 1, 2)
```
**Result:** `the string "es"`
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 2
- **Max Operands:** 3
- **Idempotent:** true