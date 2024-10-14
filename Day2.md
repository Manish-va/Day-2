# 1. Sorting a List.

To sort a list without using the built-in sort() method, we can use the Bubble Sort algorithm. This method repeatedly traverses the list, compares adjacent elements, and swaps them if they are not in the correct order.
```
my_list = [6, 3, 2, 5, 8, 11, 33]  # Initialize the list
n = len(my_list)  # length of the list
for i in range(n):
    for j in range(0, n-i-1):  # exclude the last i elements that are already sorted
        if my_list[j] > my_list[j + 1]: #compare
            my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]  # Swap elements
print(my_list)
```
Output:- [2, 3, 5, 6, 8, 11, 33]


# 2. Find the Longest Common Prefix .

```
words = ["dog", "door", "done"]
if not words:
    result = ""
else:
    # Find the shortest word
    shortest_word = min(words, key=len)
    prefix = ""
    for i in range(len(shortest_word)):
        char = shortest_word[i]
        for word in words:
            if word[i] != char:
                # Step 4: Break if characters do not match
                result = prefix
                break
        else:
            #add character to prefix
            prefix += char
            continue
        break
    result = prefix
print(result)
```
Output:- do


# 3. Roman Numeral Converter

```
roman= {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}
s = "MCMXCIV"

res = 0
prev_value = 0
# iteration through each character in roman no. string
for n in s:
    current_value = roman[n]
    if current_value > prev_value:
        # Adjust for subtraction case
        res += current_value - 2 * prev_value  
    else:
        # Add current value
        res += current_value  
    # Update previous value
    prev_value = current_value  
print(res)
```
Output:- 1994