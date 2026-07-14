employees = [
    {"name": "Carlos", "email": "carlos@empresa.com", "department": "Ventas"},
    {"name": "Ana", "email": "ana@empresa.com", "department": "TI"},
    {"name": "Luis", "email": "luis@empresa.com", "department": "Ventas"},
    {"name": "Sofia", "email": "sofia@empresa.com", "department": "RRHH"},
]

result = {}

for employees in employees:
    dept = employees['department']
    name = employees['name']

    if dept in result:
        result[dept].append(name)
    else:
        result[dept] = [name]

print(result)