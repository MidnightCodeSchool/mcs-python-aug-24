"""
Use dictionary to count the number of words in a sentence.
Clean the sentence by:
- string.split()
- string.lower()
- string.replace()
then count the words using dictionary.
{
"lorem": 2,
"ipsum": 3,
}
...
"""

from collections import Counter


lorem_ipsum = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. veniam. veniam. 
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""


def count_words(sentence) -> Counter:
    """
    ใช้ Counter ในการนับจำนวนคำในประโยค แทนการใช้ dictionary
    """
    cleaned_sentence = sentence \
        .lower() \
        .replace(",", "") \
        .replace(".", "") \
        .replace("\n", " ") \
        .strip()
    words = cleaned_sentence.split()

    return Counter(words)

print(count_words(lorem_ipsum))