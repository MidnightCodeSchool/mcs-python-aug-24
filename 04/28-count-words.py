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

lorem_ipsum = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. veniam. veniam. 
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""


def count_words(sentence) -> dict:
    cleaned_sentence = sentence \
        .lower() \
        .replace(",", "") \
        .replace(".", "") \
        .replace("\n", " ") \
        .strip()
    words = cleaned_sentence.split()

    counter = {}
    for word in words:
        if counter.get(word, None) is not None:
            counter[word] += 1
        else:
            counter[word] = 1
    
    return counter

print(count_words(lorem_ipsum))