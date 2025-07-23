---
input_types:
- Boolean
- String
- String
- String
output_type: Collection<Collection<String>>
purpose:
- Data Transformation
- String Manipulation
---
# Operator: TableCsv
---
### **Description**
Returns a matrix from a string containing row with values separated by a specific character
---
### **Syntax**
```
: TableCsv(<HasHeader>, <column separator>, <row separator>, <string table>)
```
---
### **Examples**
```
. TableCsv(True, ",", Chr(13), "id,name
1,item 1
2, item 2") will return a matrix with two rows and two columns
```
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 4
- **Max Operands:** 4
- **Idempotent:** true