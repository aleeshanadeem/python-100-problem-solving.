# Tuples — Python Problems 056–060

## 📌 Overview

This folder contains 5 Python problem-solving questions focused on Python Tuples.

The purpose of this batch was to understand tuple creation, indexing, iteration, searching, unpacking, and working with immutable collections.

---

## 🎯 Learning Objectives

After completing these problems, I practiced:

* Creating tuples
* Accessing tuple elements
* Using tuple indexing
* Iterating through tuples
* Calculating tuple values
* Finding values without relying on built-in functions
* Tuple unpacking
* Searching for values
* Understanding immutable collections

---

## 📚 Problems

| #   | Problem               | Main Concept        | Status |
| --- | --------------------- | ------------------- | ------ |
| 056 | Tuple Access          | Indexing            | ✅      |
| 057 | Tuple Sum             | Loop + Accumulator  | ✅      |
| 058 | Largest Tuple Element | Comparison + Loop   | ✅      |
| 059 | Tuple Unpacking       | Unpacking           | ✅      |
| 060 | Search in Tuple       | Membership + Search | ✅      |

---

## 🧠 Key Concepts Learned

### 1. Creating a Tuple

A tuple can store multiple values.

```python
numbers = (10, 20, 30, 40)
```

Tuples are ordered collections.

---

### 2. Tuple Indexing

Tuples use zero-based indexing.

```python
numbers = (10, 20, 30)

print(numbers[0])
```

Output:

```text
10
```

---

### 3. Tuple Iteration

A `for` loop can be used to process each tuple element.

```python
for number in numbers:
    print(number)
```

---

### 4. Tuple Unpacking

Tuple values can be assigned to separate variables.

```python
person = ("Ali", 20, "Lahore")

name, age, city = person
```

Now each value can be accessed through its corresponding variable.

---

### 5. Searching in a Tuple

A value can be checked against the values stored in a tuple.

The result can be used to make a decision:

```text
Value exists → Found
Value does not exist → Not Found
```

---

## 🔒 Immutability

One important characteristic of tuples is that they are **immutable**.

This means that after a tuple is created, its individual elements cannot normally be changed.

Example:

```python
numbers = (10, 20, 30)
```

The tuple can be accessed and processed, but its existing elements cannot simply be modified like list elements.

---

## 🧠 Problem-Solving Skills Practiced

This batch helped practice:

* Working with ordered collections
* Accessing data using indexes
* Processing collection elements
* Maintaining running results
* Comparing values
* Searching for specific values
* Unpacking structured data
* Understanding the difference between mutable and immutable collections

---

## 🧪 Testing

Important test cases included:

```text
First index
Last index
Single-element tuple
Positive numbers
Negative numbers
Existing search value
Non-existing search value
Different tuple sizes
```

---

## 📊 Batch Progress

**Problems Completed:** 5/5

**Overall Challenge Progress:** 60/100

```text
████████████░░░░░░░░ 60%
```

---

## 📁 Files

```text
09_Tuples/
│
├── 056_tuple_access.py
├── 057_tuple_sum.py
├── 058_tuple_maximum.py
├── 059_tuple_unpacking.py
├── 060_tuple_search.py
└── README.md
```

---

## 🚀 Next Step

The next topic is **Sets**.

The focus will be on unique values, set operations, membership checking, and removing duplicate data.
