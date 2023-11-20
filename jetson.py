from fastapi import FastAPI, File, UploadFile
from ultralytics import YOLO
from PIL import Image
import io

model = YOLO('best (4).pt')
app = FastAPI()

@app.post("/predict/")
async def predict(image: bytes):
    try:
        # Convert the image bytes to a PIL Image
        image = Image.open(io.BytesIO(image))

        # Make the prediction using YOLOv5
        predictions = model(image)

        # Convert the predictions to a byte array
        prediction_bytes = predictions.render().tobytes()

        return prediction_bytes
    except Exception as e:
        return {"error": str(e)}  # Handle any exceptions and return an error message

if __name__ == "__main__":
    import uvicorn

    # Start the FastAPI application
    uvicorn.run(app, host="192.168.1.2", port=8000)
