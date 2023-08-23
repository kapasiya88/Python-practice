# write a program to print input string after removing all vowels.
input_string='Kajaleopl'
vowel_list='aeiouAEIOU'
for i in vowel_list:
    if i in input_string:
        input_string=input_string.replace(i,'')
print(input_string)