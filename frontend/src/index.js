import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css'; // Pastikan file CSS ini ada untuk Tailwind
import App from './App';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
