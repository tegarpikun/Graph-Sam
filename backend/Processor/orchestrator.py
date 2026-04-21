import cv2
import numpy as np
# Pastikan path import sesuai dengan struktur folder Anda
from .slant import analyze_slant
from .segmentation import get_line_segments
from .baseline import analyze_baseline

def run_full_analysis(image_path):
    # 1. Analisis Slant (panggil fungsi dari slant.py)
    # Fungsi ini sudah melakukan imread sendiri di dalamnya
    slant_score = analyze_slant(image_path)
    
    # 2. Preprocessing manual untuk Baseline & Segmentation
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Gunakan Otsu Thresholding untuk memisahkan tulisan dari background
    _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    
    # 3. Analisis Baseline (Arah Baris)
    line_coords = get_line_segments(binary)
    baselines = []
    
    for (start, end) in line_coords:
        line_img = binary[start:end, :] # Memotong gambar hanya pada area baris tersebut
        slope = analyze_baseline(line_img)
        baselines.append(slope)
    
    avg_baseline = np.mean(baselines) if baselines else 0
    
    # 4. Mapping Interpretasi Psikologis
    # Slant > 90 derajat biasanya miring ke kanan (ekspresif)
    personality = {
        "emotional_type": "Ekspresif/Emosional" if slant_score > 90 else "Logis/Introvert",
        "mood_tendency": "Optimis/Bersemangat" if avg_baseline > 0.01 else "Stabil/Tenang"
    }
    
    return {
        "raw_data": {
            "slant": float(slant_score), 
            "baseline": float(avg_baseline)
        },
        "interpretation": personality
    }