import json
import settings

TOPICS = json.loads(open(settings.DATA_PATH + "topics.json").read())
NODE_CACHE = json.loads(open(settings.DATA_PATH + "nodecache.json").read())
EXERCISE_TOPICS = json.loads(open(settings.DATA_PATH + "maplayout_data.json").read())