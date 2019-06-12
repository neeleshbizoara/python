a = [0,1,2,3,4,5,6]
for x in a:
    if x == 3:
        break # terminate the loop
    print(x)
print('----------------------')
i = 0
while i<5:
    if i == 3:
        break
    print(i)
    i += 1




for x in a:
    if x == 2:
        continue # escipe this condition
    print(x)
print('----------------------')
i = 0
while i<5:
    i += 1
    if i == 3:
        continue
    print(i)
    #i += 1 This statment is not executed when if condition is true so move this statment after while