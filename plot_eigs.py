import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please specify eigenvalue file.")
    else:
        inname = sys.argv[1]

## using function in adjacent file
from find_adjacent import *
from solve_huckel import *

if __name__ == "__main__":
    eigs = parse_csv(inname)
    plot_orbdiag(adjacency)
    
