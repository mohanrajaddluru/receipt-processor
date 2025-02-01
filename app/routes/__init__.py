from .main import main_bp
from .receipts import receipts_bp

def register_routes(app):
    app.register_blueprint(main_bp)
    app.register_blueprint(receipts_bp)