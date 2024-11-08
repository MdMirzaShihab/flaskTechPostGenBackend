from src.app import create_app
from src.secret import SERVER_PORT

app = create_app()

if __name__ == "__main__":
    app.run(port=SERVER_PORT, debug=True)
