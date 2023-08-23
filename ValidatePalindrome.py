# check whether given phrase is a palindrome or not.
# After converting all uppercase letters to lowercase and removing all non alphanumeric letters,a phrase should be same from both the ends.
# "Madam, I'm Adam"
# “A man, a plan, a canal—Panama,”
# “Able was I ere I saw Elba”
# "rotator"
# "kajal"

s="kajal"
s2=[i.lower() for i in s if i.isalnum()]
if ''.join(s2)==''.join(reversed(s2)):
    print('True')
else:
    print('False')