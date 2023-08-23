# remove duplicate letters from a string
text='hello pradeep singh rajput'
final_text=[]
for i in text:
    if i not in final_text:
        final_text.append(i)
    else:
        continue
print(''.join(final_text))