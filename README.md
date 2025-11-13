###  Descripción de Componentes

- **main.py**: Punto de entrada de la aplicación. Inicializa FastAPI y monta los routers.
- **db.py**: Configura la conexión a la base de datos.
- **models/**: Contiene los modelos que interactúan directamente con la base de datos.
- **services/**: Implementa la lógica de negocio, separando responsabilidades del controlador.
- **routers/**: Define los endpoints HTTP que exponen la funcionalidad de la API.
