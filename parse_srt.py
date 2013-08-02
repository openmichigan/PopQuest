import json
from collections import OrderedDict

## for usual timestamp; we want pure seconds
# SECOND = 1000
# MINUTE = 60 * SECOND
# HOUR = 60 * MINUTE

##

def parseTime(timeStr):
    chunks = timeStr.split(":")
    secondCh = chunks[2].split(",")
    hours = int(chunks[0],10)
    minutes = int(chunks[1],10)
    seconds = int(secondCh[0],10)
    #millisecs = int(secondCh[1],10)
    return hours*3600 + minutes*60 + seconds
    #return "%s%s%s" % (HOUR*hours,MINUTE*minutes,SECOND*seconds)

f = open("captions.srt", "r")
fl = f.read()
bits = fl.split("\n\n")

a = 0
objs = []
for b in bits:
    bitsep = b.split("\n")
    a += 1
    obj = {}
    if len(bitsep) >= 2:
        obj["num"] = bitsep[0]
        #print obj["num"]
        obj["seconds"] = parseTime(bitsep[1]) # seconds into video
        obj["content"] = " ".join(bitsep[2:])
        objs.append(obj)

total_dict = {}
for ob in objs:
    if ob["num"] not in total_dict:
        total_dict[ob["num"]] = ob
#print total_dict

total_dict = OrderedDict(sorted(total_dict.items(),key=lambda it:int(it[1]["num"])))
print total_dict
# with open('captions.json', 'w') as outfile:
#     json.dump(total_dict, outfile)

