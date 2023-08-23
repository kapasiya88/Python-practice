# Implement Trie (Prefix Tree)
# https://leetcode.com/problems/implement-trie-prefix-tree/description/
def insert(word):
    Trie.append(word)
    output.append('null')

def search(word):
    if word in Trie:
        output.append("True")
    else:
        output.append("False")
        
def startsWith(prefix):
    for i in Trie:
        output.append(i.startswith(word))

        

commands=["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
values=[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
print(commands)
print(values)

Trie=[]
output=[]
for i in enumerate(commands):
    if i[0]==0:
        Trie
        output.append('null')
    elif i[1]=='insert':
        index=i[0]
        insert(''.join(values[index]))
    elif i[1]=='search':
        index=i[0]
        word=''.join(values[index])
        search(word)
    elif i[1]=='startsWith':
        index=i[0]
        word=''.join(values[index])
        startsWith(word)
print(Trie)
print(output)
