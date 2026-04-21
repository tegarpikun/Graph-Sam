import cv2
import numpy as np

def get_line_segments(binary_image):
    # Hitung jumlah piksel hitam (nilai 255) secara horizontal
    # Axis=1 artinya kita menjumlahkan ke samping
    horizontal_projection = np.sum(binary_image, axis=1)
    
    # Cari indeks di mana ada tulisan (jumlah piksel > threshold)
    mask = horizontal_projection > (np.max(horizontal_projection) * 0.05)
    
    # Mencari koordinat awal dan akhir setiap baris
    lines = []
    start_idx = None
    
    for i, val in enumerate(mask):
        if val and start_idx is None:
            start_idx = i
        elif not val and start_idx is not None:
            lines.append((start_idx, i))
            start_idx = None
            
    return lines # Mengembalikan list tuple (y_awal, y_akhir) untuk setiap baris