import codecs
#fi=codecs.open("torrents_mini.csv")
#fsa=fi.read()
#fi.close()
import re
fi=codecs.open("out.txt","w",encoding='utf-8')

f = open('subset.txt')
def read1k():
    return f.read(1024)
#fsa=fsa.split("\n")
#for piece in fsa:

#for piece in iter(read1k, ''):
    #process_data(piece)


f = open("torrents_mini.csv")
for line in f:
	for i in f:
		#print i.split("|")[0]
		if '|' in i:
			ta=i.split("|")


			if str(i)=='"' or str(i)=="":
				#print "gogo"
				continue
			#if re.search('|',i):
			#	continue
			la=ta[len(ta)-3]
			la=la.replace('"','')
			fi.write(la+"\n")
fi.close()