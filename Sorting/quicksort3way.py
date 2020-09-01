"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """
"""
 Based on
 https://github.com/kevin-wayne/algs4/blob/master/src/main/java/edu/princeton/cs/algs4/Quick3way.java
"""

import config as cf
from ADT import list as adtlt
from random import randrange



def sort (lst, lo, hi, compareFunc):
    if (hi <= lo ):
        return
    
    lt = lo
    i = lo+1
    gt = hi
    v = adtlt.getElement(lst, lo + 1)
    
    while i <= gt:
        cmp = compareFunc(adtlt.getElement(lst, i+1), v)
        if cmp < 0:
            adtlt.exchange(lst, lt + 1, i + 1)
            lt = lt + 1
            i = i + 1
        elif cmp > 0:
            adtlt.exchange(lst, i + 1, gt + 1)
            i = i + 1
            gt = gt -1
        else:
            pass
    
    sort(lst, lo, lt-1, compareFunc)
    sort(lst, gt+1, hi, compareFunc)
  

def permutate(lst):
    for n in range(adtlt.size(lst)):
        r = randrange(n, adtlt.size(lst))
        adtlt.exchange(lst, n + 1, r + 1)

def quickSort3Way(lst, compareFunc):
    permutate(lst)
    sort (lst, 1 - 1 , adtlt.size(lst) - 1, compareFunc)

