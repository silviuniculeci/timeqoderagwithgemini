---
input_types:
- String
- Any
- Number
- Boolean
- Number
output_type: Any
purpose:
- Utility
---
# Operator: Cache
---
### **Description**
Retrieves a cached value (second operand) based on a key (first operand)
---
### **Syntax**
```
: Cache(<key>, <object to cache>, [<cache type: 0 - module (default), 1 - session, 2 - request, 3 - domain, 4 - global, 5 - localOnDomain, 6 - localOnModule>], [<refresh cache (default false)>], [<module/domain/global cache expiration in minutes (default is 4 hours)>])
```
---
### **Examples**
```
Cache("key", [1, 2])
```
**Result:** `an array with two integers but it only evaluates it the first time,
the second time is returned from cache`
```
Cache("currentDate", Date, global)
```
**Result:** `the current date and time but and stores it in global cache for 4 hours,
so calling it before 4 hours will return the same value obtained the first time it was called and calling it after 4 hours will obtain a new date time`
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 2
- **Max Operands:** 5
- **Idempotent:** false