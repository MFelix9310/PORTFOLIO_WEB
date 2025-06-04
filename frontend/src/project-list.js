import React from 'react';
import { createRoot } from 'react-dom/client';
import ProjectList from './components/ProjectList';

// Obtener el idioma actual
const language = document.documentElement.lang || 'es';

// Inicializar React solo cuando el DOM esté listo
document.addEventListener('DOMContentLoaded', () => {
  const container = document.getElementById('react-projects-container');
  
  if (container) {
    const root = createRoot(container);
    root.render(<ProjectList language={language} />);
  }
}); 