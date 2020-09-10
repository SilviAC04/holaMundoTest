"""
Programa de Nomina de Empleados
"""


empleado_1 = {'nombre':'Silvana', 'edad': 35, 'telefono':'0992762653','salario': 1250.22,'puesto':'jefe'}
empleado_2 = {'nombre':'Lenin', 'edad': 36, 'telefono':'0992762654','salario': 1000.22,'puesto':'analista'}
empleado_3 = {'nombre':'Diana', 'edad': 37, 'telefono':'0992762655','salario': 850.22,'puesto':'tecnico'}

lista_empleados = [empleado_1,empleado_2,empleado_3]

for empleado in lista_empleados:
    nombre_empleado = empleado['nombre']
    salario_empleado = empleado['salario']

    print(nombre_empleado, salario_empleado)