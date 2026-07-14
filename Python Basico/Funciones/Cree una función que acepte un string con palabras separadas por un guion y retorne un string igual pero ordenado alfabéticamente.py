def sort_string(my_string):
    my_list = my_string.split("-")    
    my_list.sort()
    result = "-".join(my_list)        
    return result

print(sort_string("python-variable-function-computer-monitor"))