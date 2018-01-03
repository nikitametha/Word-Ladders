 
 ''' Graph conversion '''
 
import pickle

reader= open('neww.txt', 'r');
with open("ed_neww.txt", "rb") as fp:   # Unpickling
   b = pickle.load(fp)




import networkx as nx
net = nx.Graph()
for words in reader:
  for word in words.split():

	net.add_node(word);


for k,v in b.iteritems():
    for v_i in v:
        net.add_edge(k,v_i)


w1 = raw_input("Start Word: ")
w2 = raw_input("End Word:   ")
print(nx.shortest_path(net, w1, w2)) 

