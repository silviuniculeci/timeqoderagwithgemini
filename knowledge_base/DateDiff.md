---
input_types:
- Date
- String
output_type: Number
purpose:
- Date & Time
---
# Operator: DateDiff
---
### **Description**
Returns the difference between two dates in requested date part
---
### **Syntax**
```
: DateDiff(<date to substract from>, <date to substract>, <date part>)
Date partings: year, month, day, hour, minute, second, time, workingHour, workingDay
```
---
### **Examples**
```
. DateDiff(Date, ToDate("2009-01-01"), day)
```
**Result:** `the number of days passed from 2009-01-01`
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 3
- **Max Operands:** 3
- **Idempotent:** true