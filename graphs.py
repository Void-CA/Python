import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

df = pd.read_csv('example.csv')

G = nx.from_pandas_edgelist(df, source='origen', target='destino', edge_attr='peso', create_using=nx.DiGraph())

plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G, seed=42)

edge_labels = nx.get_edge_attributes(G, 'peso')
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2500, edge_color='black', arrows=True,
        font_size=10, font_color='black', font_weight='bold', edgecolors='black', linewidths=1)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='darkblue')

plt.title('Grafo de Conexiones', fontsize=12)
plt.tight_layout()
plt.savefig('grafo_pesos.png', dpi=300)
plt.show()
