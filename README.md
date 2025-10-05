# 🔐 Auth Vue + Flask

Proyecto completo de **autenticación** con **frontend en Vue.js** y **backend en Flask (Python)**.  
Desarrollado como práctica para aprender sobre **GitHub, ramas, commits y colaboración**.

---

## 🧠 Descripción General

Este proyecto implementa un sistema básico de autenticación de usuarios donde el frontend (Vue.js) se comunica con una API REST construida en Flask.  
Incluye manejo de rutas, formularios de login/registro y conexión entre cliente y servidor.

**Estructura principal:**
auth-vue-flask/
├── frontend/ # Interfaz de usuario (Vue.js)
├── backend/ # API REST (Flask)
└── venv/ # Entorno virtual (no se sube a GitHub)

---

## 🚀 Tecnologías Utilizadas

### **Frontend**
- Vue.js 3
- Axios (para peticiones HTTP)
- HTML5, CSS3, JavaScript (ES6)
- Node.js y npm

### **Backend**
- Python 3.11
- Flask
- Flask-CORS
- Flask-Login
- Werkzeug

### **Otros**
- Git & GitHub (control de versiones)
- Visual Studio Code (IDE)
- Entorno virtual `venv`

---

## ⚙️ Instalación y Ejecución

### 🔹 Clonar el repositorio
```bash
git clone https://github.com/susanatc00/auth-vue-flask.git
cd auth-vue-flask
🔹 Backend (Flask)

Crea y activa un entorno virtual:

python -m venv venv
venv\Scripts\activate      # En Windows
source venv/bin/activate   # En Linux/Mac


Instala dependencias:

pip install -r requirements.txt


Ejecuta el servidor Flask:

cd backend
python app.py


El backend estará disponible en:

http://localhost:5000

🔹 Frontend (Vue.js)

Abre una nueva terminal y entra al directorio:

cd frontend


Instala las dependencias:

npm install


Ejecuta el servidor de desarrollo:

npm run serve


Abre en el navegador:

http://localhost:8080

🧩 Funcionalidades Principales

✅ Registro y autenticación de usuarios
✅ Comunicación entre frontend y backend vía API REST
✅ Validación básica de datos en formularios
✅ Separación clara entre cliente y servidor
✅ Estructura modular para escalar el proyecto

👩‍💻 Autora

Susana Toro C.
Estudiante de Ingeniería en ciencia de datos en la Universidad Pontificia Bolivariana
📧 susana.toroc@upb.edu.co

🐙 GitHub: @susanatc00

🌱 Próximos Pasos

Agregar base de datos (SQLite o PostgreSQL)

Mejorar la interfaz con Vue Router y componentes dinámicos

Añadir autenticación JWT

Implementar despliegue (Heroku o Vercel)

📜 Licencia

Este proyecto es de uso académico y libre para aprendizaje.
© 2025 Susana Toro C.
Actualizado por Susana Toro C. el 4 de octubre de 2025
