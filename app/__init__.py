from flask import Flask, jsonify
from pathlib import Path
from .config import Config
from .extensions import db


def create_app(config_class=Config):
    root = Path(__file__).resolve().parent.parent
    app = Flask(__name__, template_folder=str(root / "templates"), static_folder=str(root / "static"))
    if isinstance(config_class, dict):
        app.config.from_mapping(config_class)
    else:
        app.config.from_object(config_class)
    app.config["UPLOAD_FOLDER"].mkdir(parents=True, exist_ok=True)
    db.init_app(app)

    from .routes import main
    app.register_blueprint(main)

    with app.app_context():
        db.create_all()

    @app.get("/api/health")
    def health():
        try:
            db.session.execute(db.text("SELECT 1"))
            database = "ok"
        except Exception:
            database = "unavailable"
        return jsonify({"status": "ok", "database": database, "demo_mode": app.config["DEMO_MODE"]})

    return app
