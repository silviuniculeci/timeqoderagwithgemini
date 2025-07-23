---
input_types:
- Any
- Collection
- Collection
output_type: Any
purpose:
- Collection Manipulation
- Data Access
---
# Operator: Lookup
---
### **Description**
Searches a value in a collection of keys and returns the corresponding value (correspondence is based on position)
---
### **Syntax**
```
: Lookup(<value to find>, <collection of keys / map>, [<collection of values>])
```
---
### **Examples**
```
1. Lookup(1, [5, 2, 1], ["v5","v2","v1"])
```
**Result:** `"v1"`
```
2. Lookup(1, Map([Create(Roles, id := 0, name := 'Anonymous'), Create(Roles, id := 1, name := 'Administrator')], id, name))
```
**Result:** `"Administrator"`
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 2
- **Max Operands:** 3
- **Idempotent:** true