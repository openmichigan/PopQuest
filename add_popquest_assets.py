import json
from collections import OrderedDict

question_file = "questionfile_example.txt" # put the filename of the PLAIN TEXT file of your questions here
videourl_file = "videourl.txt" # make a file called videourl.txt with the appropriate URL of the videourl

qu = open(question_file, "r")
vf = open(videourl_file, "r")

questions_dict = {}

questions = qu.read()
ql = questions.split("\n\n")
nums = range(1,len(ql)+1)

allmats = zip(nums, ql)
for q in allmats:
	ques_items = q[1].split("\n")
	if q[0] not in questions_dict:
		for i in ques_items[1:]:
			if "*" in i:
				correct = i.replace("*","")
		answers = [x.replace("*","") for x in ques_items[1:]]

		questions_dict[q[0]] = {"num":q[0], "text":ques_items[0], "correct":correct, "answers":answers}

questions_dict = OrderedDict(sorted(questions_dict.items(), key=lambda x:int(x[1]["num"])))
#print questions_dict

# take care of video asset, small json file
## TODO: validate video URL/path
url = vf.read().strip()
video_asset = {"url":url}

with open("questions.json", 'w') as outfile:
	json.dump(questions_dict, outfile)

with open("video.json", 'w') as outfile:
	json.dump(video_asset,outfile)

