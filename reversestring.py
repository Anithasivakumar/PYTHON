def reverse(s): 
    return ' '.join(w[::-1] for w in s.split(" "))
s=input("")
print(reverse(s))
