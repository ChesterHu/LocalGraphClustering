from typing import *
import numpy as np
from .cpp import densest_subgraph_cpp
from .GraphLocal import GraphLocal

def densest_subgraph(G):
    """
        Finding a maximum density subgraph.
        For details please refer to: A.V.Goldberg. Finding a maximum density subgraph
        link: http://digitalassets.lib.berkeley.edu/techreports/ucb/text/CSD-84-171.pdf

        Parameters
        ----------

        G: GraphLocal
            
        Returns
        -------

        output 0: maximum density
        output 1: A cluster with the maximum density.

        """ 
    n = G.adjacency_matrix.shape[0]

    (density,actual_xids) = densest_subgraph_cpp(n,np.int64(G.adjacency_matrix.indptr),
                np.int64(G.adjacency_matrix.indices),np.float64(G.adjacency_matrix.data/2),G.lib)

    return [density,actual_xids]
