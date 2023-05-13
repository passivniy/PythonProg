import math
from import_modules.validator import set_values
from import_modules.isnt_negatives import numbers_isnt_negatives


# MODULE isnt_negatives: 

# def numbers_isnt_negatives(lst:list):
#    for x,i in enumerate(lst):
#        while lst[x]<=0:
#            lst[x]=int(input(f'Enter correct value(i>0,your value is : {lst[x]}): '))
#   return lst if len(lst)>1 else lst[0]



print('''Task_3 Danyil
 Lytvynov IKM-221D Task_3 ''')

x=numbers_isnt_negatives(set_values())

print(f'y = {math.sqrt(math.log(pow(x, 2) - 4))}')
