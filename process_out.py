import codecs
fi=codecs.open("out.txt","r",encoding="utf-8")
f=fi.read()
fi.close()
f=f.split("\n")
a=[]
myDic={'series & tv': 0, 'books': 0, 'movies': 0, 'other': 0, 'music': 0, 'anime': 0, 'games': 0, 'software': 0, 'adult': 0}

for ii,i in enumerate(f):
	#if i not in a:
	if ii!=len(f)-1:
		myDic[str(i)]=myDic[str(i)]+1
#	print str(i)+" "+str(myDic[str(i)])
print myDic
#	myDic[str(i)]=myDic[str(i)]+1
#		a.append(i)
#freq=[0]*len(a)
#myDic = {}
#print a
#for i,lista in enumerate(a):
#	if i!=len(a)-1:
#		print lista
#		myDic[lista] = 0
#print myDic
#for i in f:
#	myDic[i]=myDic[i]+1
#print myDic
#for i in range(len(a)):
#	b[i]=0
