
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
