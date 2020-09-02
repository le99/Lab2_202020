import config as cf
import csv
from ADT import list as lt
from DataStructures import listiterator
from time import process_time 

from Sorting import insertionsort 
from Sorting import selectionsort 
from Sorting import quicksort 
from Sorting import mergesort 
from Sorting import quicksort3way
import sys

# print(sys.getrecursionlimit())
sys.setrecursionlimit(10000)

lista = lt.newList('ARRAY_LIST', None)

def printList(lista):
    iter = listiterator.newIterator(lista)
    while listiterator.hasNext(iter):
        c = listiterator.next(iter)
        print(c["apellido"], ",", c["nombre"])

with open("Data/p3.csv", encoding="utf-8-sig") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')
    for row in reader:
        lt.addLast(lista, row)



t1_start = process_time()

#======================================
# Ordenar personas ascendentemente por (apellido, nombre)
#======================================

def less(e1, e2):
    if e1["apellido"] < e2["apellido"]:
        return True
    elif e1["apellido"] == e2["apellido"] and e1["nombre"] < e2["nombre"]:
        return True
    else:
        return False


#=======================================

l = lt.subList(lista, 1, lt.size(lista))
t1_start = process_time()
insertionsort.insertionSort(l, less)
t1_stop = process_time()
# printList(l)
print("InsertionSort:\t",t1_stop-t1_start," segundos")

#=======================================

l = lt.subList(lista, 1, lt.size(lista))
t1_start = process_time()
selectionsort.selectionSort(l, less)
t1_stop = process_time()
# printList(l)
print("SelectionSort:\t",t1_stop-t1_start," segundos")

#=======================================

l = lt.subList(lista, 1, lt.size(lista))
t1_start = process_time()
mergesort.mergesort(l, less)
t1_stop = process_time()
# printList(l)
print("MergeSort:\t",t1_stop-t1_start," segundos")

#=======================================

l = lt.subList(lista, 1, lt.size(lista))
t1_start = process_time()
quicksort.quickSort(l, less)
t1_stop = process_time()
# printList(l)
print("QuickSort:\t",t1_stop-t1_start," segundos")

#=======================================

l = lt.subList(lista, 1, lt.size(lista))
t1_start = process_time()
quicksort3way.quickSort3Way(l, less)
t1_stop = process_time()
# printList(l)
print("Quick3-way:\t",t1_stop-t1_start," segundos")
