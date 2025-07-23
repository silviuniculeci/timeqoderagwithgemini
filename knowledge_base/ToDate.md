---
input_types:
- String
- String
- String
output_type: Date
purpose:
- Data Transformation
- Date & Time
---
# Operator: ToDate
---
### **Description**
Converts a string to a date using the passed format
---
### **Syntax**
```
: ToDate(<string date>, [<format>], [<culture name - if nothing is provided it uses current culture>])
ex1. ToDate("15/02/2009", "dd/MM/yyyy")
ex2. ToDate("15Jul2009", "ddMMMyyyy", "en-US")
```
---
### **Examples**
No examples provided.
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 1
- **Max Operands:** 3
- **Idempotent:** true