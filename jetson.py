from fastapi import FastAPI, File, UploadFile
from ultralytics import YOLO

app = FastAPI()

@app.post("/predict/")
model = YOLO('best.pt')
async def predict(image: bytes):
    # Convert the image bytes to a PIL Image
    image = Image.open(io.BytesIO(image))

    # Make the prediction using YOLOv5
    predictions = model(image)

    # Convert the predictions to a byte array
    prediction_bytes = predictions.toImage().tobytes()

    return prediction_bytes
    
if __name__ == "__main__":
    import uvicorn

    # Start the FastAPI application
    uvicorn.run(app, host="192.168.1.2", port=8000)
