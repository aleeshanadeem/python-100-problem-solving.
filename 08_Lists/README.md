# Lists — Python Problems 051–055

## 📌 Overview

This folder contains 5 Python problem-solving questions focused on Python Lists.

The purpose of this batch was to practice storing multiple values, accessing list elements, processing list data, finding values, counting elements, reversing data, and handling duplicates.

---

## 🎯 Learning Objectives

After completing these problems, I practiced:

* Creating and working with lists
* Iterating through list elements
* Calculating a list sum
* Finding the largest element
* Counting specific elements
* Reversing a list
* Removing duplicate values
* Maintaining original element order
* Combining lists with conditions and loops

---

## 📚 Problems

| #   | Problem              | Main Concept       | Status |
| --- | -------------------- | ------------------ | ------ |
| 051 | List Sum             | Loop + Accumulator | ✅      |
| 052 | Largest List Element | Comparison + Loop  | ✅      |
| 053 | Count Even Numbers   | Loop + Condition   | ✅      |
| 054 | Reverse List         | List + Indexing    | ✅      |
| 055 | Remove Duplicates    | List + Membership  | ✅      |

---

## 🧠 Key Concepts Learned

### 1. Creating a List

A list can store multiple values.

```python
numbers = [10, 20, 30, 40]
```

---

### 2. Accessing List Elements

Lists use zero-based indexing.

```python
numbers = [10, 20, 30]

print(numbers[0])
```

Output:

```text
10
```

---

### 3. Iterating Through a List

A `for` loop can be used to process each element.

```python
for number in numbers:
    print(number)
```

---

### 4. Accumulator with Lists

A variable can be used to maintain a running total.

```text
Start
  ↓
Read element
  ↓
Add to total
  ↓
Read next element
  ↓
Repeat
```

This pattern was used in the list-sum problem.

---

### 5. Searching and Comparing Elements

List elements can be compared one by one to find a required value, such as the largest element.

---

### 6. Removing Duplicates

Duplicate values can be identified while processing a list.

An important requirement in this problem was to maintain the **original order** of the elements.

Example:

```text
[1, 2, 2, 3, 4, 4]
       ↓
[1, 2, 3, 4]
```

---

## 🧠 Problem-Solving Skills Practiced

This batch helped practice:

* Processing collections of data
* Iterating through multiple values
* Maintaining a running result
* Comparing elements
* Counting elements based on conditions
* Building a new list from existing data
* Thinking about duplicate values
* Preserving data order

---

## 🧪 Testing

Important test cases included:

```text
Empty list
Single-element list
All even numbers
No even numbers
Repeated values
Already unique values
Negative numbers
```

---

## 📊 Batch Progress

**Problems Completed:** 5/5

**Overall Challenge Progress:** 55/100

```text
███████████░░░░░░░░░ 55%
```

---

## 📁 Files

```text
08_Lists/
│
├── 051_list_sum.py
├── 052_largest_list_element.py
├── 053_count_even_numbers.py
├── 054_reverse_list.py
├── 055_remove_duplicates.py
└── README.md
```

---

## 🚀 Next Step

The next topic is **Tuples**.

The focus will be on understanding tuple creation, accessing tuple data, unpacking, searching, and working with immutable collections.
