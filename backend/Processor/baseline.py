from sklearn.linear_model import LinearRegression

def analyze_baseline(line_img):
    # Cari semua koordinat piksel hitam
    coords = np.column_stack(np.where(line_img > 0))
    
    # Kita fokus pada titik terbawah (y) untuk setiap x
    # Ini penyederhanaan: ambil sampel titik untuk regresi
    x = coords[:, 1].reshape(-1, 1)
    y = coords[:, 0]
    
    model = LinearRegression().fit(x, y)
    slope = model.coef_[0] # Ini adalah kemiringan garis (optimisme/pesimisme)
    
    return slope