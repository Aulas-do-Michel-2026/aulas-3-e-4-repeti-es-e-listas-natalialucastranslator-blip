"""
#### Exercício 3 - Comparando listas.

Receba duas listas de input do usuário. Ele digitará como um texto com os números separados por vígula. 
Para isso, pode-se utilizar o código disponibilizado que vai transformar esse texto em lista para você.

Eu quero que você me diga qual das listas tem o maior número dentro delas. 

Se a primeira lista tiver o maior número, imprima: "Primeira".
Se a segunda lista tiver o maior número, imprima: "Segunda".
Se ambas tiverem o mesmo número como maior, digite: "Ambas".

Exemplos:

----------------------------------

Digite a sua primeira lista (separando os números por vírgula): 1, 50, 2, 40
Digite a sua segunda lista (separando os números por vírgula): 0, 2, 99, 1, 1, 3

Resposta:
Segunda

----------------------------------

Digite a sua primeira lista (separando os números por vírgula): 1, 0, 2, 30
Digite a sua segunda lista (separando os números por vírgula): 9, 9, 9, 30

Resposta:
Ambas
"""

# Código para pegar as listas de input
primeira_lista = [*map(int, input("Digite a sua primeira lista (separando os números por vírgula): ").split(","))]
segunda_lista = [*map(int, input("Digite a sua segunda lista (separando os números por vírgula): ").split(","))]

entrada1 = input("Digite a sua primeira lista (separando os números por vírgula): ")
lista1_strings = entrada1.split(",")
primeira_lista = []
for item in lista1_strings:
    primeira_lista.append(int(item))
entrada2 = input("Digite a sua segunda lista (separando os números por vírgula): ")
lista2_strings = entrada2.split(",")
segunda_lista = []
for item in lista2_strings:
    segunda_lista.append(int(item))
maior1 = max(primeira_lista)
maior2 = max(segunda_lista)
if maior1 > maior2:
    print("Primeira")
elif maior2 > maior1:
    print("Segunda")
else:
    print("Ambas")
