import React, { useState, useEffect } from 'react';
import { CSSTransition, TransitionGroup } from 'react-transition-group';
import axios from 'axios';
import ProjectCard from './ProjectCard';

import './ProjectList.css';

const ProjectList = ({ language }) => {
  const [projects, setProjects] = useState([]);
  const [filteredProjects, setFilteredProjects] = useState([]);
  const [activeFilter, setActiveFilter] = useState('all');
  const [loading, setLoading] = useState(true);
  
  useEffect(() => {
    const fetchProjects = async () => {
      try {
        const response = await axios.get('/api/projects/');
        setProjects(response.data.projects);
        setFilteredProjects(response.data.projects);
        setLoading(false);
      } catch (error) {
        console.error('Error fetching projects:', error);
        setLoading(false);
      }
    };
    
    fetchProjects();
  }, []);
  
  useEffect(() => {
    if (activeFilter === 'all') {
      setFilteredProjects(projects);
    } else {
      const filtered = projects.filter(project => 
        project.skills && project.skills.includes(activeFilter)
      );
      setFilteredProjects(filtered);
    }
  }, [activeFilter, projects]);
  
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
      <div className="filter-buttons" data-aos="fade-up">
        <button 
          className={`filter-btn ${activeFilter === 'all' ? 'active' : ''}`} 
          onClick={() => handleFilterChange('all')}
        >
          {language === 'en' ? 'All Projects' : 'Todos los Proyectos'}
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

      <div className="row">
        <TransitionGroup className="row" component={null}>
          {filteredProjects.map((project, index) => (
            <CSSTransition
              key={project.id}
              timeout={300}
              classNames="project-item"
            >
              <div 
                className="col-md-6 col-lg-4 mb-4 project-item" 
                data-aos="fade-up" 
                data-aos-delay={100 * (index % 3 + 1)}
              >
                <ProjectCard project={project} language={language} />
              </div>
            </CSSTransition>
          ))}
        </TransitionGroup>
      </div>
      
      {filteredProjects.length === 0 && (
        <div className="col-12 text-center py-5">
          <p>{language === 'en' ? 'No projects found with this filter.' : 'No se encontraron proyectos con este filtro.'}</p>
        </div>
      )}
    </div>
  );
};

export default ProjectList; 