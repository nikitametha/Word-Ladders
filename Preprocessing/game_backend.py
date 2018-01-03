'''ALL SHORTEST PATHS..COMP GENERATES THE GAME'''




import pickle
import random

reader= open('neww.txt', 'r');
with open("ed_words_neww.txt", "rb") as fp:   # Unpickling
   b = pickle.load(fp)


a=[];

import networkx as nx
net = nx.Graph()
for words in reader:
  for word in words.split():
        a.append(word);  
	net.add_node(word);


for k,v in b.iteritems():
    for v_i in v:
        net.add_edge(k,v_i)
x=0
ll=[]


print("WELCOME ");
print("SELECT DIFFICULTY ");
print("LEVEL: 1 (HARD) ");
print("LEVEL: 2 (EASY)");
inp=raw_input("TYPE 1 OR 2: ");
if(inp=="1"): inp="ONE";
if(inp=="2"): inp="TWO";


#DIFFICULTY LEVEL MAX--any length
if(inp=="ONE"):
    while True:
	try:
    		f1=random.choice(a );
    		f2=random.choice(a );
   	 	ll=nx.shortest_path(net, f1, f2)
    		print("Start Word: ",f1)
    		print("End Word: ",f2)
	except nx.NetworkXNoPath:
    		continue
	break


#DIFFICULTY LEVEL EASY-- SELECT THE LENGTH OF WORD LIST TO BE USED
if(inp=="TWO"):
   xx=raw_input("Enter word length (3 - 7): "); xx=int(xx);
   #dww=1;
   lst=[];
   for i in a:
     if(len(i)==xx):
        lst.append(i);		



   while True:
	try:
    			f1=random.choice( lst );
    			f2=random.choice( lst );
		
  		 	ll=nx.shortest_path(net, f1, f2)
  		  	print("Start Word: ",f1)
  		  	print("End Word: ",f2)
	except nx.NetworkXNoPath:
    		continue
	break



g=[]
rr=1;
print("Type 1 to give up");
print("Make the bridge!");
t=raw_input();


while(g!=ll):
      if(t=="1"):
             print(ll);
	     break;
     
      if (t in ll):
         g.append(t)
	 rr=rr+1;
	 print("Correct!");
      else:
	 #print("Hint");
	 if(len(ll[rr-1])<len(ll[rr])):
			print("Try again! Add a letter!");
	 elif(len(ll[rr-1])>len(ll[rr])):
			print("Try again! Delete a letter");
	 else:
			print("Try again! Change a letter!");
 		

         x=x+1
      
      t=raw_input();
     





