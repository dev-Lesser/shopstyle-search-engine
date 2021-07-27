from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import redis
import datetime
import requests, json
redis_client = redis.StrictRedis(host='redis', port=6379, db=0)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/v1/items/{category}/{sid}/{eid}")
def get_items(category: str, sid: int, eid: int):
    results = redis_client.get('{category}:{sid}_{eid}'.format(category=category, sid=sid, eid=eid))

    if results == None:
        results = requests.get('http://polling_server:3000/api/v1/items/{category}/{sid}/{eid}'.format(category=category, sid=sid, eid=eid))
        return JSONResponse(
            status_code=200,
            content= json.loads(results.content)
        )
        # redis_client.set('{category}:{sid}_{eid}'.format(category=category, sid=sid, eid=eid), results, datetime.timedelta(minutes=1))
    return JSONResponse(
        status_code=200,
        content= json.loads(results)['products']
    )

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=3000)

