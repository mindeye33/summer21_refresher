import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def parse(csv_name):
    bonds = pd.read_csv(csv_name, sep=',', header=None)
    bonds = np.array(bonds)
    return bonds

def build_hamil(alpha, beta, bonds):
    dim = len(bonds)
    ham = np.zeros((dim,dim))
    
    for i in range(dim):
        ham[i,i] = alpha
    
    for i in range(dim):
        neighbs = bonds[i]
        for neighb in neighbs:
            ham[i, neighb] = beta
    #print(ham)
    return ham

def diagonalize(ham): 
    eigvals, eigvecs = np.linalg.eigh(ham)
    #print(eigvals)
    return eigvals, eigvecs


#plotting
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
hamiltonian = build_hamil(alpha, beta, bonds)
eigvals, eigvecs = diagonalize(hamiltonian)
plot(eigvals)
