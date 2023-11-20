from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.post("/predict/")
async def object_detection(file: UploadFile = File(...)):
    contents = await file.read()
    
    # Gelen dosyayı işlemek yerine, sadece mesaj döndürme örneği
    return {"message": "Resim başarıyla alındı ve işleniyor..."}
    
if __name__ == "__main__":
    import uvicorn

    # Start the FastAPI application
    uvicorn.run(app, host="192.168.1.2", port=8000)
