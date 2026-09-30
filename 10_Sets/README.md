# Sets — Python Problems 061–065

## 📌 Overview

This folder contains 5 Python problem-solving questions focused on Python Sets.

The purpose of this batch was to practice working with unique values, removing duplicates, comparing collections, and performing common set operations.

---

## 🎯 Learning Objectives

After completing these problems, I practiced:

* Creating sets
* Removing duplicate values
* Set membership
* Set intersection
* Set union
* Set difference
* Finding common elements
* Converting lists into sets
* Working with unique collections

---

## 📚 Problems

| #   | Problem                       | Main Concept     | Status |
| --- | ----------------------------- | ---------------- | ------ |
| 061 | Unique Values                 | Set + Duplicates | ✅      |
| 062 | Set Intersection              | Intersection     | ✅      |
| 063 | Set Union                     | Union            | ✅      |
| 064 | Set Difference                | Difference       | ✅      |
| 065 | Common Elements Between Lists | Sets + Lists     | ✅      |

---

## 🧠 Key Concepts Learned

### 1. Sets

A set is an unordered collection of unique elements.

```python
numbers = {1, 2, 3, 4}
```

A set automatically removes duplicate values.

---

### 2. Removing Duplicates

Converting a list into a set can be used to remove duplicate values.

```python
numbers = [1, 2, 2, 3, 3, 4]

unique_numbers = set(numbers)
```

The result contains only unique values.

---

### 3. Intersection

Intersection finds elements that exist in both sets.

```text
Set A ∩ Set B
```

Example:

```text
{1, 2, 3} ∩ {2, 3, 4}
        ↓
     {2, 3}
```

---

### 4. Union

Union combines the unique elements from both sets.

```text
Set A ∪ Set B
```

Example:

```text
{1, 2, 3} ∪ {3, 4, 5}
        ↓
   {1, 2, 3, 4, 5}
```

---

### 5. Difference

Difference finds elements that exist in the first set but not in the second set.

```text
Set A - Set B
```

Example:

```text
{1, 2, 3, 4} - {3, 4, 5}
        ↓
      {1, 2}
```

---

## 🧠 Problem-Solving Skills Practiced

This batch helped practice:

* Identifying duplicate data
* Working with unique values
* Comparing collections
* Finding common values
* Combining collections
* Finding values that exist in one collection but not another
* Choosing an appropriate Python data structure

---

## 🧪 Testing

Important test cases included:

```text
Duplicate values
No duplicate values
Completely different sets
Identical sets
Partially overlapping sets
Empty sets
Lists containing repeated values
```

---

## 📊 Batch Progress

**Problems Completed:** 5/5

**Overall Challenge Progress:** 65/100

```text
█████████████░░░░░░░ 65%
```

---

## 📁 Files

```text
10_Sets/
│
├── 061_unique_values.py
├── 062_set_intersection.py
├── 063_set_union.py
├── 064_set_difference.py
├── 065_common_elements.py
└── README.md
```

---

## 🚀 Next Step

The next topic is **Dictionaries**.

The focus will be on key-value data, accessing values, updating data, searching, and processing dictionary information.
