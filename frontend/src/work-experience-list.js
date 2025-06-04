import React from 'react';
import { createRoot } from 'react-dom/client';
import WorkExperienceList from './components/WorkExperienceList';

// Obtener el idioma actual
const language = document.documentElement.lang || 'es';

// Inicializar React solo cuando el DOM esté listo
document.addEventListener('DOMContentLoaded', () => {
  const container = document.getElementById('react-work-experiences-container');
  
  if (container) {
    const root = createRoot(container);
    root.render(<WorkExperienceList language={language} />);
  }
}); 