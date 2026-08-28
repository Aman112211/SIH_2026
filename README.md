# KARIGAR AI

KARIGAR AI is a Flask-based AI Commerce Copilot for India's marginalized artisans. It sits above existing commerce infrastructure and turns product, market and business signals into the next useful decision: what to list, how to price, where to sell and what to make next. Officers get explainable SHG intervention intelligence.

## Run locally

Requires Python 3.12+.

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python seed.py
python run.py
```

Open `http://localhost:5000`, or use `/demo` for the controlled SIH story and `/officer` for the district dashboard. SQLite is the default. Set `DATABASE_URL` to a PostgreSQL SQLAlchemy URL for deployment.

## Core routes

- `/` artisan voice-first home
- `/products/<id>` listing health and fair pricing
- `/markets` explainable opportunity signals
- `/production` production recommendation
- `/officer` officer intelligence dashboard
- `/demo` six-step judge flow
- `/api/health` health check
- `POST /demo/reset` restore deterministic demo data

## Architecture

`app/models.py` contains the normalized commerce schema. `app/services/intelligence.py` owns deterministic scoring and recommendation logic; routes remain thin. External AI and commerce providers can be connected behind these service boundaries, while `DEMO_MODE=true` keeps the demonstrator honest and usable without credentials.

## Data honesty

The seed dataset is synthetic and marked `synthetic_demo` on transactions. Market signals are simulated. The ₹550/day Andhra Pradesh skilled-labour figure is displayed as a documented proxy, not universal legal advice. Authenticity and GI checks are not certification.

## Production roadmap

Add Flask-Login/CSRF auth, object-storage uploads, occupation-specific wage records, authorized ONDC credentials, real ASR/LLM adapters, migrations and background jobs before production deployment. See `docs/` for the intended boundaries.
