from src.config.config import APPLICATION_MODE_DEBUGABLE
from src.bootstrap import app
from src.route import route


if __name__ == '__main__':
    route(app)
    app.run_server(debug=APPLICATION_MODE_DEBUGABLE)
