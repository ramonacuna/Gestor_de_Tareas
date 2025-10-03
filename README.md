## Instalación y uso

1. Clona el repositorio:

    ```bash
    git clone https://github.com/miguepoloc/especializacion_ds
    cd especializacion_ds
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
