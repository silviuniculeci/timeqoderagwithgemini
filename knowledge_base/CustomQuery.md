---
input_types:
- String
- Any
output_type: Expression
purpose:
- Data Access
- Entity Manipulation
---
# Operator: CustomQuery
---
### **Description**
Generates a custom SQL clause to be used in filtering read entities from database. It can be used inside the operators 'ReadEntity', 'ReadEntities', 'UpdateEntity', 'DeleteEntity', 'CountEntities', and 'ExistsEntity'
---
### **Syntax**
```
: CustomQuery(<query string>, [<input parameter1> := <value1>], [<input parameter2> := <value2>], ...)
```
---
### **Examples**
```
: ReadEntities(Orders, CustomQuery("total > @amount", @amount := 100))
```
**Result:** `all the orders from the database with the total greater than 100`
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 1
- **Max Operands:** 1024
- **Idempotent:** false