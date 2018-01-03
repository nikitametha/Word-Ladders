

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
x=[]
ll=[]
#print("Made");
ll2=[]
from flask import Flask,request, render_template
app = Flask(__name__)

@app.route("/")
def index():
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
	x=[];
	x.append(f1);
	x.append(f2);
        leng=len(ll);
        ll2=" ".join(ll);

        return render_template("hello2.html",x=x,leng=leng,ll=ll2);

@app.route('/result',methods = ['POST', 'GET'])
def result():
      result = request.form
      res=[]; res2=1;
      w1=(result['start'])
      w2=(result['end'])
      if(w1 in a and w2 in a):
          try: res=nx.shortest_path(net, w1, w2);
          except nx.NetworkXNoPath: res2=-1;
      else: res2=0;
      leng=len(res);
      res1=(res);
      
      return render_template("result.html",res1 = res1, res2=res2)

if __name__ == '__main__':
   app.run(debug = True)
