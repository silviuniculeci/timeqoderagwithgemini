---
input_types:
- EntityType
- String
- String
output_type: Any
purpose:
- Data Access
- Data Transformation
---
# Operator: ReadJson
---
### **Description**
Reads an entity or a list of entities from a json
---
### **Syntax**
```
: ReadJson(<entity type>, <source json>, [<JSON path>])
ex1. ReadJson(Country, '{code: "UK", name: "United Kingdom"}')
ex2. ReadJson(Address, '{legalAddress: {street: "Some street", city: "London"} }', '$.legalAddress')
ex3. ReadJson(Null, '{name: "legal address", address: {street: "Some street", city: "London"} }', '$.address.city')
```
---
### **Examples**
No examples provided.
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 2
- **Max Operands:** 3
- **Idempotent:** false