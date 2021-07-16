#import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx


# parses the coordinates from an xyz file
def parse(xyz_name):
    # make a new datatype (numpy.void)
    xyz_row_format = np.dtype(dtype=[('element', 'U1'), ('x', 'f8'), ('y', 'f8'),('z', 'f8')])
    xyz = np.genfromtxt(xyz_name, skip_header=2, dtype=xyz_row_format)
    return xyz

# throws out all atoms that are not carbon, and returns a numpy array

# finds distance between two vectors

# builds adjacency matrix, with no cutoffs

# from an adjacency matrix, it extracts which atoms are < cutoff aways

# plots the adjacency matrix, with some cutoff
def plot(adjacency, cutoff = 2.0):
    adjacency = np.where(adjacency <= cutoff, adjacency, 0)
    graph = nx.from_numpy_matrix(adjacency, create_using=nx.MultiGraph)
    nx.draw(graph, with_labels=True, font_weight='bold')
    plt.savefig("graph.png")
    #plt.show()

# outputs the bonds csv
def output_csv(mat, outname):
    #np.savetxt(outname, mat, delimiter=",")
    np.savetxt(outname, mat, delimiter=",", fmt='%u')


#xyz = parse('xyz/benzene.xyz')
#plot(adjacency) 
#output_csv(bonds, "benzene_bonds.csv")

