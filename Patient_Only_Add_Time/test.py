print() 
print('----------------------------------------')
print(format(f'DAY 1', "10s"))
print('----------------------------------------')
print('(Top to bottom: New Patients - Waiting - Admitted - Released)') 
print() 
for i in range(24): 
    print(format(f'{i}:00', '6s'), end = " ")
