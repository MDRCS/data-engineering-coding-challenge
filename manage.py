import os
from app import init_app

app = init_app(os.environ.get('environment'))

if __name__ == "__main__":
    app.run(port=5000, debug=True)
