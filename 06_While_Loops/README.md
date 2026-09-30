# While Loops — Python Problems 041–045

## 📌 Overview

This folder contains 5 Python problem-solving questions focused on the `while` loop.

The purpose of this batch was to practice repetition based on conditions, stopping loops at the correct time, processing digits, and creating repeated user-input logic.

---

## 🎯 Learning Objectives

After completing these problems, I practiced:

* `while` loops
* Loop conditions
* Updating loop variables
* Countdown logic
* Sentinel values
* Digit processing
* Number reversal
* Repeated user input
* Loop termination
* Condition-based repetition

---

## 📚 Problems

| #   | Problem            | Main Concept               | Status |
| --- | ------------------ | -------------------------- | ------ |
| 041 | Countdown          | `while` loop               | ✅      |
| 042 | Sum Until Zero     | Sentinel value             | ✅      |
| 043 | Digit Count        | Digit processing           | ✅      |
| 044 | Reverse Number     | `%` + `//` + `while`       | ✅      |
| 045 | Number Guess Check | Repeated input + condition | ✅      |

---

## 🧠 Key Concepts Learned

### 1. `while` Loop

A `while` loop repeats code as long as its condition remains true.

```python
while condition:
    # repeated code
```

The condition must eventually become false so that the loop can stop.

---

### 2. Loop Control

A `while` loop normally requires:

1. Starting value
2. Condition
3. Update

```text
Start
  ↓
Check condition
  ↓
Run code
  ↓
Update value
  ↓
Check again
```

---

### 3. Sentinel Value

A sentinel value is a special value that tells the program to stop receiving input.

In Problem 042, `0` was used as the stopping value.

```text
Input → Input → Input → 0
                         ↓
                       Stop
```

---

### 4. Digit Processing

Problems 043 and 044 practiced processing numbers digit by digit.

Important operators:

```text
%   → remainder
//  → floor division
```

These operators can be combined with a loop to work through the digits of a number.

---

### 5. Loop Termination

A major part of using `while` loops is knowing **when the loop should stop**.

For example, in the guessing problem, the loop continues until the correct number is entered.

---

## 🧠 Problem-Solving Skills Practiced

This batch helped practice:

* Thinking about loop conditions
* Controlling when a loop starts and stops
* Updating variables correctly
* Processing numbers step by step
* Handling repeated user input
* Using special stopping conditions
* Avoiding infinite loops

---

## 🧪 Testing

Important test cases included:

```text
1
5
10
0
Single-digit numbers
Multiple-digit numbers
Numbers ending in 0
Correct guess
Incorrect guesses
```

---

## 📊 Batch Progress

**Problems Completed:** 5/5

**Overall Challenge Progress:** 45/100

```text
█████████░░░░░░░░░░░ 45%
```

---

## 📁 Files

```text
06_While_Loops/
│
├── 041_countdown.py
├── 042_sum_until_zero.py
├── 043_digit_count.py
├── 044_reverse_number.py
├── 045_number_guess_check.py
└── README.md
```

---

## 🚀 Next Step

The next topic is **Nested Loops / Patterns**.

The focus will be on understanding one loop inside another loop and using loops to generate structured output.
