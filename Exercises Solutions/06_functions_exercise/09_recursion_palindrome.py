def palindrome(word, idx):
    if idx >= len(word) // 2:
        return f"{word} is a palindrome"

    right = word[idx]
    left = word[-1 - idx]
    if right != left:
        return f"{word} is not a palindrome"

    return palindrome(word, idx + 1)


print(palindrome("abcba", 0))


# -----------------------------------------Second way------------------------------------
# data = "abba"
#
# for i in range(len(data)):
#     left = data[i]
#     right = data[-1 - i]
#
#     if left != right:
#         print("False")
#         break
# else:
#     print("True")