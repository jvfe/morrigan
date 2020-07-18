# -*- coding: utf-8 -*-
"""Main module template with example functions."""
import networkx as nx
from networkx.readwrite import json_graph
import json


def g_inp(inp_graph):
    if ".txt" in inp_graph:
        G = nx.read_edgelist(inp_graph)
        return G

    elif ".xml" in inp_graph:
        G = nx.read_graphml(inp_graph)
        return G


def g_out(graph, outfile):
    if ".json" in outfile:
        data = json_graph.node_link_data(graph)
        with open(outfile, "w") as f:
            json.dump(data, f)
    elif ".txt" in outfile:
        nx.write_edgelist(graph, outfile)
