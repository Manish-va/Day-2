my_list = [6, 3, 2, 5, 8, 11, 33]  # Initialize the list
n = len(my_list)  # length of the list
for i in range(n):
    for j in range(0, n-i-1):  # exclude the last i elements that are already sorted
        if my_list[j] > my_list[j + 1]: #compare
            my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]  # Swap elements
print(my_list)
