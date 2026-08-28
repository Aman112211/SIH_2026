from app import create_app
from app.data.seed import seed_demo_data

app = create_app()
with app.app_context():
    seed_demo_data()
    print("KARIGAR AI demo data seeded.")
