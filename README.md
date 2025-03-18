TreeLearner 🌿🌳

Descripción:
TreeLearner es un clasificador de especies de árboles basado en visión artificial, diseñado específicamente para el Parque Ambiental Chimayoy ubicado en pasto-nariño (Colombia). Este proyecto utiliza técnicas de Machine Learning y aprendizaje profundo para la identificación precisa de especies vegetales a partir de imágenes, proporcionando una herramienta de base para futuras aplicaciones más avanzadas.

Objetivo:
El proyecto busca establecer una base sólida en la aplicación de modelos de inteligencia artificial para el reconocimiento de especies arbóreas. Su implementación inicial permitirá generar datos y optimizar modelos que en el futuro puedan expandirse a diferentes plataformas, como:

📱 Aplicaciones móviles para identificación en campo.
🌐 Aplicaciones web para consulta y análisis de especies.
📊 Integración con sistemas de monitoreo ambiental.

Alcance:
TreeLearner no solo es un proyecto base para el desarrollo de herramientas de clasificación de árboles, sino que también sienta las bases para exploraciones más amplias en la conservación y gestión ambiental mediante tecnología de inteligencia artificial.

🚀 Este es solo el comienzo de un ecosistema de aplicaciones inteligentes para el estudio y la preservación de la biodiversidad.

📂 Explicación de la estructura del proyecto

🏗 Estructura general

TreeLearner/ ├── env/ # Entorno virtual de Python (No se versiona) ├── data/ # Datos de imágenes de árboles │ ├── raw/ # Imágenes originales sin procesar │ ├── processed/ # Imágenes preprocesadas │ ├── labels/ # Anotaciones en formato YOLO │ └── metadata.csv # Información sobre las imágenes ├── models/ # Modelos entrenados │ └── yolo/ # Modelos YOLO │ ├── best.pt # Modelo YOLO optimizado │ └── yolov8_config.yaml # Configuración de entrenamiento ├── src/ # Código fuente │ ├── main.py # Punto de entrada del proyecto │ ├── preprocessing.py # Preprocesamiento de imágenes │ ├── model.py # Definición e integración con YOLO │ ├── train.py # Entrenamiento de YOLO │ ├── predict.py # Predicciones con YOLO │ └── evaluate.py # Evaluación del modelo ├── ui/ # Interfaz gráfica │ ├── app.py # Aplicación web o de escritorio │ ├── static/ # Archivos estáticos (CSS, JS, imágenes) │ └── templates/ # Plantillas HTML si se usa Flask ├── notebooks/ # Jupyter Notebooks │ ├── exploratory_analysis.ipynb # Análisis exploratorio de datos │ └── yolo_training.ipynb # Entrenamiento con YOLO ├── tests/ # Pruebas automatizadas │ ├── test_preprocessing.py # Pruebas del preprocesamiento │ └── test_model.py # Pruebas del modelo YOLO ├── logs/ # Registros del sistema │ └── training.log # Registros del entrenamiento ├── requirements.txt # Dependencias del proyecto └── README.md # Documentación general