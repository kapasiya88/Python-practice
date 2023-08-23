# implement a function to find the longest common suffix among a list of strings.
a=[]
b=[]
l=['kajlp','kalp','kajalp','kajalp']

def find_shortest_string(arr):
    min_string_len=len(min(arr,key=len))
    min_string=min(arr,key=len)

    if min_string_len > 1:
        mid=int(min_string_len//2)
        low=mid-min_string_len
        high=min_string_len
    else:
        mid=0
        low=-1
        high=0
        
    find_right_arr(arr,min_string,mid,low,high)


def find_right_arr(strlist,min_str,mid,start,end):
    add_text=0  
    min_str_right= min_str[start:]
    
    for i in strlist:
        if i[start:]==min_str_right:
            add_text=1
        else:
            add_text=0
            print(''.join(list(reversed(b))))
            break 
    if add_text==1:
        b.append(min_str_right)
        end=mid-end #-1
        new_arr=[i[:end] for i in strlist]
        find_shortest_string(new_arr)
    
find_shortest_string(l)

