# Group Anagrams - Solution

from collections import defaultdict
from typing import List

def group_anagrams_sorted(strs: List[str]) -> List[List[str]]:
    """
    Group anagrams using sorted strings as dictionary keys.
    Time Complexity: O(n * k log k)
    Space Complexity: O(n * k)
    """
    anagram_map = defaultdict(list)
    
    for word in strs:
        # Step 1: Sort each word to get the key
        sorted_word = ''.join(sorted(word))
        # Step 2: Group by the sorted word
        anagram_map[sorted_word].append(word)

    # Step 3: Return grouped values
    return list(anagram_map.values())

def group_anagrams_count(strs: List[str]) -> List[List[str]]:
    """
    Group anagrams using character count tuple as dictionary keys.
    Time Complexity: O(n * k)
    Space Complexity: O(n * k)
    """
    anagram_map = defaultdict(list)

    for word in strs:
        # Step 1: Count frequency of each character (assuming lowercase a-z)
        count = [0] * 26
        for char in word:
            count[ord(char) - ord('a')] += 1
        # Step 2: Use count as key
        key = tuple(count)
        anagram_map[key].append(word)

    # Step 3: Return grouped values
    return list(anagram_map.values())

# Example usage
if __name__ == "__main__":
    input_words = ["eat", "tea", "tan", "ate", "nat", "bat"]

    print("--- Using sorted key ---")
    print(group_anagrams_sorted(input_words))

    print("--- Using count key ---")
    print(group_anagrams_count(input_words))
