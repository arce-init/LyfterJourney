list_a =['first_name', 'last_name', 'role'] 
list_b =['Alejandro', 'Arce', 'Technical Support Engineer']

my_dict = {}
for i in range(len(list_a)):
    my_dict[list_a[i]] = list_b[i]

print(my_dict)