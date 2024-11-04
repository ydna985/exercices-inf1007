#!/usr/bin/env python
# -*- coding: utf-8 -*-


# TODO: Importez vos modules ici
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
# TODO: Définissez vos fonctions ici (il en manque quelques unes)
def linear_values() -> np.ndarray:
    
    return np.array([])


def coordinate_conversion(cartesian_coordinates: np.ndarray) -> np.ndarray:
    return np.array([])


def find_closest_index(values: np.ndarray, number: float) -> int:
    return abs((values-number)).argmin()

def calcul_integral():
    result=integrate.quad(lambda x: np.exp(-x**2), -np.inf,np.inf)
    x=np.arange(-4,4,0.00000000000000001)
    y=[]
    for i in x:
        y.append(integrate.quad(lambda x: np.exp(-x**2), 0,x)[0])
    print(x.shape, np.array(y).shape)
    plt.plot(x,y)
    plt.show()
def mont_Carlo(nb_it=10000):
    x_cercle=[]
    y_cercle=[]
    otherx=[]
    othery=[]
    for i in range(nb_it):
        x=np.random.random()
        y=np.random.random()
        if np.sqrt(x**2+y**2) <= 1:
            x_cercle.append(x)
            y_cercle.append(y)
        else:
            otherx.append(x)
            othery.append(y)

    plt.scatter(x_cercle,y_cercle)
    plt.scatter(otherx,othery)
    plt.show()
    return 4*(len(x_cercle)/nb_it)
        
if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    print(coordinate_conversion(np.array([(0, 0), (10, 10), (2, -1)])))
    print(find_closest_index(np.array([1, 3, 8, 10]), 9.5))
    # x=np.linspace(-1,1,250)
    # y=x**2*np.sin(1/x**2)+x
    # plt.plot(x,y)
    # plt.show()
    # calcul_integral()
    mont_Carlo()

