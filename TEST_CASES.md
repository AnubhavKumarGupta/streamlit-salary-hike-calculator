# Test Cases & Examples

## 🧪 Testing Your Salary Hike Calculator

---

## ✅ Valid Test Cases

### Test Case 1: Standard Positive Hike (20%)
**Input:**
- Old Salary: ₹50,000.00
- New Salary: ₹60,000.00

**Expected Output:**
- Hike Percentage: +20.00%
- Difference: ₹+10,000.00
- Message: "👍 Great! That's a good increment!"
- Color: Green

---

### Test Case 2: Excellent Hike (25%)
**Input:**
- Old Salary: ₹100,000.00
- New Salary: ₹125,000.00

**Expected Output:**
- Hike Percentage: +25.00%
- Difference: ₹+25,000.00
- Message: "🎉 Excellent! That's a fantastic hike!"
- Color: Green

---

### Test Case 3: Small Hike (5%)
**Input:**
- Old Salary: ₹80,000.00
- New Salary: ₹84,000.00

**Expected Output:**
- Hike Percentage: +5.00%
- Difference: ₹+4,000.00
- Message: "✨ That's a positive change!"
- Color: Green

---

### Test Case 4: Moderate Hike (15%)
**Input:**
- Old Salary: ₹200,000.00
- New Salary: ₹230,000.00

**Expected Output:**
- Hike Percentage: +15.00%
- Difference: ₹+30,000.00
- Message: "👍 Great! That's a good increment!"
- Color: Green

---

### Test Case 5: No Change (0%)
**Input:**
- Old Salary: ₹75,000.00
- New Salary: ₹75,000.00

**Expected Output:**
- Hike Percentage: 0.00%
- Difference: ₹0.00
- Message: "⏸️ No change in salary"
- Color: Yellow/Warning

---

### Test Case 6: Salary Reduction (-10%)
**Input:**
- Old Salary: ₹100,000.00
- New Salary: ₹90,000.00

**Expected Output:**
- Hike Percentage: -10.00%
- Difference: ₹-10,000.00
- Message: "⚠️ This is a salary reduction"
- Color: Red

---

### Test Case 7: Small Reduction (-2%)
**Input:**
- Old Salary: ₹50,000.00
- New Salary: ₹49,000.00

**Expected Output:**
- Hike Percentage: -2.00%
- Difference: ₹-1,000.00
- Message: "⚠️ This is a salary reduction"
- Color: Red

---

### Test Case 8: Large Numbers (Exceptional Hike 50%)
**Input:**
- Old Salary: ₹1,000,000.00
- New Salary: ₹1,500,000.00

**Expected Output:**
- Hike Percentage: +50.00%
- Difference: ₹+500,000.00
- Message: "🎉 Excellent! That's a fantastic hike!"
- Color: Green

---

### Test Case 9: Decimal Values
**Input:**
- Old Salary: ₹45,500.50
- New Salary: ₹52,325.75

**Expected Output:**
- Hike Percentage: +15.00%
- Difference: ₹+6,825.25
- Message: "👍 Great! That's a good increment!"
- Color: Green

---

### Test Case 10: Small Starting Salary
**Input:**
- Old Salary: ₹15,000.00
- New Salary: ₹18,000.00

**Expected Output:**
- Hike Percentage: +20.00%
- Difference: ₹+3,000.00
- Message: "👍 Great! That's a good increment!"
- Color: Green

---

## ❌ Error Cases (Should Show Error Messages)

### Error Case 1: Zero Old Salary
**Input:**
- Old Salary: ₹0.00
- New Salary: ₹50,000.00

**Expected Output:**
- Error Message: "⚠️ Old salary must be greater than 0!"
- No calculation performed

---

### Error Case 2: Negative Old Salary
**Input:**
- Old Salary: -₹10,000.00
- New Salary: ₹50,000.00

**Expected Output:**
- Error Message: "⚠️ Old salary must be greater than 0!"
- No calculation performed

---

### Error Case 3: Negative New Salary
**Input:**
- Old Salary: ₹50,000.00
- New Salary: -₹10,000.00

**Expected Output:**
- Error Message: "⚠️ New salary cannot be negative!"
- No calculation performed

---

## 📊 Real-World Scenarios

### Scenario 1: Fresher to 1 Year Experience
**Context:** First annual increment
**Input:**
- Old Salary: ₹25,000.00
- New Salary: ₹30,000.00

**Expected:**
- Hike: +20.00%
- Message: "👍 Great! That's a good increment!"

---

### Scenario 2: Mid-Level Promotion
**Context:** Promotion from developer to senior developer
**Input:**
- Old Salary: ₹60,000.00
- New Salary: ₹85,000.00

**Expected:**
- Hike: +41.67%
- Message: "🎉 Excellent! That's a fantastic hike!"

---

### Scenario 3: Company Switch
**Context:** Moving to better opportunity
**Input:**
- Old Salary: ₹75,000.00
- New Salary: ₹105,000.00

**Expected:**
- Hike: +40.00%
- Message: "🎉 Excellent! That's a fantastic hike!"

---

