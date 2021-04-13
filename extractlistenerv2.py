import sys
import os
import re
#import os.path

toolsname='Listener Log Extractor'
createdby='Created by Wahyu Joko Raharjo/ wahyu.jraharjo@gmail.com  (c)2017'

def usage():
	print (toolsname)
	print (createdby)
	print (' ')
	print ('Usage:')
	print ('python',sys.argv[0],'[listener_log_file] [output_file]')
	print (' ')

	
#print (sys.argv)
#print (sys.argv[2:]) 
if len(sys.argv)!=3 :
	usage() 
	sys.exit(0)

print (toolsname)
print (createdby)	
	
cwd = os.getcwd()
infile=sys.argv[1]
outfile=sys.argv[2]

if os.path.isfile(infile)!=True :
	input_file= os.path.join(cwd,infile)
else:
	input_file=infile
	
output_file=os.path.join(cwd,outfile)

if os.path.isfile(input_file)!=True :
	print (input_file, 'file not found, exit')
	sys.exit(0)
	
getinFile=open(input_file,"r")
getoutFile=open(output_file,"w")

buffer = []
#keepCurrentSet = True

regex=re.compile('\\bSERVICE_NAME\\b')
pl=0
pr=0
p1=0
p2=0

waktu=''
sid=''
program=''
hostname=''
user=''
ipaddr=''
port=''

#str.find(str, beg=0, end=len(string))
for line in getinFile:
    #.findall('\\bCONNECT_DATA\\b',line)
    if bool(regex.search(line))==True : #diolah disini
        #print line
        
        #waktu
        pl=line.find(' *')
        # <txt> after this line
        waktu=line[6:pl]
        pr=pl+len(' *')
        
        #SERVICE_NAME #var2[1:5]
        pl=line.find('SERVICE_NAME=',pr)
        p1=pl+len('SERVICE_NAME=')
        pr=pl
        pl=line.find(')',pr)
        p2=pl
        pr=pl
        
        sid=line[p1:p2]
        #print (sid)
        
        #PROGRAM
        pl=line.find('PROGRAM=',pr)
        p1=pl+len('PROGRAM=')
        pr=pl
        pl=line.find(')',pr)
        p2=pl
        pr=pl
        
        program=line[p1:p2]
        #print(program)
        
        #HOST	#hostname
        pl=line.find('HOST=',pr)
        p1=pl+len('HOST=')
        pr=pl
        pl=line.find(')',pr)
        p2=pl
        pr=pl
        
        hostname=line[p1:p2]
        #print(hostname)
        
        #USER
        pl=line.find('USER=',pr)
        p1=pl+len('USER=')
        pr=pl
        pl=line.find(')',pr)
        p2=pl
        pr=pl
        
        user=line[p1:p2]
        #print(user)
        
        #HOST
        pl=line.find('HOST=',pr)
        p1=pl+len('HOST=')
        pr=pl
        pl=line.find(')',pr)
        p2=pl
        pr=pl
        
        ipaddr=line[p1:p2]
        #print(ipaddr)
        
        #PORT  #clientport
        pl=line.find('PORT=',pr)
        p1=pl+len('PORT=')
        pr=pl
        pl=line.find(')',pr)
        p2=pl
        pr=pl
        
        port=line[p1:p2]
        #print(port)
        
        buffer.append(waktu+';'+sid+';'+program+';'+hostname+';'+user+';'+ipaddr+';'+port+"\n")
        str=""
        getoutFile.write(str.join(buffer))
        buffer = []
    
getinFile.close()
getoutFile.close()

print ('')
print ('Output saved to ',output_file)
print ('')

