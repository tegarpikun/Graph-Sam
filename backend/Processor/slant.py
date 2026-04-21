import cv2
import numpy as np
import matplotlib.pyplot as plt

def analyze_slant(image_path):
    # 1. Load gambar dan konversi ke grayscale
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # 2. Binarization (Otsu's Thresholding)
    # Menghasilkan gambar hitam putih bersih
    _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    
    # 3. Skeletonization (Opsional tapi disarankan)
    # Mengecilkan stroke untuk melihat struktur garis
    kernel = np.ones((3,3), np.uint8)
    skeleton = cv2.erode(binary, kernel, iterations=1)
    
    # 4. Probabilistic Hough Line Transform
    # Mendeteksi garis-garis imajiner pada goresan huruf
    lines = cv2.HoughLinesP(skeleton, 1, np.pi/180, threshold=50, minLineLength=20, maxLineGap=5)
    
    angles = []
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            # Hitung sudut dalam derajat
            angle = np.rad2deg(np.arctan2(y2 - y1, x2 - x1))
            
            # Kita hanya tertarik pada garis vertikal (huruf 'l', 't', 'b', dsb)
            # Biasanya antara 60 sampai 120 derajat
            if 60 < abs(angle) < 120:
                angles.append(angle)
    
    avg_slant = np.mean(angles) if angles else 0
    return avg_slant

# Contoh Penggunaan
slant_result = analyze_slant('handwriting_sample.png')
print(f"Rata-rata kemiringan tulisan: {slant_result:.2f} derajat")