### Scenario 4: Annual Increment
**Context:** Standard yearly increment
**Input:**
- Old Salary: ₹90,000.00
- New Salary: ₹99,000.00

**Expected:**
- Hike: +10.00%
- Message: "✨ That's a positive change!"

---

### Scenario 5: Economic Downturn
**Context:** Company-wide salary reduction
**Input:**
- Old Salary: ₹100,000.00
- New Salary: ₹85,000.00

**Expected:**
- Hike: -15.00%
- Message: "⚠️ This is a salary reduction"

---

## 🎯 Edge Cases

### Edge Case 1: Very Small Hike (0.01%)
**Input:**
- Old Salary: ₹100,000.00
- New Salary: ₹100,010.00

**Expected:**
- Hike: +0.01%
- Message: "✨ That's a positive change!"

---

### Edge Case 2: Very Small Reduction (-0.01%)
**Input:**
- Old Salary: ₹100,000.00
- New Salary: ₹99,990.00

**Expected:**
- Hike: -0.01%
- Message: "⚠️ This is a salary reduction"

---

### Edge Case 3: Maximum JavaScript Number
**Input:**
- Old Salary: ₹999,999,999.00
- New Salary: ₹1,199,999,998.80

**Expected:**
- Hike: +20.00%
- Should handle large numbers correctly

---

### Edge Case 4: Many Decimal Places
**Input:**
- Old Salary: ₹50,123.4567
- New Salary: ₹60,148.1480

**Expected:**
- Hike: +20.00%
- Should round to 2 decimal places

---

## 🔬 Calculation Accuracy Tests

### Test 1: Precision Check
**Input:**
- Old Salary: ₹33,333.33
- New Salary: ₹44,444.44

**Calculation:**
- Difference: ₹11,111.11
- Percentage: (11111.11 / 33333.33) × 100 = 33.33%

**Expected:**
- Hike: +33.33%

---

### Test 2: Rounding Check
**Input:**
- Old Salary: ₹45,000.00
- New Salary: ₹52,000.00

**Calculation:**
- Difference: ₹7,000.00
- Percentage: (7000 / 45000) × 100 = 15.555...%

**Expected:**
- Hike: +15.56% (rounded to 2 decimals)

---

### Test 3: Negative Rounding
**Input:**
- Old Salary: ₹90,000.00
- New Salary: ₹85,555.00

**Calculation:**
- Difference: ₹-4,445.00
- Percentage: (-4445 / 90000) × 100 = -4.938...%

**Expected:**
- Hike: -4.94% (rounded to 2 decimals)

---

## 📋 Test Checklist

Use this checklist to verify all features:

### Basic Functionality
- [ ] App loads without errors
- [ ] Input fields accept numbers
- [ ] Default values display correctly (₹50,000 and ₹60,000)
- [ ] Calculate button is visible and clickable
- [ ] Results display after clicking button

### Calculation Accuracy
- [ ] Positive hike calculates correctly
- [ ] Negative hike calculates correctly
- [ ] Zero change displays 0.00%
- [ ] Decimal numbers handled properly
- [ ] Large numbers display correctly
- [ ] Percentage rounded to 2 decimals

### Error Handling
- [ ] Zero old salary shows error
- [ ] Negative old salary shows error
- [ ] Negative new salary shows error
- [ ] Errors prevent calculation
- [ ] Error messages are clear

### UI Elements
- [ ] Title displays with gradient
- [ ] Subtitle shows correctly
- [ ] Input labels visible (📊 Old Salary, 📈 New Salary)
- [ ] Button has hover effect
- [ ] Result card animates smoothly
- [ ] Breakdown card displays all info

### Color Coding
- [ ] Positive hike shows green
- [ ] Negative change shows red
- [ ] Zero change shows appropriate color
- [ ] Colors applied to all relevant fields

### Messages
- [ ] >20% shows "Excellent" message
- [ ] >10% shows "Great" message
- [ ] >0% shows "Positive" message
- [ ] 0% shows "No change" message
- [ ] <0% shows "Reduction" warning

### Real-time Features
- [ ] Preview updates when inputs change
- [ ] Preview shows before button click
- [ ] Preview matches final calculation

### Responsive Design
- [ ] Works on full screen
- [ ] Works on smaller windows
- [ ] Layout adjusts properly
- [ ] Text remains readable

### Performance
- [ ] App loads quickly
- [ ] Calculations instant
- [ ] No lag in input fields
- [ ] Animations smooth

---

## 🚀 Quick Test Script

Copy-paste these values to quickly test:

```
Test 1: 50000 → 60000 = +20.00%
Test 2: 100000 → 125000 = +25.00%
Test 3: 80000 → 84000 = +5.00%
Test 4: 75000 → 75000 = 0.00%
Test 5: 100000 → 90000 = -10.00%
Test 6: 0 → 50000 = ERROR
Test 7: 50000 → -10000 = ERROR
```

---

## ✅ All Tests Passed?

If all tests pass, your app is ready for:
- ✅ Production use
- ✅ EXE conversion
- ✅ Distribution to users
- ✅ Deployment to cloud

**Happy Testing! 🎉**
