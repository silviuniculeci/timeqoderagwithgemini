---
input_types:
- Collection<Any>
- Collection<Any>
- Expression
- Expression
- Expression
output_type: Collection<Any>
purpose:
- Collection Manipulation
- Data Transformation
---
# Operator: Match
---
### **Description**
Matches the elements from first collection in the second collection based on the specified rule and evaluates an expression for every matched element. The operator returns the values produced by the matched expression.
If an unmatched expression is provided the operator returns also the values produces by the unmatched expression.
If the match expression is an equality expression then the matching process is optimized otherwise.
---
### **Syntax**
```
: Match(<first collection> In <local param>, <second collection> In <local param>, <matching expression>, <expression for matched elements>, [<expression for unmatched elements>])
```
---
### **Examples**
```
. Match(Products In @product, ProductCategories In @category, @product.productCategoryId = @category.id, @product.vat := @category.vat)
```
**Result:** `the collection of products with updated VAT`
---
### **Technical Details**
- **Type:** Function
- **Min Operands:** 4
- **Max Operands:** 5
- **Idempotent:** false