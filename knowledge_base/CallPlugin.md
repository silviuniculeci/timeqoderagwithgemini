---
input_types:
- Number
- String
- Collection<Any>
- Boolean
output_type: Any
purpose:
- Plugin & Integration
---
# Operator: CallPlugin
---
### **Description**
Calls a plugin by id
---
### **Syntax**
```
: CallPlugin(<plugin id / identifier>, [<output index / collection of inputs>], [<true - override all inputs, false - override only not null inputs, default is false>], [<output index>])
ex1. CallPlugin(10) returns the entire output of the plugin with id 10
ex2. CallPlugin(getUserInfo, ["name"]) calls plugin with identifier 'getUserInfo', passes the value "name" for the first input and returns the output
ex3. CallPlugin(10, [Date], true, 0) calls plugin with id 10, passes the current date for the first input and returns the first output
```
---
### **Examples**
No examples provided.
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 1
- **Max Operands:** 4
- **Idempotent:** false