---
input_types:
- Any
output_type: Any
purpose:
- Data Access
- Utility
---
# Operator: KnownEntity
---
### **Description**
Returns the id / identifier of a rule, the name of an entity or the id of a plugin in order to reference (load) it for current module
ex1: KnownEntity(Rule(10)) returns 10
ex2: KnownEntity(Orders) returns "Orders"
ex3: KnownEntity(CallPlugin(SendEmail)) returns "SendEmail"
---
### **Syntax**
Not specified.
---
### **Examples**
No examples provided.
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 1
- **Max Operands:** 1
- **Idempotent:** false