import React, { useState } from 'react';

const ProjectCard = ({ project, language }) => {
  const [showDescription, setShowDescription] = useState(false);
  const [showImage, setShowImage] = useState(false);
  
  const title = language === 'en' && project.title_en ? project.title_en : project.title;
  const description = language === 'en' && project.description_en ? project.description_en : project.description;
  const technologies = language === 'en' && project.technologies_en ? project.technologies_en : project.technologies;
  
  const skills = project.skills ? project.skills.split(',').map(skill => skill.trim()) : [];
  
  const getSkillDisplay = (skill) => {
    switch(skill) {
      case 'data_scientist':
        return 'Data Scientist';
      case 'data_analyst':
        return 'Data Analyst';
      case 'python_developer':
        return 'Python Developer';
      default:
        return skill;
    }
  };
  
  return (
    <div className="project-card h-100">
      <div className="project-card-header">
        <h4>{title}</h4>
        <p className="mb-0">{technologies}</p>
        
        {skills.length > 0 && (
          <div className="mt-2">
            {skills.map((skill, index) => (
              <span key={index} className="category-badge">
                {getSkillDisplay(skill)}
              </span>
            ))}
          </div>
        )}
      </div>
      
      <div className="project-card-body">
        <div className="d-flex flex-wrap gap-2 mb-3">
          <button 
            className={`btn btn-sm btn-orange btn-toggle ${showDescription ? 'active' : ''}`}
            onClick={() => setShowDescription(!showDescription)}
          >
            {language === 'en' ? 'Description' : 'Descripción'}
          </button>
          
          <button 
            className={`btn btn-sm btn-orange btn-toggle ${showImage ? 'active' : ''}`}
            onClick={() => setShowImage(!showImage)}
          >
            {language === 'en' ? 'Image' : 'Imagen'}
          </button>
          
          <a href={`/portfolio/projects/${project.id}`} className="btn btn-sm btn-orange">
            {language === 'en' ? 'Details' : 'Detalles'}
          </a>
          
          {project.github_url && (
            <a href={project.github_url} target="_blank" rel="noopener noreferrer" className="btn btn-sm btn-orange">
              GitHub
            </a>
          )}
          
          {project.project_url && (
            <a href={project.project_url} target="_blank" rel="noopener noreferrer" className="btn btn-sm btn-orange">
              {language === 'en' ? 'Demo' : 'Demo'}
            </a>
          )}
        </div>
        
        <div id={`image-${project.id}`} className={`project-image-container ${showImage ? 'active' : ''}`}>
          {project.thumbnail && (
            <img src={project.thumbnail} alt={title} className="img-fluid rounded" />
          )}
        </div>
        
        <div id={`description-${project.id}`} className={`project-description ${showDescription ? 'active' : ''}`}>
          <p>{description}</p>
        </div>
      </div>
    </div>
  );
};

export default ProjectCard; 