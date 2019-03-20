#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 11:08:45 2019

@author: anthonyplumb
"""

"""
Anthony Plumb
Phys 350 
Lab 07
"""

import numpy as np
from numpy.linalg import eig
import matplotlib.pyplot as plt


#Define original array
matrix=np.array([[2,-1],[-1,2]])

def calc_frequencies_and_modes(matrix,k_over_m):
    #multiply k_over_m into matrix
    M_matrix=matrix*k_over_m
    #slice eighenvalues from eigenvectors
    eighenvalues=eig(M_matrix)[0]
    #slice two eighenvectors into seperate frequencies
    frequency1=np.sqrt(eighenvalues[0])
    frequency2=np.sqrt(eighenvalues[1])
    #slice eighenvectors from eighenvalues
    eighenvector=eig(M_matrix)[1]
    return frequency1,frequency2,eighenvector

freq1,freq2,Vec=calc_frequencies_and_modes(matrix,1)

x_init=np.array([1,1])#initial array
test=np.array([1,0])

def calc_components_from_initial_conditions(x_init,Vec):
    #slice two eigenvectors to seperate them
    Ve1=Vec[:,0]
    Ve2=Vec[:,1]
    
    #dot product of initial vector and eigenvectors
    a=x_init@Ve1
    b=x_init@Ve2
    return a,b

#print(calc_components_from_initial_conditions(x_init,Vec))
#print(calc_components_from_initial_conditions(test,Vec))

t_init = 0
t_end = 10
N_times = 1000

time = np.linspace(t_init, t_end, num=N_times)

# So that we can multiply the array of times by two dimensinoal vectors
# later.
time = time.reshape(N_times, 1)

def func_x(freq1,freq2,Vec,time,x_init):
    a,b= calc_components_from_initial_conditions(x_init,Vec)
    xoft= a*np.cos(freq1*time)*Vec[:,0]+b*np.cos(freq2*time)*Vec[:,1]
    return xoft
xoft=func_x(freq1,freq2,Vec,time,x_init)


def plot_motion_of_masses(x, time, title='Movement of Masses'):
    """
    Function to make a plot of motion of masses as a function 
    of time. The time should be on the vertical axis and the 
    position on the horizontal axis.
    Parameters
    ----------
    x : array of position, N_times by 2 elements
        The array of positions, set up so that x[:, 0] 
        is the position of mass 1 relative to equilibrium
        and x[:, 1] is the position of mass 2.
    time : array of times
        Times at which the positions have been calculated.
    title : str
        A descriptive title for the plot to make grading easier.
    """
    # Nothing special about these, but they look nice
    x1_equilibrium_pos = 6
    x2_equilibrium_pos = 3

    x1 = x[:, 0] + x1_equilibrium_pos
    x2 = x[:, 1] + x2_equilibrium_pos

    plt.plot(x1, time, label='Mass 1')
    plt.plot(x2, time, label='Mass 2')
    plt.xlim(0, 9)
    plt.legend()
    plt.title(title)
    
    
plot_motion_of_masses(xoft,time)


matrix2=np.array([[2,-1],[-10,20]])
freq1_2,freq2_2,Vec2=calc_frequencies_and_modes(matrix2,1)
xoft_2=func_x(freq1_2,freq2_2,Vec2,time,x_init)
plot_motion_of_masses(xoft_2,time)
    
    
    
    
    