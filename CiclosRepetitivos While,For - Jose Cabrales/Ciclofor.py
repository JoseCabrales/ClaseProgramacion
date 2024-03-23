vuelo = {
    "Aerolinea": "Avianca",
    "Vuelo": "AV3102",
    "Origen": "CTG",
    "Destino": "MDE",
    "Tipo_Maleta": ['Cabina', 'Mano', 'Bodega']
}

print("Valores del diccionario:")
for key, value in vuelo.items():
    print(f"{key}: {value}")


print("\nValores del tipo de maleta:")
for tipo_maleta in vuelo["Tipo_Maleta"]:
    print(tipo_maleta)