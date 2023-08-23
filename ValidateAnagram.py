# print if the given 2 text are anagram of each other or not.
a1="conversation"
a2="voices rant on"
a1_temp=list(a1.replace(" ",""))
a2_temp=list(a2.replace(" ",""))
a1_temp.sort()
a2_temp.sort()
if a1_temp==a2_temp:
    print("it is an anagram")
else:
    print("not an anagram")