import requests
import json
from random import randint

# sub: name of sub; sortby: top, new 
def get_feed(sub, sortby):
    imgur_feed = "http://imgur.com/r/{}/{}.json"
    req_url = imgur_feed.format(sub, sortby)
    res = requests.get(req_url).text

    return json.loads(res)

img_collection = []

subs = ["aww", "food"] # Add subs to pull from

for sub in subs:
    feed = get_feed(sub, "new")

    if not feed["success"]:
        print "An error occurred with the current sub."

    data = feed["data"]

    for d in data:
        img_collection.append(d)

rand_img = img_collection[randint(0, len(img_collection) - 1)]
img_url = "http://i.imgur.com/{}{}".format(rand_img["hash"], rand_img["ext"])
print img_url
