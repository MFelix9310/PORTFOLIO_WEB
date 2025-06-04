# Portfolio Web Profesional de Felix Ruiz M.

Este es un portfolio web profesional y visualmente impactante que muestra el perfil como Python Developer y Data Scientist de Felix Ruiz M., con un diseño atractivo y funcionalidades dinámicas gestionadas a través de Django admin. Incorpora React para las interfaces de usuario más interactivas.

## Tecnologías Utilizadas

- **Backend**: Python Django con ORM para base de datos
- **API**: Django REST Framework para endpoints que alimentan a React
- **Frontend**: HTML5, CSS3, Bootstrap 5, React 18
- **Empaquetador**: Webpack para compilar los componentes React
- **Efectos visuales**: React Transition Group, Animaciones CSS, AOS Animations
- **Diseño responsivo**: Compatible con todos los dispositivos

## Características Principales

- Página de inicio con diseño impactante y secciones destacadas
- Sección de Educación con visualización atractiva
- Galería de Certificaciones con filtrado por estado de vigencia
- Showcase de Proyectos con interfaz React, animaciones y filtros interactivos
- Experiencia Laboral con componentes React y transiciones suaves
- Sección de Contacto con formulario y redes sociales
- Panel de administración Django para gestionar todo el contenido

## Arquitectura de la Aplicación

El proyecto utiliza una arquitectura híbrida:
- Django maneja el backend, la administración y renderiza las plantillas base
- React se integra en páginas específicas (proyectos y experiencia laboral) para proporcionar una interfaz de usuario más interactiva
- Django REST Framework proporciona endpoints API que alimentan los componentes React

## Requisitos de Instalación

- Python 3.8 o superior
- Node.js 14 o superior y npm
- pip (gestor de paquetes de Python)
- Entorno virtual (recomendado)

## Instalación

1. Clona este repositorio:
   ```
   git clone <url-del-repositorio>
   cd portfolio-web
   ```

2. Crea y activa un entorno virtual (opcional pero recomendado):
   ```
   python -m venv venv
   # En Windows:
   venv\Scripts\activate
   # En macOS/Linux:
   source venv/bin/activate
   ```

3. Instala las dependencias de Python:
   ```
   pip install -r requirements.txt
   ```

4. Instala las dependencias de Node.js:
   ```
   cd frontend
   npm install
   cd ..
   ```

5. Aplica las migraciones:
   ```
   python manage.py migrate
   ```

6. Crea un superusuario para acceder al panel de administración:
   ```
   python manage.py createsuperuser
   ```

7. Compila los componentes React:
   ```
   cd frontend
   npm run dev
   ```

8. En otra terminal, inicia el servidor de desarrollo Django:
   ```
   python manage.py runserver
   ```

9. Accede al sitio web en `http://127.0.0.1:8000/` y al panel de administración en `http://127.0.0.1:8000/admin/`

## Estructura del Proyecto

- `portfolio/`: Aplicación principal con los modelos y vistas
- `portfolio_web/`: Configuración del proyecto Django
- `static/`: Archivos estáticos (CSS, JS, imágenes)
- `media/`: Archivos subidos por el usuario
- `templates/`: Plantillas HTML
- `frontend/`: Código fuente de React
  - `src/`: Componentes y lógica React
  - `src/components/`: Componentes React reutilizables
  - `webpack.config.js`: Configuración de Webpack

## Desarrollo Frontend con React

Para trabajar en los componentes React:

1. Navega al directorio frontend:
   ```
   cd frontend
   ```

2. Inicia el compilador de webpack en modo desarrollo (observa cambios):
   ```
   npm run dev
   ```

3. Para construir para producción:
   ```
   npm run build
   ```

## Uso del Panel de Administración

1. Accede al panel de administración en `http://127.0.0.1:8000/admin/` con tus credenciales de superusuario.
2. Gestiona todas las secciones del portfolio:
   - **Perfil**: Información básica como nombre, título y biografía
   - **Educación**: Formación académica
   - **Certificaciones**: Certificados profesionales
   - **Proyectos**: Trabajos realizados con imágenes, videos y documentos
   - **Experiencia Laboral**: Historial profesional con empresas y posiciones

## Personalización

El diseño del portfolio está basado en un esquema de colores con blanco como base y acentos en naranja (#ff7a00), que se aplica tanto en los componentes Django tradicionales como en los componentes React.

Para personalizar:
- Estilos globales: modifica el archivo `static/css/style.css`
- Componentes React: edita los archivos `.css` en `frontend/src/components/`

