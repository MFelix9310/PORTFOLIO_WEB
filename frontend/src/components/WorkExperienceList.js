import React, { useState, useEffect } from 'react';
import { CSSTransition, TransitionGroup } from 'react-transition-group';
import axios from 'axios';
import WorkExperienceCard from './WorkExperienceCard';

import './WorkExperienceList.css';

const WorkExperienceList = ({ language }) => {
  const [experiences, setExperiences] = useState([]);
  const [filteredExperiences, setFilteredExperiences] = useState([]);
  const [activeFilter, setActiveFilter] = useState('all');
  const [loading, setLoading] = useState(true);
  
  useEffect(() => {
    const fetchExperiences = async () => {
      try {
        const response = await axios.get('/api/work-experiences/');
        setExperiences(response.data.work_experiences);
        setFilteredExperiences(response.data.work_experiences);
        setLoading(false);
      } catch (error) {
        console.error('Error fetching work experiences:', error);
        setLoading(false);
      }
    };
    
    fetchExperiences();
  }, []);
  
  useEffect(() => {
    if (activeFilter === 'all') {
      setFilteredExperiences(experiences);
    } else {
      const filtered = experiences.filter(experience => 
        experience.skills && experience.skills.includes(activeFilter)
      );
      setFilteredExperiences(filtered);
    }
  }, [activeFilter, experiences]);
  
  const handleFilterChange = (filter) => {
    setActiveFilter(filter);
  };
  
  if (loading) {
    return (
      <div className="text-center py-5">
        <div className="spinner-border text-orange" role="status">
          <span className="visually-hidden">Loading...</span>
        </div>
      </div>
    );
  }
  
  return (
    <div>
      {experiences.length > 1 && (
        <div className="filter-buttons" data-aos="fade-up">
          <button 
            className={`filter-btn ${activeFilter === 'all' ? 'active' : ''}`} 
            onClick={() => handleFilterChange('all')}
          >
            {language === 'en' ? 'All' : 'Todos'}
          </button>
          <button 
            className={`filter-btn ${activeFilter === 'data_scientist' ? 'active' : ''}`} 
            onClick={() => handleFilterChange('data_scientist')}
          >
            Data Scientist
          </button>
          <button 
            className={`filter-btn ${activeFilter === 'data_analyst' ? 'active' : ''}`} 
            onClick={() => handleFilterChange('data_analyst')}
          >
            Data Analyst
          </button>
          <button 
            className={`filter-btn ${activeFilter === 'python_developer' ? 'active' : ''}`} 
            onClick={() => handleFilterChange('python_developer')}
          >
            Python Developer
          </button>
        </div>
      )}

      <div className="row">
        <TransitionGroup className="row" component={null}>
          {filteredExperiences.map((experience, index) => (
            <CSSTransition
              key={experience.id}
              timeout={300}
              classNames="work-item"
            >
              <div 
                className="col-md-6 mb-4 work-item" 
                data-aos="fade-up" 
                data-aos-delay={100 * (index % 2 + 1)}
              >
                <WorkExperienceCard experience={experience} language={language} />
              </div>
            </CSSTransition>
          ))}
        </TransitionGroup>
      </div>
      
      {filteredExperiences.length === 0 && (
        <div className="col-12 text-center py-5">
          <p>{language === 'en' ? 'No work experiences found with this filter.' : 'No se encontraron experiencias laborales con este filtro.'}</p>
        </div>
      )}
    </div>
  );
};

export default WorkExperienceList; 