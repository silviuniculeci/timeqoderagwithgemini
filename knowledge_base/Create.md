---
input_types:
- EntityType
- Any
- String
- Number
output_type: Entity
purpose:
- Entity Manipulation
---
# Operator: Create
---
### **Description**
Creates an entity value from an array
---
### **Syntax**
```
Create(<entity type>, [<member 1> := <value 1>] / [<entity value 1>], [<member 2> := <value 2>] / [<entity value 2>], ...)
```
```
Create(<entity type>, <entity value>, [<max level - default is 16>])
```
```
Create(<entity type>, [<list of values to be assigned to members>], [<member 1>], [<member 2>], ...)
```
---
### **Examples**
```
1. Create(OptionsType, Id := 1, Description := "Option 1")
```
```
2. Create(OptionsType, sourceOptions, 2)
```
```
3. Create(OptionsType, [1, "Option 1"], Id, Description)
```
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 1
- **Max Operands:** 2147483647
- **Idempotent:** false