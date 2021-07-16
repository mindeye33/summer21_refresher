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

# from an adjacency matrix, zeros out all distances > 2, and anything below 2 is turned to 1
# build a stripped down connectivity matrix, based on some cutoff

# plots the adjacency matrix, with some cutoff
def plot(adjacency, cutoff = 2.0):
    graph = nx.from_numpy_matrix(adjacency, create_using=nx.MultiGraph)
    nx.draw(graph, with_labels=True, font_weight='bold')
    plt.savefig("graph.png")
    #plt.show()

# outputs the bonds csv
def output_csv(mat, outname):
    np.savetxt(outname, mat, delimiter=",", fmt='%u')


#xyz = parse('xyz/allyl.xyz')
#plot(adjacency) 
#output_csv(bonds, "adjacency/allyl.csv")

