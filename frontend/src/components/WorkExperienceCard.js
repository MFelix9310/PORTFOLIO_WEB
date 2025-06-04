import React from 'react';

const WorkExperienceCard = ({ experience, language }) => {
  const company = language === 'en' && experience.company_en ? experience.company_en : experience.company;
  const position = language === 'en' && experience.position_en ? experience.position_en : experience.position;
  const description = language === 'en' && experience.description_en ? experience.description_en : experience.description;
  const keywords = language === 'en' && experience.keywords_en ? experience.keywords_en : experience.keywords;
  
  const skills = experience.skills ? experience.skills.split(',').map(skill => skill.trim()) : [];
  
  // Formatear fecha legible
  const formatDate = (dateString) => {
    if (!dateString) return '';
    
    const date = new Date(dateString);
    const options = { year: 'numeric', month: 'long' };
    return date.toLocaleDateString(language === 'en' ? 'en-US' : 'es-ES', options);
  };
  
  // Determinar si mostrar descripción truncada
  const truncatedDescription = description.length > 150 
    ? description.substring(0, 150) + '...' 
    : description;
  
  return (
    <div className="work-card h-100">
      <div className="work-card-header">
        <div className="work-company">
          {experience.company_logo && (
            <img src={experience.company_logo} alt={company} className="company-logo" />
          )}
          <h4 className="work-company-name">{company}</h4>
        </div>
        
        <h5 className="work-title">{position}</h5>
        
        <p className="work-dates">
          <i className="far fa-calendar-alt me-2"></i>
          {formatDate(experience.start_date)} - {' '}
          {experience.current_job 
            ? (language === 'en' ? 'Present' : 'Actualidad')
            : formatDate(experience.end_date)
          }
        </p>
        
        {skills.length > 0 && (
          <div className="mt-2">
            {skills.map((skill, index) => (
              <span key={index} className="work-skill">{skill}</span>
            ))}
          </div>
        )}
      </div>
      
      <div className="work-card-body">
        <div className="work-description">
          {truncatedDescription}
        </div>
        
        <div className="text-center mt-3">
          <a href={`/portfolio/experience/${experience.id}`} className="btn btn-sm btn-orange">
            <i className="fas fa-arrow-right me-1"></i>
            {language === 'en' ? 'View Details' : 'Ver Detalles'}
          </a>
        </div>
      </div>
    </div>
  );
};

export default WorkExperienceCard; 