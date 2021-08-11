import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please specify adjacency infile.")
    else:
        inname = sys.argv[1]


# parses a csv file into a numpy array
def parse_csv(csv_name):
    adjacency = pd.read_csv(csv_name, sep=',', header=None)
    adjacency = np.array(adjacency)
    return adjacency

# based on some values of alpha and beta, builds the huckel hamiltonian
def build_hamil(alpha, beta, adjacency):
    dim = len(adjacency)
    ham = np.zeros((dim,dim))
    
    for i in range(dim):
        ham[i,i] = alpha
    
    ham += beta*adjacency
    print(ham)
    return ham

# finds eigenvectors/eigenvalues of a matrix
def diagonalize(ham): 
    eigvals, eigvecs = np.linalg.eigh(ham)
    #print(eigvals)
    return eigvals, eigvecs


#plots eigenvalues and saves it to mo_diagram.png
def plot_orbdiag(eigvals):
    x = np.array(range(len(eigvals)))
    y = np.array(eigvals)
    plt.scatter(x, y, c="b", marker="_")
    plt.title("Orbital Eigenvalues")
    #plt.title("Occupied Orbital Eigenvalues of C$_{60}$")
    #plt.xlabel("Eigenvalue")
    plt.ylabel("Energy")
    plt.savefig('mo_diagram.png')
    #plt.show()


if __name__ == "__main__":
    alpha = -3 #-11.2
    beta = -2 #-3.5
    
    adjacency = parse_csv(inname)
    hamiltonian = build_hamil(alpha, beta, adjacency)
    eigvals, eigvecs = diagonalize(hamiltonian)
    plot_orbdiag(eigvals)
