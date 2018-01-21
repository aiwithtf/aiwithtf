from graphviz import Digraph


def visualize_graph(graph):
    dot = Digraph()

    for n in graph.as_graph_def().node:
        dot.node(n.name, label=n.name)

        for i in n.input:
            dot.edge(i, n.name)

    return dot
