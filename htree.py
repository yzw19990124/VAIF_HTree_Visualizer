import json
import networkx as nx
import matplotlib.pyplot as plt

def htree_built(data):
    print("start building graph...")
    G = nx.DiGraph()
    level = 0
    limit = len(data)
    for group, node_stats in data.items():
        G.add_node(group, layer = level)
        for stat in node_stats:
            parsed = stat.split('NodeStats')
            node_name = f"{parsed[0].strip()[:-1]}_{group}"
            stat_per_node = parsed[1].strip("\n")  
            G.add_node(node_name, label=stat_per_node, layer=level)
            G.add_edge(group, node_name)
        level += 1

    print("Done.")
    return G

def visual(G):
    pos = nx.multipartite_layout(G, subset_key="layer")
    labels = nx.get_node_attributes(G, 'label')
    nx.draw(G, pos, with_labels=True, node_size=100, node_color='skyblue', font_size=2, font_weight='bold')
    print("Done.")
    plt.show()

if __name__ == "__main__":
    with open('parsed.json', 'r') as file:
        data = json.load(file)
    graph = htree_built(data)
    # print(graph._node)
    visual(graph)