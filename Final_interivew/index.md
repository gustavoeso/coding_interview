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

* Try creating a sorted version of each word to serve as a key.
* Store each word in a dictionary using its sorted form as a grouping key.
* The dictionary will automatically group all words with the same characters.
* After building the dictionary, return all the values as the grouped anagrams.

## Solution

### Step 1: Generate a canonical representation

For each word in the input list, sort the characters alphabetically. This sorted string will serve as a unique identifier (or key) for its group of anagrams.

For example:
```python
"eat" -> "aet"
"tea" -> "aet"
"tan" -> "ant"
```

### Step 2: Use a dictionary to group anagrams

Iterate through the original list of words:
- Compute the sorted version of the word (key)
- If the key doesn't exist in the dictionary, create it
- Add the original word to the corresponding group

### Step 3: Return the groups

At the end, return the dictionary's values as a list of anagram groups.

### Python Implementation

```python
def group_anagrams(words):
    """
    Agrupa palavras que são anagramas entre si usando ordenação de caracteres.
    """
    grupos = {}

    for palavra in words:
        # Cria a chave a partir da palavra ordenada
        chave = ''.join(sorted(palavra))

        # Adiciona a palavra no grupo correspondente
        if chave not in grupos:
            grupos[chave] = [palavra]
        else:
            grupos[chave].append(palavra)

    # Retorna todos os grupos
    return list(grupos.values())
```

## Time and Space Complexity

### Time Complexity
* **O(n * k log k)**, onde `n` é o número de palavras e `k` é o tamanho médio de cada palavra (por conta do `sorted`).

### Space Complexity
* **O(n * k)**, para armazenar os grupos de anagramas e as chaves.

Esta abordagem é eficiente, clara e muito usada em entrevistas. Não há necessidade de ordenar a lista de entrada nem utilizar estruturas adicionais como listas auxiliares ordenadas. A lógica se sustenta apenas na construção da chave ordenada e agrupamento via dicionário.
