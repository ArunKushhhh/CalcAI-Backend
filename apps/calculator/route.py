from fastapi import APIRouter, HTTPException
import base64
from io import BytesIO
from apps.calculator.utils import analyze_image
from schema import ImageData
from PIL import Image
import logging

router = APIRouter()

@router.post("")
async def run(data: ImageData):
    try:
        # Validate base64 image data
        if not data.image or "," not in data.image:
            raise HTTPException(status_code=400, detail="Invalid image data format")
        
        # Decode and process image
        image_data = base64.b64decode(data.image.split(",")[1])
        image_bytes = BytesIO(image_data)
        image = Image.open(image_bytes)

        # Analyze image
        responses = analyze_image(image, dict_of_vars=data.dict_of_vars)
        
        if not responses:
            return {
                "message": "No mathematical expressions detected",
                "type": "warning",
                "data": []
            }
        
        data_list = []
        for response in responses:
            data_list.append(response)

        return {
            "message": "Image processed successfully",
            "type": "success",
            "data": data_list
        }
        
    except Exception as e:
        logging.error(f"Error processing image: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error processing image: {str(e)}")