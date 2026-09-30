# Input & Output — Python Problems 001–010

This section contains the first 10 problems of my **Python 200 Problem-Solving Challenge**.

The goal of this section is to practice basic Python input, output, variables, type conversion, arithmetic operations, and simple problem-solving.

---

## 🎯 Learning Objectives

By completing these problems, I practiced:

* Taking input from users
* Displaying output using `print()`
* Storing values in variables
* Converting data types using `int()` and `str()`
* Performing basic arithmetic operations
* Applying mathematical formulas
* Understanding `%` and `//`
* Solving simple real-world problems
* Writing and testing Python programs

---

## 📚 Problems

| #   | Problem                  | Difficulty | Main Concepts                   | Status |
| --- | ------------------------ | ---------- | ------------------------------- | ------ |
| 001 | Sum Two Numbers          | Easy       | Input, Variables, Addition      | ✅      |
| 002 | Sum Three Numbers        | Easy       | Multiple Inputs, Addition       | ✅      |
| 003 | Personal Information     | Easy       | Strings, Input, Type Conversion | ✅      |
| 004 | Rectangle Area           | Easy       | Input, Multiplication, Formula  | ✅      |
| 005 | Rectangle Perimeter      | Easy       | Formula, Arithmetic             | ✅      |
| 006 | Average of Three Numbers | Easy       | Addition, Division              | ✅      |
| 007 | Celsius to Fahrenheit    | Easy       | Formula, Arithmetic             | ✅      |
| 008 | Simple Shopping Bill     | Easy       | Multiplication, Input           | ✅      |
| 009 | Swap Two Numbers         | Medium     | Multiple Assignment             | ✅      |
| 010 | Sum of Digits            | Medium     | `//`, `%`, Digit Extraction     | ✅      |

---

## 🧠 Problem Details

### 001 — Sum Two Numbers

**Concepts:** `input()`, variables, `int()`, addition, `print()`

Take two numbers from the user and print their sum.

**Key Learning:** How to receive numerical input and perform addition.

---

### 002 — Sum Three Numbers

**Concepts:** Multiple inputs, variables, arithmetic

Take three numbers from the user and calculate their total.

**Key Learning:** Applying the same logic to multiple values.

---

### 003 — Personal Information

**Concepts:** Strings, integers, input, type conversion

Take the user's name, age, and address and display them in a meaningful sentence.

**Key Learning:** Working with different data types and combining values in output.

---

### 004 — Rectangle Area

**Concepts:** Input, multiplication, mathematical formula

Calculate the area of a rectangle using:

`Area = Length × Width`

**Key Learning:** Converting a mathematical formula into Python code.

---

### 005 — Rectangle Perimeter

**Concepts:** Input, arithmetic, formula

Calculate the perimeter of a rectangle using:

`Perimeter = 2 × (Length + Width)`

**Key Learning:** Using parentheses and arithmetic operators correctly.

---

### 006 — Average of Three Numbers

**Concepts:** Addition, division, variables

Calculate the average of three numbers using:

`Average = (a + b + c) / 3`

**Key Learning:** Translating an average formula into code.

---

### 007 — Celsius to Fahrenheit

**Concepts:** Input, variables, arithmetic, formula

Convert a temperature from Celsius to Fahrenheit using:

`F = (C × 9/5) + 32`

**Key Learning:** Implementing a conversion formula.

---

### 008 — Simple Shopping Bill

**Concepts:** Input, multiplication, variables

Calculate the total bill using:

`Total = Price × Quantity`

**Key Learning:** Applying arithmetic to a real-world problem.

---

### 009 — Swap Two Numbers

**Concepts:** Variables, multiple assignment

Swap the values of two variables.

Example:

`a = 10, b = 20`

After swapping:

`a = 20, b = 10`

**Key Learning:** Understanding Python multiple assignment.

---

### 010 — Sum of Digits

**Concepts:** Integer division, modulo, digit extraction

Find the sum of the digits of a three-digit number.

Example:

`345 → 3 + 4 + 5 = 12`

**Key Learning:** Using `//` and `%` to extract individual digits.

---

## 🔍 Common Learning Points

### 1. `input()` returns a string

For numerical calculations, conversion is usually required:

```python
number = int(input())
```

### 2. Variable naming matters

Instead of:

```python
a = 10
b = 20
c = a + b
```

more descriptive names can improve readability:

```python
first_number = 10
second_number = 20
total = first_number + second_number
```

### 3. `//` vs `/`

`/` performs normal division and returns a division result.

`//` performs floor division.

### 4. `%` gives the remainder

For example:

```python
17 % 5
```

gives:

```text
2
```

---

## 📝 Mistakes & Improvements

### Problem 009

The swapping logic was correct using:

```python
a, b = b, a
```

However, the original solution did not display the values **before swapping**.

**Lesson:** Always check the complete output requirement, not only the main calculation.

---

## 📊 Batch Result

**Problems Completed:** 10 / 10

**Main Skills Practiced:**

* Input / Output
* Variables
* Type Conversion
* Arithmetic Operators
* Mathematical Formulas
* Basic Problem Solving
* Digit Extraction
* Python Multiple Assignment

---

## 🚀 Next Step

The next batch will focus on **Operators and Arithmetic Logic** with more varied problem styles and gradually increasing difficulty.

**Progress: 10 / 200**
