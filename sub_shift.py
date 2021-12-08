import re
import sys

try:
    sec=float(sys.argv[2])
except IndexError:
    print("Not enough agruments inserted - first enter .srt file name then enter seconds")

def convert(seconds):
    min_, sec = divmod(seconds, 60)
    mili=sec-int(sec)
    hour, min_ = divmod(min_, 60)
    return "%02d:%02d:%02d,%03d" % (hour, min_, sec,1000*mili)

with open(sys.argv[1],'r', encoding="utf8") as f:
    content=f.readlines()

content = [x.split('\n') for x in content]
ftr = [3600,60,1,0.001]
for i,row in enumerate(content):
    try:
        row_=row[0].split(' ')       
        tmp=re.search("\d\d:\d\d:\d\d",row_[0]).string
        time1=sum([a*b for a,b in zip(ftr, map(int,re.split(',|:',tmp)))])
        time1+=sec      
        tmp=re.search("\d\d:\d\d:\d\d",row_[2]).string
        time2=sum([a*b for a,b in zip(ftr, map(int,re.split(',|:',tmp)))])
        time2+=sec       
        time1=convert(time1)
        time2=convert(time2)            
        content[i]=time1+" --> "+time2
    except:
       pass

with open(sys.argv[1],'w', encoding="utf8") as f:
    for row in content:
        line=''
        for row2 in row:
            line+=row2
        f.write(line+'\n')

