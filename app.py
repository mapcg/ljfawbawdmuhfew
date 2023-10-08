from fastapi import FastAPI
from fastapi.responses import JSONResponse
import os

import json

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/teste")
async def test():
    test = {
	"cameras": [
		{
			"mac": "d8:36:5f:42:28:06",
			"path": "pc1"
		},
		{
			"mac": "abcdef",
			"path": "pc2"
		}
	]
}
    return test

