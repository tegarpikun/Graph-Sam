import React, { useState } from 'react';
import axios from 'axios';
import { Upload, Activity, CheckCircle, AlertCircle } from 'lucide-react';
import { motion } from 'framer-motion';

function App() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleUpload = async () => {
    if (!file) return;
    setLoading(true);
    const formData = new FormData();
    formData.append('file', file);

    try {
      // Menghubungkan ke endpoint FastAPI yang telah Anda buat
      const response = await axios.post('http://127.0.0.1:8000/analyze', formData);
      setResult(response.data);
    } catch (error) {
      console.error("Error uploading file", error);
      alert("Gagal menganalisis gambar.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-slate-50 p-8 font-sans text-slate-900">
      <header className="max-w-4xl mx-auto mb-12 text-center">
        <h1 className="text-4xl font-bold mb-2">GraphoAI Analyzer</h1>
        <p className="text-slate-500">Identifikasi Kepribadian Melalui Tulisan Tangan</p>
      </header>

      <main className="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8">
        {/* Kolom Upload */}
        <section className="bg-white p-6 rounded-2xl shadow-sm border border-slate-200">
          <div className="border-2 border-dashed border-slate-300 rounded-xl p-8 text-center">
            <input 
              type="file" 
              onChange={(e) => setFile(e.target.files[0])} 
              className="hidden" 
              id="fileInput"
            />
            <label htmlFor="fileInput" className="cursor-pointer">
              <Upload className="mx-auto mb-4 text-blue-500" size={48} />
              <p className="font-medium">{file ? file.name : "Pilih Foto Tulisan Tangan"}</p>
            </label>
          </div>
          <button 
            onClick={handleUpload}
            disabled={!file || loading}
            className="w-full mt-6 bg-blue-600 text-white py-3 rounded-lg font-semibold hover:bg-blue-700 disabled:bg-slate-300 transition"
          >
            {loading ? "Menganalisis..." : "Mulai Analisis"}
          </button>
        </section>

        {/* Kolom Hasil */}
        <section className="bg-white p-6 rounded-2xl shadow-sm border border-slate-200">
          <h2 className="text-xl font-bold mb-6 flex items-center gap-2">
            <Activity size={20} /> Hasil Analisis
          </h2>
          {result ? (
            <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }}>
              <div className="mb-6 p-4 bg-blue-50 rounded-lg">
                <p className="text-sm text-blue-600 font-bold uppercase tracking-wider">Tipe Emosional</p>
                <p className="text-2xl font-semibold">{result.interpretation.emotional_type}</p>
              </div>
              <div className="mb-6 p-4 bg-green-50 rounded-lg">
                <p className="text-sm text-green-600 font-bold uppercase tracking-wider">Kecenderungan Mood</p>
                <p className="text-2xl font-semibold">{result.interpretation.mood_tendency}</p>
              </div>
              <div className="text-xs text-slate-400">
                Raw Data: Slant {result.raw_data.slant.toFixed(2)}° | Baseline {result.raw_data.baseline.toFixed(4)}
              </div>
            </motion.div>
          ) : (
            <div className="h-48 flex items-center justify-center text-slate-400 border border-dashed rounded-xl">
              Hasil akan muncul di sini
            </div>
          )}
        </section>
      </main>
    </div>
  );
}

export default App;