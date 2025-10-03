## Instalación y uso

1. Clona el repositorio:

    ```bash
    git clone https://github.com/ramonacuna/Gestor_de_Tareas.git
    cd Gestor_de_Tareas
    ```

2. Crea y activa un entorno virtual:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

    En windows
    ```bash
    python3 -m venv venv
    venv/Scripts/Activate
    ```

3. Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```
4. Corre la aplicación


    ```bash
    uvicorn main:app --reload
    ```
