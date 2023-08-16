lista1 = ["peliculas", "series", "novelas"]
lista2 = list((1, 2, 3, 4))  # tupla a converit en lista
lista3 = list(range(1, 11))
lista4 = ["hola", 1, 2, False, True]

# print(lista1)
# print(lista2)
# print(lista3)
# print(lista4)

# print("------------------")
# print(lista1.count("series"), " -> ", lista1)
# print(lista1.clear(), " -> ", lista1)
# print(lista1.append("agrego"), " -> ", lista1)
# print(lista1.insert(1, "inserto"), " -> ", lista1)
# print(lista1.index("inserto"), " -> ", lista1)
# print(lista1.pop(), " -> ", lista1)
# print(lista1.extend("persona"), " -> ", lista1)  # ingrsa cada letra de esta palabra
# print(lista1.remove("p"), " -> ", lista1)
# print(lista1.reverse(), " -> ", lista1)

# nuevo_programa = ""

# while nuevo_programa != "parar":
#     nuevo_programa = input("\ningrese nuevo programa televisivo: ")

#     if nuevo_programa != "parar":
#         lista1.append(nuevo_programa)

# print("\n######## Lista de programas ###########")
# for item in lista1:
#     print(f"{lista1.index(item)+1}, {item}")


print("\n######## Listas multidimensionales ###########")

lista4 = [[1, 2, [3, 4, 5], 3], [4, 5, 6], [7, 8, 9]]

print(lista4)

for item in lista4:
    for value1 in item:
        print("primera dimension-> ", value1)
        if isinstance(value1, list):
            print("---")
            for value2 in value1:
                print("segunda dimension-> ", value2)
            print("---")
