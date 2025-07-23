---
input_types:
- EntityType
- Expression
- Collection<Any>
- String
output_type: String
purpose:
- Data Access
---
# Operator: BuildCustomQuery
---
### **Description**
Generates an SQL clause from a filtering expression and updates the given collection for the query parameters.
---
### **Syntax**
```
: BuildCustomQuery(<entity type>, <filter expression>, <parameters collection>, [<table alias>])
ex1. BuildCustomQuery(Clients, email = InstanceInfo.CurrentUserEmail, @paramaters) returns the text "[email] = @0" and adds the parameter @0 with its value to the @parameters collection
ex2. BuildCustomQuery(Products, InList(typeId, StaticArray(1, 2, 5)) And price >= 500, @paramaters) returns the text "([typeId] IN (@0,@1,@2)) AND (([price] >= @3))" and adds the parameters
```
---
### **Examples**
No examples provided.
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 3
- **Max Operands:** 4
- **Idempotent:** false