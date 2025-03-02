def reverse_string(x):
    s = ""
    for i in range(1, len(x) + 1):
        s += (x[-i])
    print(s)
    
    if x == s:
        print("Palindrome")
    else: 
        print("Not Palindrome") 


reverse_string("abcde1234")
reverse_string("abcdcba")
