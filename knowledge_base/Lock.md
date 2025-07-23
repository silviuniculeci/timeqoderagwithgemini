---
input_types:
- Any
- Expression
- Boolean
output_type: Any
purpose:
- Control Flow
---
# Operator: Lock
---
### **Description**
Assures that the subexpression is executed one at a time
---
### **Syntax**
```
: Lock(<locking key>, <subexpression to evaluate inside lock>, [<use global lock - default is false meaning that a domain level lock is used>])
```
---
### **Examples**
```
. Lock(Project.id, (Project.count := Project.count + 1, SaveEntity(Project))) assures that the incrementation of Project.count and its update in database is performed only one at a time
```
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 2
- **Max Operands:** 3
- **Idempotent:** true