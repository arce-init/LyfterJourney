def count_upper(my_string):
    upper = 0
    lower = 0
    for letter in my_string:
        if letter.isupper():
            upper = upper + 1
        elif letter.islower():
            lower = lower + 1
    print(f"There's {upper} upper cases and {lower} lower cases")

count_upper("I love Pollos Don Fransisco")

