# implement a function to find the longest common prefix among a list of strings.
l=['kajala','kajlp','kajaae','kajapt']
# l=['geeksforgeeks','geeks','geek','geezer']
# l=['apple','ape','april']
a=[]
b=[]

def find_left_str(strlist,min_str,start,end):
    add_text=0
    low=start    
    high=end             
    for i in strlist:
        if i[low:high]==min_str:
            add_text=1
        else:
            add_text=0
            break 
    if add_text==1:
        return (a.append(min_str))
    else:
        mid=int(start+(len(min_str)/2))
        find_left_str(strlist,min_str[start:mid],start,mid)
        find_right_str(strlist,min_str[mid:high],mid,high)

def find_right_str(strlist,min_str,start,end):
    add_text=0
    low=start       
    high=end      
    
    for i in strlist:
        if i[low:high]==min_str:
            add_text=1
        else:
            add_text=0
            break 
    if add_text==1:
        return (b.append(min_str))
    elif len(min_str) > 1:
        low=start
        mid=int(len(min_str)/2)
        high=low+len(min_str)
        
        find_left_str(strlist,min_str[0:mid],low,low+mid) #e,2,1
        find_right_str(strlist,min_str[mid:len(min_str)],mid,high)  #k,1,4
    else:
        return (b.append(''))
        

min_len_string=len(min(l,key=len))
min_str=min(l,key=len)
mid=int(min_len_string/2)

left_str=find_left_str(l,min_str[0:mid],0,mid)
right_str=find_right_str(l,min_str[mid:min_len_string],mid,min_len_string)
final_list=a+b
print(''.join(final_list))
