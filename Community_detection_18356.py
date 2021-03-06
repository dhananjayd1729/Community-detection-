# -*- coding: utf-8 -*-
"""lab project 18356

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1N8EF5--ftRJ9SfvOokfsebtmxcQeidUO
"""

!pip install networkx
!pip install matplotlib

!pip install community

from google.colab import files
uploaded = files.upload()

import community as community_louvain
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import networkx as nx

# load the karate club graph
G = nx.read_gml("dolphins.gml")

# compute the best partition
partition = community_louvain.best_partition(G)

# draw the graph
pos = nx.spring_layout(G)
# color the nodes according to their partition
cmap = cm.get_cmap('viridis', max(partition.values()) + 1)
nx.draw_networkx_nodes(G, pos, partition.keys(), node_size=40,
                       cmap=cmap, node_color=list(partition.values()))
nx.draw_networkx_edges(G, pos, alpha=0.5)
plt.show()
# modularity(partition, G)
# print(modularity)

0.41567

nx.__version__

!pip install python-modularity-maximization==0.0.1rc4

from modularity_maximization import partition
from modularity_maximization.utils import get_modularity

import networkx as nx
import matplotlib.pyplot as plt

# load the graph
G = nx.read_gml("dolphins.gml")

# visualize the graph
nx.draw(G, with_labels = True)

len(G.nodes), len(G.edges)

def edge_to_remove(graph):
  G_dict = nx.edge_betweenness_centrality(graph)
  edge = ()

  # extract the edge with highest edge betweenness centrality score
  for key, value in sorted(G_dict.items(), key=lambda item: item[1], reverse = True):
      edge = key
      break

  return edge

def girvan_newman(graph):
	# find number of connected components
	sg = nx.connected_components(graph)
	sg_count = nx.number_connected_components(graph)

	while(sg_count == 1):
		graph.remove_edge(edge_to_remove(graph)[0], edge_to_remove(graph)[1])
		sg = nx.connected_components(graph)
		sg_count = nx.number_connected_components(graph)

	return sg

#find communities in the graph
c = girvan_newman(G.copy())

# find the nodes forming the communities
node_groups = []

for i in c:
  node_groups.append(list(i))

node_groups

# plot the communities
color_map = []
for node in G:
    if node in node_groups[0]:
        color_map.append('blue')
    else: 
        color_map.append('green')  

nx.draw(G, node_color=color_map, with_labels=True)
plt.show()

print( nx.algorithms.community.modularity(G,nx.algorithms.community.label_propagation_communities(G)))

!pip install igraph

!pip install lsalib

g = make_graph("Zachary")
coords = layout_with_fr(g)
# plot the graph
plot(g, layout=coords, vertex.size=10)



