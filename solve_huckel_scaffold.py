import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# parses a csv file into a numpy array
def parse(csv_name):
    bonds = pd.read_csv(csv_name, sep=',', header=None)
    bonds = np.array(bonds)
    return bonds

# based on some values of alpha and beta, builds the huckel hamiltonian

# finds eigenvectors/eigenvalues of a matrix

#plots eigenvalues and saves it to mo_diagram.png
def plot(eigvals):
    x = np.array(range(len(eigvals)))
    y = np.array(eigvals)
    plt.scatter(x, y, c="b", marker="_")
    plt.title("Orbital Eigenvalues")
    #plt.title("Occupied Orbital Eigenvalues of C$_{60}$")
    #plt.xlabel("Eigenvalue")
    plt.ylabel("Energy")
    plt.savefig('mo_diagram.png')
    #plt.show()


alpha = -3 #-11.2
beta = -2 #-3.5

bonds = parse('c60_bonds.csv')
#plot(eigvals)
