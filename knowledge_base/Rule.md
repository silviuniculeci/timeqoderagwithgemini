---
input_types:
- Any
- Collection
output_type: Any
purpose:
- Control Flow
---
# Operator: Rule
---
### **Description**
Evaluates a rule; Accepts input parameters to be passed either as 'parameter := value' associations or as <parameter, value> pairs
---
### **Syntax**
```
Rule(<id / identifier>, [<input parameter1> := <value1>], [<input parameter2> := <value2>], ...)
```
```
Rule(<id / identifier>, [<input parameter1>, <value1>], [<input parameter2>, <value2>], ...)
```
---
### **Examples**
```
Rule(10) evaluates the rule with id 10 and
```
**Result:** `it's result`
```
Rule(addTwoNumbers, @first := 2, @second := 3) evaluates the rule with identifier 'addNumbers' and passes the input parameters @first and @second with values 2 and 3
```
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 1
- **Max Operands:** 1024
- **Idempotent:** false