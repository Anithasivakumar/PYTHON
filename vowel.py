n=str(input(""))
if(n=='A'or n=='a' or n=='E'or n=='e' or n=='I'or n=='i' or n=='O'or n=='o' or
   n=='U'or n=='u'):
    print("Vowel")
elif((n>='a'and n<='z') or (n>='A'and n<='Z')):
     print("Consonant")
else:
     print("Invalid")
