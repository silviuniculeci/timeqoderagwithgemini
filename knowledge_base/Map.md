---
input_types:
- Collection
- Expression
- Expression
output_type: Collection<Any>
purpose:
- Collection Manipulation
- Data Transformation
---
# Operator: Map
---
### **Description**
Creates a map from a collection using the second operand as the key and the third operand as the value
Syntax1: Map(<collection>, <key expression>, [<value expression - default is CurrentValue>])
Syntax2: Map() creates an empty map that can be used later to add items using the AddItem operator
ex1. Map([1, 3, 5], CurrentValue, "Value" + CurrentValue) returns a map with the values 1, 3 and 5 and associated values "Value 1", "Value 3", "Value 5"
ex2. Map([Create(Roles, id := 0, name := 'Anonymous'), Create(Roles, id := 1, name := 'Administrator')], id, name) creates a map with the ids of the roles from input collection and the names of the roles as corresponding values
---
### **Syntax**
Not specified.
---
### **Examples**
No examples provided.
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 0
- **Max Operands:** 3
- **Idempotent:** false