'''def_uppercase(input_name):
    output_name=''
    for character in input_name:
        lower_case_ascii_number=ord(character)
        upper_case_ascii_number=lower_case_ascii_number+32       #-32
        output_name+=chr(upper_case_ascii_number)
    return output_name
input_namee='ARUN'
output_name=upper_case(input_name)
print('uppercase:',output_name)'''


'''input_name="ARUn"
count=0

total_length=len(input_name)
for character in input_name:
        lower_case_ascii_number=ord(character)
        if 65<=lower_case_ascii_number and lower_case_ascii_number<=97:
            count+=1

if count==total_length:
    print("true")
else:
    print("false")'''
            
