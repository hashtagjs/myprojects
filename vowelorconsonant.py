vowels = ['a','e','i','o','u','A','E','I','O','U']
n = raw_input()
if (n.isalpha()):
    if (n in vowels):
        print("vowel")
    else:
        print("consonant")
else:
    print("invalid")
