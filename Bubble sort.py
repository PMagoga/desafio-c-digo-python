#defino a função bubble sort

def bubble_sort(lista):
    for numero in range(len(lista)-1,0,-1):
        for i in range(numero):
            if lista[i]>lista[i+1]:
                item = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = item
                print(lista)
    return lista

lista = [2, 5, 3, 7, 13, 1, 4]
print(bubble_sort(lista))