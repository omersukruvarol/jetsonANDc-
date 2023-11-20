from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.post("/8000/")
async def object_detection(file: UploadFile = File(...)):
    contents = await file.read()
    
    # Gelen dosyayı işlemek yerine, sadece mesaj döndürme örneği
    return {"message": "Resim başarıyla alındı ve işleniyor..."}
