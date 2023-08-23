# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

s = "{[]}"
# s = "()[]{}"
# s="(]"
s_dict={'(':')','[':']','{':'}'}
a=[]
out='True'
for i in s:
    if i in s_dict.keys():
        a.append(i)
    elif i in s_dict.values():
        b=a.pop()
        if s_dict[b]!=i:
            out='False'
            break
print (out)