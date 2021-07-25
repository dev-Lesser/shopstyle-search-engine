import pymongo
import requests
from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import json
import redis
import datetime

redis_client = redis.StrictRedis(host='redis', port=6379, db=0)


client = pymongo.MongoClient('mongodb://mongodb:27017')
db = client.attrfashion
collection = db.shopstyle_test
SHOPSTYLE_URL = "https://www.shopstyle.com/api/v2/products"


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/v1/items/{category}/{sid}/{eid}")
def get_items_from_api(category: str, sid: int, eid: int):
    params = {
        "includeProducts": "true",
        "limit" : eid-sid,
        "pid": "shopstyle", # pid 필수
        "offset": sid,
        "cat": category
    }
    results = requests.get(SHOPSTYLE_URL, params=params)
    results = json.loads(results.content)

    if 'id_1' not in [i['name'] for i in collection.list_indexes()]:# id 인덱스 생성
        collection.create_index([('id', 1)])
    redis_client.set('{category}:{sid}_{eid}'.format(category=category, sid=sid, eid=eid), json.dumps(results), datetime.timedelta(minutes=5))
    for item in results['products']:
        check_id = item['id']
        collection.update({'id': check_id},item, upsert=True)
    return JSONResponse(
        status_code=200,
        content= results['products']
    )

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=3000)

