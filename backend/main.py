from fastapi import FastAPI, UploadFile, File
import shutil
import os
from processor.orchestrator import run_full_analysis

app = FastAPI()

@app.post("/analyze")
async def analyze_handwriting(file: UploadFile = File(...)):
    # Simpan file sementara
    temp_path = f"temp_{file.filename}"
    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    # Jalankan mesin grafologi
    result = run_full_analysis(temp_path)
    
    # Hapus file setelah analisis
    os.remove(temp_path)
    
    return result

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
