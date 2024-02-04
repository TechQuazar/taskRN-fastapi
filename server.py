from fastapi import FastAPI, Request, File, UploadFile, BackgroundTasks
from fastapi.templating import Jinja2Templates
import shutil
import ocr
import os
import uuid
import json
from fastapi.middleware.cors import CORSMiddleware
import firebase_admin
import pyrebase
import json
from  firebase_config import firebase
from pydantic import BaseModel


class Item(BaseModel):
    imageName: str

app = FastAPI()
# Allow all origins for CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
templates = Jinja2Templates(directory="templates")

@app.get("/")
def home(request: Request):
    return {"Hello World!"}

@app.post("/api/v1/ocr")
async def extract_text(item:Item):
    print("Name:",item.imageName)
    storage  = firebase.storage()
    file = 'images/downloaded.jpg'
    
    storage.download(item.imageName,file)
    # text = await ocr.read_image(file)
    data = {}
    data['patient'] = 'Jane Doe'
    data['doctor'] = 'James Wilson'
    data['medicine'] = [{'name':'D2o', 'dose':'1 per week','totaldose':'4'},{'name':'B-blocker', 'dose':'1 per day','totaldose':'7'}]
    data['pharmacyID'] = '1234'
    # After we get results, add to database
    db = firebase.database()
    db.child("prescription").push(data)
    print("Data pushed to firebase")

    return data


# @app.post("/api/v1/extract_text")
# async def extract_text(image: UploadFile = File(...)):
#     print('Image data on server',image)
#     # temp_file = _save_file_to_disk(image, path="temp", save_as="temp")
#     # text = await ocr.read_image(temp_file)
    
#     return {"filename": image.filename, "text": 'Sample OCR from the server'}
