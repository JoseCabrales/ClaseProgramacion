
perro = {}


perro['nombre'] = 'Mateo'
perro['color'] = 'Blanco'
perro['raza'] = 'French Poodle'
perro['patas'] = '4 Patas'
perro['edad'] = '10 Años'

print("Diccionario Perro")
print(perro)


estudiante = {
    'Nombre': 'Jose',
    'Apellido': 'Cabrales',
    'Sexo': 'Masculino',
    'Edad': 18,
    'Estado Civil': 'Comprometido',
    'Habilidades': ['Python', 'Java'],
    'Pais': 'Colombia',
    'Ciudad': 'Cartagena',
    'Direccion': 'Barrio La central kra62a #22A11'
}


longitud_estudiante = len(estudiante)


Habilidades = estudiante['Habilidades']
tipo_habilidades = type(Habilidades)


estudiante['Habilidades'].extend(['Adaptacion', 'Entrenamiento con pesas'])


claves_estudiante = list(estudiante.keys())


valores_estudiante = list(estudiante.values())


lista_tuplas_estudiante = list(estudiante.items())


del estudiante['Direccion']


del perro
print("Diccionario Perro Borrado...")


print("Diccionario del estudiante:", estudiante)
print("Longitud del diccionario del estudiante:", longitud_estudiante)
print("Tipo de datos de las habilidades:", tipo_habilidades)
print("Claves del diccionario del estudiante:", claves_estudiante)
print("Valores del diccionario del estudiante:", valores_estudiante)
print("Lista de tuplas del diccionario del estudiante:", lista_tuplas_estudiante)