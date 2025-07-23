---
input_types:
- Collection<Expression>
- Collection<Collection<Any>>
output_type: Any
purpose:
- Data Access
---
# Operator: MultiLookUp
---
### **Description**
Determines an element in a multidimensional object
all operands excepting the last represent the conditions for each dimension
the last operand represent the multidimensional object containing the values
---
### **Syntax**
Not specified.
---
### **Examples**
```
. MultiLookUp([paramX > 3, paramX <= 3], [paramY <= 5,paramY > 5], [[0, 1], [2, 3]])
```
**Result:** `3 if X <= 3 and Y > 5`
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 2
- **Max Operands:** 65535
- **Idempotent:** true