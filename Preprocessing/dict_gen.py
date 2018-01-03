''' Dictionary Generation- through array ''' 
import time
start = time.time()


from nltk import edit_distance
reader= open('neww.txt', 'r');
reader2=open('neww.txt', 'r');

wd=dict();
x=0
z=[0,0,0,0,0]
'''for words in reader:
  for word in words.split():
         l=len(word)
         if(l==3): z[0]+=1;
	 elif(l==4):z[1]+=1; 
	 elif(l==5):z[2]+=1; 
	 elif(l==6):z[3]+=1;
         else:++z[4];
z[1]+=z[0];
z[2]+=z[1];
z[3]+=z[2];
z[4]+=z[3];
print(z[0]);
print(z[1]);
print(z[2]);
reader.seek(0,0);
dd=0;
for words in reader:
  for word in words.split():
	wd[word]=[];dd=0;
        #x=x+1;
        #reader2.seek(x,0);
	for listofwordss in reader2:
           for listofwords in listofwordss.split():
		dd=dd+1;
                if(x<z[0] and dd>z[1]):
			reader2.seek(x+1,0);
		elif((x>z[0] and x<z[1])and dd>z[2]):
			reader2.seek(x+1,0);
		elif((x>z[1] and x<z[2])and dd>z[3]):
			reader2.seek(x+1,0);
		elif((x>z[2] and x<z[3])and dd>z[4]):
			reader2.seek(x+1,0);
                else:
                    e=edit_distance(str(word),str(listofwords));
		    if(e==1):	
			 wd[word].append(listofwords);
                    reader2.seek(x+1,0);
'''
a=[];
'''for words in reader:
  for word in words.split():
	#x=x+1;
	l1=len(word);
	wd[word]=[];
	for listofwordss in reader2:
           for listofwords in listofwordss.split():
		l2=len(listofwords);
		if((l2-l1)>1):
			x=x+1;
			reader2.seek(x,0);
		else:
			e=edit_distance(str(word),str(listofwords));
		        if(e==1):	
			    wd[word].append(listofwords);	'''	


      
	  
for words in reader:
  for word in words.split():
		a.append(word);

print ("done appending");

s=0;z=4;
for i in range(0,len(a)):
	wd[a[i]]=[];
	l1=len(a[i]);
	s=0;
	if(l1==z): 
             print("done")
             print(time.time()-start);
             z=z+1
	for j in range(i,len(a)):
		if(len(a[j])-l1>1):
			s=1;
			break;
		else:
			e=edit_distance(str(a[i]),str(a[j]));
		        if(e==1):	
			    wd[a[i]].append(a[j]);
	#if(s==1):
		#break;





 			


import pickle
with open("ed_neww.txt", "wb") as fp:   #Pickling
  pickle.dump(wd, fp)

print(time.time()-start)
with open("ed_neww.txt", "rb") as fp:   # Unpickling
  b = pickle.load(fp)

        
#print(b)            
