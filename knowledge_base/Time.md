---
input_types:
- Date
output_type: Date
purpose:
- Date & Time
- Utility
---
# Operator: Time
---
### **Description**
Returns the time component of a date
---
### **Syntax**
```
: Time([<date>])
ex1. Time() returns the current local time
ex2. Time(ToDate('2000-12-31 20:15', 'yyyy-MM-dd hh:mm')) returns the time from the input date
```
---
### **Examples**
No examples provided.
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 0
- **Max Operands:** 1
- **Idempotent:** false