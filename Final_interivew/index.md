# Group Anagrams (LeetCode 49)

## Description

Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

Two strings are anagrams if they contain the same characters with the same frequency, but possibly in a different order.

### Examples

```python
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["eat","tea","ate"],["tan","nat"],["bat"]]

Input: strs = [""]
Output: [[""]]

Input: strs = ["a"]
Output: [["a"]]
```

## Reference

This problem is adapted from [LeetCode Problem 49 - Group Anagrams](https://leetcode.com/problems/group-anagrams/), which is a commonly asked question in technical interviews at companies like Amazon, Google, and Facebook.

## Hints

* How can you represent a word in a way that two anagrams produce the same representation?
* Can you use a hash map to group words by that representation?
* Try sorting the characters in each word.
* Alternatively, use a fixed-size array of character counts as the key.

## Solution 1: Sort-based grouping

### Step 1: Define the problem structure

We want to group words such that all anagrams appear together. For that, we need to identify a key that is the same for all anagrams.

### Step 2: Canonical representation

Sort the characters of each word in alphabetical order. For example, both "eat" and "tea" become "aet". This sorted string will be our dictionary key.

### Step 3: Hash map grouping

Create a dictionary (hash map) where:

* The **key** is the sorted string;
* The **value** is a list of words that match this sorted string.

Iterate over all strings in the input list, sort them, and append them to the dictionary.

### Step 4: Collect results

The final result is the list of values from the dictionary.

## Solution 2: Character-count-based grouping (more efficient)

### Step 1: Understand limitations of sorting

Sorting takes O(k log k), where `k` is the length of each word. If we want to optimize this, we can use the frequency of each letter instead of sorting.

### Step 2: Frequency as key

Create a fixed-size list of 26 integers (one for each letter a-z). This represents how many times each character appears in the word. Convert this list to a tuple and use it as the key in your dictionary.

For example, "bat" becomes (1, 0, 0, ..., 1, ..., 1) where 'a', 'b', and 't' are marked.

### Step 3: Group by count-tuple

Again, use a dictionary where:

* The **key** is the character count tuple;
* The **value** is the list of words that match that signature.

This avoids sorting and improves performance, especially for longer strings.

### Step 4: Collect results

Return the values of the dictionary.

## Time and Space Complexity

### Sorting-based approach

* **Time Complexity**: O(n \* k log k), where `n` is the number of strings and `k` is the average length of a string.
* **Space Complexity**: O(n \* k), to store the grouped anagrams.

### Count-based approach

* **Time Complexity**: O(n \* k), as character counting is linear in the size of each string.
* **Space Complexity**: O(n \* k), similar to above for storing results and keys.
