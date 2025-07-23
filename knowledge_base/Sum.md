---
input_types:
- Collection<Number>
- Number
output_type: Number
purpose:
- Aggregation
- Mathematical
---
# Operator: Sum
---
### **Description**
Returns the sum of input operands
---
### **Syntax**
```
Sum(<collection of values 1>, [<collection of values 2>], ...)
```
```
Sum(<value 1>, [<value 2>], ...)
```
---
### **Examples**
```
. 1: Sum([1, 3, 2])
```
**Result:** `6`
```
. 2: Sum(1, 5, 2)
```
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 1
- **Max Operands:** 65535
- **Idempotent:** true