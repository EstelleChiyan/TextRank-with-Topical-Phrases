from .graph import Graph


def build_graph(sentences, frequent_phrases):
    graph = Graph()
    for item in sentences:
        weight = 1
        for phrase in frequent_phrases.keys():
            if((item.text.lower()).find(phrase) >= 0):
                weight += 1
        if not graph.has_node(item.token):
            graph.add_node(item.token, weight)
        
    return graph


def remove_unreachable_nodes(graph):
    for node in graph.nodes():
        if sum(graph.edge_weight((node, other)) for other in graph.neighbors(node)) == 0:
            graph.del_node(node)
