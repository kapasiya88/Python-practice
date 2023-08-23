# Write a function to reverse the order of words in a sentence.
def reverse_sentence(sen):
    state_list=state.split(' ')
    state_reverse=state_list[::-1]
    return (' '.join(state_reverse))

state='Implement a function to reverse the order of words in a given sentence'
print(reverse_sentence(state))