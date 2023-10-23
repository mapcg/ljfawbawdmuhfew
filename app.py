from fastapi import FastAPI
from fastapi.responses import JSONResponse
import os

import json

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/e8dd115e87d2cc44f0e3f640138f6bff")
async def test():
    test = {
	"cameras": [
		{
			"mac": "none",
			"path": "cam",
			"type": "usb"
		},
		{
			"mac": "ab:cd:ef:12:34:56",
			"path": "pc2",
			"type": "rtsp"
		}
	]
}
    return test

