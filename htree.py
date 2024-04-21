import json
import networkx as nx
import matplotlib.pyplot as plt

def htree_built(data):
    print("start building graph...")
    G = nx.DiGraph()

    root_node = "ROOT"
    G.add_node(root_node)

    for group, node_stats in data.items():
        G.add_node(group)
        G.add_edge(root_node, group)

        for stat in node_stats:
            parsed = stat.split('NodeStats')
            node_name = f"{parsed[0].strip()[:-1]}_{group}"
            stat_per_node = parsed[1].strip("\n")  
            G.add_node(node_name, label=stat_per_node)
            G.add_edge(group, node_name)

    print("Done.")
    return G

def visual(G):
    pos = nx.spring_layout(G)
    # labels = nx.get_node_attributes(G, 'label')#Dont show labels on the graph
    nx.draw(G, pos, with_labels=True, node_size=500, node_color='skyblue', font_size=5, font_weight='bold')
    plt.show()

if __name__ == "__main__":
    with open('parsed.json', 'r') as file:
        data = json.load(file)
    graph = htree_built(data)
    # print(graph._node)
    visual(graph)