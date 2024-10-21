from src import create_app
import os


app = create_app()

if __name__ == '__main__':
    debug_mode = os.getenv('FLASK_DEBUG', 'false').lower() == 'true'
    app.run(host='0.0.0.0', port=int(os.getenv('FLASK_RUN_PORT', 5000)), debug=debug_mode)
