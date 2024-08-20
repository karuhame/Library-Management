from fastapi import FastAPI, HTTPException, Query
from typing import List, Dict, Optional, Annotated

from config.database import accounts_collection
from routes.account import accountRouter

app = FastAPI()

app.include_router(accountRouter)

@app.get("/blog/{id}")
# id: from path, limit: from query   
async def get_status(id: int, limit: Annotated[str | None, Query(min_length=3, max_length=50)] = None):
    return {"data": id, "limit": limit}

@app.get("/blog")
async def get_status():
    return {"data": 100}


