# For Loops — Python Problems 036–040

## 📌 Overview

This folder contains 5 Python problem-solving questions focused on the `for` loop.

The purpose of this batch was to practice repetition, counting, accumulation, and repeated calculations.

---

## 🎯 Learning Objectives

After completing these problems, I practiced:

* `for` loops
* `range()`
* Repeating operations
* Counting values
* Calculating sums
* Multiplication tables
* Even number identification
* Factorial calculation
* Using a variable to accumulate results

---

## 📚 Problems

| #   | Problem              | Main Concept       | Status |
| --- | -------------------- | ------------------ | ------ |
| 036 | Print Numbers        | `for` + `range()`  | ✅      |
| 037 | Sum of Numbers       | Loop + Accumulator | ✅      |
| 038 | Multiplication Table | Loop + Calculation | ✅      |
| 039 | Count Even Numbers   | Loop + Condition   | ✅      |
| 040 | Factorial            | Loop + Accumulator | ✅      |

---

## 🧠 Key Concepts Learned

### 1. `for` Loop

A `for` loop is used when we want to repeat an operation for a sequence or range of values.

```python
for i in range(1, 6):
    print(i)
```

Output:

```text
1
2
3
4
5
```

---

### 2. `range()`

`range()` generates a sequence of numbers that can be used with loops.

```python
range(1, 6)
```

produces:

```text
1, 2, 3, 4, 5
```

The ending value is not included.

---

### 3. Accumulator

An accumulator stores a continuously updated result.

For example, while calculating a sum:

```text
Start
  ↓
0
  ↓
Add next number
  ↓
Update total
  ↓
Repeat
```

This pattern is useful in many problem-solving tasks.

---

### 4. Loop + Condition

A loop can be combined with a condition to process only specific values.

For example:

```text
1 → check
2 → check
3 → check
4 → check
...
```

This idea was used when counting even numbers.

---

### 5. Factorial

Factorial is another example of repeated multiplication.

For example:

```text
5! = 5 × 4 × 3 × 2 × 1
```

The problem demonstrates how a loop can repeatedly update a result.

---

## 🧠 Problem-Solving Skills Practiced

This batch helped practice:

* Understanding repetition
* Choosing an appropriate range
* Tracking a running result
* Combining loops with conditions
* Converting mathematical processes into code
* Testing different input values

---

## 🧪 Testing

Important test cases included:

```text
1
2
5
10
0
```

Special cases such as `0` were especially important for the factorial problem.

---

## 📊 Batch Progress

**Problems Completed:** 5/5

**Overall Challenge Progress:** 40/100

```text
████████░░░░░░░░░░░░ 40%
```

---

## 📁 Files

```text
05_For_Loops/
│
├── 036_print_numbers.py
├── 037_sum_numbers.py
├── 038_multiplication_table.py
├── 039_count_even_numbers.py
├── 040_factorial.py
└── README.md
```

---

## 🚀 Next Step

The next topic is **While Loops**.

The focus will be on repetition where the number of iterations depends on a condition.
