from fastapi import FastAPI, File, UploadFile
from models.schema import LabTestResponse
from utils.ocr_processor import process_image
from utils.parser import extract_lab_tests

app = FastAPI()

@app.post("/get-lab-tests", response_model=LabTestResponse)
async def get_lab_tests(image: UploadFile = File(...)):
    try:
        raw_text = process_image(image.file)
        lab_data = extract_lab_tests(raw_text)

        return {
            "is_success": True,
            "data": lab_data
        }
    except Exception as e:
        return {
            "is_success": False,
            "data": [],
            "error": str(e)
        }
