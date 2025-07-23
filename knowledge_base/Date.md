---
input_types:
- Date
- Boolean
- Number
output_type: Date
purpose:
- Date & Time
---
# Operator: Date
---
### **Description**
Returns the current date
---
### **Syntax**
```
: Date([<date>] | [<is UTC time>] | [<year>, <month>, <day>])
ex1. Date() returns the current local date and time
ex2. Date(Date) removes the time from current local date
ex3. Date(ToDate('2000-12-31 20:15', 'yyyy-MM-dd hh:mm')) extract only the date and returns 31/12/2000
ex4. Date(2000, 12, 31) creates a new date from year, month, day and returns 31/12/2000
```
---
### **Examples**
No examples provided.
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 0
- **Max Operands:** 3
- **Idempotent:** false