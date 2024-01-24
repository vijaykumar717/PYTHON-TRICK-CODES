##generate a google meet link

import random

meet_link=''

link_address=''

link='https://meet.google.com/'

val=int(input("enter your value"))
for even in range(0,val):
    empty_string=''
    if even%2==0:
        for char in range(0,3):
            ltr=random.randint(97,122)
            new_ltr=chr(ltr)
            empty_string+=new_ltr
    else:
        for char in range(0,4):
            letter=random.randint(97,122)
            new_letter=chr(letter)
            empty_string+=new_letter
    link_address+=empty_string+'-'
meet_link+=link+link_address

print(meet_link.strip('-'))
    
