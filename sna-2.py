import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd

names = ['botterill', 'beane', 'mcquaid', 'girardi', 'polak', 'engelland', 'botts', 'krueger', 'risto', 'olofsson', 'reinhart', 'miller'
         'vesey', 'scandella', 'montour', 'lazar', 'rodrigues', 'hutton', 'ullmark', 'sheary', 'jokiharju']

threads = ['thread_goaltending.csv', 'thread_jason botterill.csv', 'thread_sabres tickets.csv', 'thread_speculation opening night.csv']
messages = [0]*4

def create_sna_graph(message, thread_title):
    t_names = []
    # for message in messages:
    temp_l = []
    for i in range(len(message)-2):
        s = ":".join(message[i:i+1])
        for name in names:
            if name in s.lower():
                temp_l.append(name)
        t_names.append(temp_l)
        temp_l = []

    print(t_names)

    G_weighted = nx.Graph()

    for l in t_names:
        for i in range(len(l) - 1):
            for j in range(i + 1, len(l)):
                G_weighted.add_edge(l[i], l[j], weight=1)

    #
    # for i in range(len(t1_names)-1):
    #     for j in range(i+1,len(t1_names)):
    #         G_weighted.add_edge(t1_names[i], t1_names[j], weight=1)

    nx.draw_networkx(G_weighted)

    plt.show()
    plt.savefig(thread_title[:len(thread_title)-3]+'.png')
    # plt.close()

for i,thread in enumerate(threads):
    df = pd.read_csv(thread)
    create_sna_graph(list(df['Messages']), thread)



