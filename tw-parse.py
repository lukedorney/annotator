import json
"""takes twitter data created by tw-collect.py in json format
 and makes it human readable"""

"""input file containing data in json format """
twitter = open('SMIRKING_FACE-d.txt', 'r')

tweets = []
"""output file in the format:
    tweet
    user
    
"""
fi = open("SMIRKING_FACE-t.txt", "w")

for line in twitter:
    try:
        js = json.loads(line)
        tweets.append(js)
    except:
        continue
"""count how many tweets we made it through"""
x = 0
for tw in tweets:
    try:
        x+=1
        print (tw['text'])
        print("@" + tw['user']['screen_name'])
        print('\n\n')
    except:
        print ("failed")
        continue
print (x)
          
