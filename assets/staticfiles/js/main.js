// Esperar a que el DOM esté completamente cargado
document.addEventListener('DOMContentLoaded', function() {
    // Función para cambiar el estilo del navbar al hacer scroll
    function handleNavbarScroll() {
        const navbar = document.querySelector('.navbar');
        if (window.scrollY > 50) {
            navbar.classList.add('bg-white', 'shadow-sm');
        } else {
            navbar.classList.remove('bg-white', 'shadow-sm');
        }
    }

    // Evento de scroll para el navbar
    window.addEventListener('scroll', handleNavbarScroll);

    // Reproducir video cuando se hace hover (para proyectos)
    const projectVideos = document.querySelectorAll('.project-video');
    if (projectVideos.length > 0) {
        projectVideos.forEach(video => {
            video.addEventListener('mouseenter', function() {
                if (this.paused) {
                    this.play();
                }
            });
            
            video.addEventListener('mouseleave', function() {
                if (!this.paused) {
                    this.pause();
                }
            });
        });
    }

    // Filtros para proyectos
    const filterButtons = document.querySelectorAll('.filter-btn');
    const projectItems = document.querySelectorAll('.project-item');

    if (filterButtons.length > 0 && projectItems.length > 0) {
        filterButtons.forEach(button => {
            button.addEventListener('click', function() {
                // Remover clase activa de todos los botones
                filterButtons.forEach(btn => btn.classList.remove('active'));
                
                // Añadir clase activa al botón actual
                this.classList.add('active');
                
                // Obtener el valor del filtro
                const filterValue = this.getAttribute('data-filter');
                
                // Filtrar proyectos
                projectItems.forEach(item => {
                    if (filterValue === 'all') {
                        item.style.display = 'block';
                    } else {
                        if (item.classList.contains(filterValue)) {
                            item.style.display = 'block';
                        } else {
                            item.style.display = 'none';
                        }
                    }
                });
            });
        });
    }

    // Validación del formulario de contacto
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            let isValid = true;
            
            // Validar nombre
            const nameInput = document.getElementById('name');
            if (!nameInput.value.trim()) {
                showError(nameInput, 'Por favor ingresa tu nombre');
                isValid = false;
            } else {
                removeError(nameInput);
            }
            
            // Validar email
            const emailInput = document.getElementById('email');
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailInput.value.trim() || !emailRegex.test(emailInput.value)) {
                showError(emailInput, 'Por favor ingresa un email válido');
                isValid = false;
            } else {
                removeError(emailInput);
            }
            
            // Validar asunto
            const subjectInput = document.getElementById('subject');
            if (!subjectInput.value.trim()) {
                showError(subjectInput, 'Por favor ingresa el asunto');
                isValid = false;
            } else {
                removeError(subjectInput);
            }
            
            // Validar mensaje
            const messageInput = document.getElementById('message');
            if (!messageInput.value.trim()) {
                showError(messageInput, 'Por favor ingresa tu mensaje');
                isValid = false;
            } else {
                removeError(messageInput);
            }
            
            // Si no es válido, prevenir el envío del formulario
            if (!isValid) {
                e.preventDefault();
            }
        });
    }

    // Función para mostrar error
    function showError(input, message) {
        const formControl = input.parentElement;
        const errorDiv = formControl.querySelector('.invalid-feedback') || document.createElement('div');
        
        errorDiv.className = 'invalid-feedback d-block';
        errorDiv.innerText = message;
        
        input.classList.add('is-invalid');
        
        if (!formControl.querySelector('.invalid-feedback')) {
            formControl.appendChild(errorDiv);
        }
    }

    // Función para remover error
    function removeError(input) {
        input.classList.remove('is-invalid');
        const formControl = input.parentElement;
        const errorDiv = formControl.querySelector('.invalid-feedback');
        
        if (errorDiv) {
            errorDiv.remove();
        }
    }

    // Efecto de parallax para la sección de héroe
    const heroSection = document.querySelector('.hero-section');
    if (heroSection) {
        window.addEventListener('scroll', function() {
            const scrollPosition = window.scrollY;
            const heroBackground = document.querySelector('.hero-background');
            
            if (heroBackground) {
                heroBackground.style.transform = `translateY(${scrollPosition * 0.4}px)`;
            }
        });
    }
});

// Inicializar lightbox para galería de proyectos
document.addEventListener('DOMContentLoaded', function() {
    // Verificar si hay imágenes en la galería
    const galleryItems = document.querySelectorAll('.gallery-item a');
    if (galleryItems.length > 0) {
        // Inicializar lightbox si existe la librería
        if (typeof GLightbox !== 'undefined') {
            GLightbox({
                selector: '.gallery-item a',
                touchNavigation: true,
                loop: true,
                autoplayVideos: false
            });
        }
    }
}); 