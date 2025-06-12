word = input("Enter a word: ")

vowels = "aeiouAEIOU"

#start loop and goes through every charachter in word
#each letter is temporary stored in the variable set in this case  | i |
 
for i in word:
    if i not in vowels: # not in checks if some
        print(i.upper()) #if is lowercase makes upper

# |not in| filters everything INSIDE the variable vowels so its not printed

# | in | filters everything OUTSIDE the variable voewls so its not printed