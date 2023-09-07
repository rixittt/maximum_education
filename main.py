def palindrome(input_string):
    input_string = input_string.lower()
    return input_string == input_string[::-1]


input_str1 = "лепсспел"
input_str2 = "helloworld"

res1 = palindrome(input_str1)
res2 = palindrome(input_str2)

print(res1)
print(res2)
