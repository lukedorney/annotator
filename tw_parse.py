import json
"""takes twitter data created by tw_collect.py in json format
 and makes it human readable"""

"""input file containing data in json format """
with open("EMOTIONLESS_FACE_data.txt", 'annotations', encoding='utf-8') as input_file:
    tweets = input_file.readlines()
tweets = [json.loads(line) for line in tweets]
"""output file in the format:
    tweet
    user
    
"""
with open("EMOTIONLESS_FACE_text.txt", "w", encoding='utf-8') as f:
    for tweet in tweets:
        f.write(tweet['text'] + '\n@' + tweet['user']['screen_name'] + '\n\n')
"""count how many tweets we made it through"""
x = 0
for tw in tweets:
    x += 1
    print(tw['text'], '\n@', tw['user']['screen_name'])
print(x)
