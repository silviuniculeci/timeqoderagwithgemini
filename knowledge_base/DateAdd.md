---
input_types:
- Date
- Number
- String
output_type: Date
purpose:
- Date & Time
---
# Operator: DateAdd
---
### **Description**
Adds a date part to the date passed as the first operand
---
### **Syntax**
```
: DateAdd(<date>, <increment>, <date part>)
Date partings: year, month, day, hour, minute, second, time, workingHour, workingDay
```
---
### **Examples**
```
. DateAdd(Date, 1, day)
```
**Result:** `the next day`
```
. DateAdd(Date(2000, 12, 31), Date, time) adds the current time of day to the date 2000/12/31
```
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 3
- **Max Operands:** 3
- **Idempotent:** true