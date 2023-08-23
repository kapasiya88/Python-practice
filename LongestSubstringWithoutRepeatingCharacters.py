#Longest substring without repeating characters.
string = "geeksforgeeks"
c_list=[]
c_final_list=[]

for c in string:
    if c in c_list:
        c_final_list.append(''.join(c_list))
        c_list=[]
        c_list.append(c)
    else:
        c_list.append(c)
c_final_list.append(''.join(c_list))

max_len_sub=max(c_final_list,key=len)
print(max_len_sub)