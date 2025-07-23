---
input_types:
- Number
output_type: Any
purpose:
- Collection Manipulation
---
# Operator: CurrentValue
---
### **Description**
Returns current value inside an iteration operator
---
### **Syntax**
```
: CurrentValue([<nesting level (default is 0)>])
```
---
### **Examples**
```
. Iterate(["A", "B"],ToStr(CurrentIndex) + "-" + CurrentValue)
```
**Result:** `the array of strings ["0-A","1-B"]`
```
. Iterate(Table(2, [2, 2, 3, 1]), Iterate(CurrentValue, ToDbl(CurrentValue) * 100 / Sum(CurrentValue(1))))
```
**Result:** `the matrix [[50, 50], [75, 25]]`
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 0
- **Max Operands:** 1
- **Idempotent:** false