import networkx as nx
import matplotlib.pyplot as plt

# Create graph
G = nx.Graph()

# Add nodes and relationships
G.add_edge("Goa", "Beach")
G.add_edge("Manali", "Mountain")
G.add_edge("Jaipur", "Historical")

G.add_edge("Goa", "Seafood")
G.add_edge("Manali", "Snow")
G.add_edge("Jaipur", "Fort")

# Draw graph
plt.figure(figsize=(6,6))
nx.draw(G, with_labels=True, node_color='lightblue', node_size=2000, font_size=10)
plt.title("Knowledge Graph of Tourist Places")

plt.savefig("graph.png")
plt.show()
