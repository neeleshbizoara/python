def student(name, age):
    print("Name:", name)
    print("age:", age)

student("Neelesh", 32)
print('-------Default Argument-------')
'''Default Argument'''
def employee(name='Unknown', age=0):
    print("Name:", name)
    print("Age:",age)

employee()
employee('Neelesh')

print('----------Variable length arguments------------')
'''Variable length arguments
Here *workin will give tuple'''
def Company(name, since, *workin):
    print('Company Name is', name)
    print('Since', since)
    print('Work in', workin)
    for x in workin:
        print(x)

Company('Msys', 2015, 'Storage', 'Virtualization', 'Networking', 'Finance', 'Machine Learning', 'Telecom')

print('We can pass key value pair to function')
'''Here **workin will give dictionary'''

def Company(name, since, **workin):
    print('Company Name is', name)
    print('Since', since)
    print('Work in', workin)
    for domain, client in workin.items():
        print('{0} is working in {1} doamin current client is {2}'.format(name, domain, client))

Company('Msys', 2015, Storage = 'Tintri', Virtualization = "Tintri", Networking="Velocloud", Finance="Paytm", ML = "Idea")

