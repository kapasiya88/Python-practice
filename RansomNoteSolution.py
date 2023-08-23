# Ransom Note Solution in Python
# https://lifewithdata.com/2023/06/15/leetcode-ransom-note-solution-in-python/#:~:text=The%20problem%20requires%20us%20to,by%20the%20ransom%20note%20string.
from collections import Counter 
magazine = "give me one grand today night"
ransomnote = "give one grand today"
cnt_magazine=Counter(magazine)
cnt_ransomnote=Counter(ransomnote)
print(cnt_magazine)
print(cnt_ransomnote)
for key,val in cnt_ransomnote.items():
    if val > cnt_magazine[key]:
        flag=False
        break
    else:
        flag=True
print(flag)