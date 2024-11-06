def vowels_remove(in_string):
    output=[c for c in in_string if c not in 'aeiou']
    return output
print("Enter word to remove vowels")
input_string=input()
print("Output is : ",vowels_remove(input_string))
def double_number(int_num):
    return [2*i if i%2==0 else i for i in int_num]
print(double_number([i for i in range(10)]))
