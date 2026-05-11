import os

from fastapi import FastAPI
from fastapi import UploadFile
from fastapi import File

from app.graph.workflow import app_graph


app = FastAPI()


UPLOAD_FOLDER = "app/uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.post("/analyze")


async def analyze_report(file: UploadFile = File(...)):

    file_path = f"{UPLOAD_FOLDER}/{file.filename}"

    with open(file_path, "wb") as f:
        f.write(await file.read())


    result = app_graph.invoke({
        "file_path": file_path
    })

    return result