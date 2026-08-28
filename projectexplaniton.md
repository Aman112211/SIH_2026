# KARIGAR AI — Project Explanation

## 1. What is KARIGAR AI?

KARIGAR AI is an AI Commerce Copilot for India's marginalized artisans.

It is not another marketplace. It is an intelligence layer that helps artisans and government teams make better commerce decisions:

1. What do I have?
2. How should I sell it?
3. Where should I sell it?
4. What price should I charge?
5. What should I make next?
6. Which SHGs need support?

The central idea is:

> Existing systems help artisans enter digital commerce. KARIGAR AI helps them succeed inside it.

## 2. The Problem

Many artisans can make excellent products but face practical digital-commerce problems:

- Creating a professional listing is difficult.
- Forms and technical language create a barrier.
- Prices are often guessed or copied from competitors.
- Artisans do not know which markets have demand.
- Production decisions are not connected to market signals.
- Government officers can see numbers but may not know which group needs help first.

KARIGAR AI connects these separate decisions into one continuous workflow.

## 3. How the System Works

```text
Artisan voice or product information
              ↓
Product understanding
              ↓
Smart catalogue
              ↓
Listing health
              ↓
Fair price intelligence
              ↓
Market opportunity
              ↓
Production recommendation
              ↓
Commerce adapter
              ↓
Government intervention intelligence
```

The system is designed as a closed loop:

```text
Create → List → Sell → Observe → Learn → Recommend → Produce
```

## 4. Main User Experiences

### Artisan experience

The artisan sees a simple, mobile-friendly interface with one primary action: **Ask Karigar AI**.

In a production version, the artisan could say:

> This is a Kondapalli horse. I made it from poniki wood. It took three days. I sell it for 800 rupees.

The system would extract product attributes, identify missing information and ask only the next necessary question. The artisan remains the authority and confirms uncertain information before publishing.

The current demo represents this voice interaction with a lightweight browser interaction and a visible demo transcript.

### Officer experience

The officer dashboard aggregates artisan, product, sales and listing information. It highlights actionable problems such as:

- SHGs with weak catalogue quality
- Sellers whose prices may be unsustainable
- Clusters where demand exceeds supply
- Seasonal opportunities that need production support

The officer receives recommendations, but the officer reviews and approves any intervention.

## 5. Current Working Features

### Smart catalogue and listing health

Every product has a listing score. The demo product starts at `57/100` because it is missing dimensions, a complete description, a confirmed technique and an image.

The **Fix with AI** action fills safe missing fields and recalculates the score to `94/100`. The result is a visible before-and-after demonstration.

### Fair price intelligence

The price engine is deterministic and transparent. It calculates:

```text
Material cost
+ Fair labour
+ Packaging
+ Logistics
+ Platform cost
= Minimum sustainable cost
```

The demo uses a ₹550/day Andhra Pradesh skilled-labour benchmark proxy. The interface identifies the source and explicitly says it is not universal legal advice. The exact occupation, worker category, zone and current notification must be loaded before production use.

### Market opportunity

Market signals contain demand, competition, seasonality, source and confidence. The demo calculates an opportunity score using demand, inverse competition and seasonal strength.

The market screen displays cities such as Hyderabad, Pune and Bengaluru and labels the information as simulated demo market signals.

### Production recommendation

This is the main differentiator. The system answers:

> What should I make next?

The demo recommends a product, quantity, price range, target markets, selling period, estimated margin, reason and confidence level.

This connects market intelligence to an artisan's actual production decision.

### Government intervention intelligence

The officer dashboard provides three explainable priorities:

1. Photography support for SHGs with weak product images.
2. Pricing support for sellers who may be below sustainable prices.
3. Production and raw-material coordination where demand is higher than supply.

The dashboard also includes an impact simulation. It is visibly labelled as an estimate rather than a guaranteed outcome.

## 6. Technical Architecture

The application uses:

- Python 3.12+ as the target runtime
- Flask for the web backend
- Flask-SQLAlchemy for persistence
- SQLite for immediate local development
- PostgreSQL-compatible configuration for deployment
- Jinja2 server-rendered templates
- CSS for the design system and responsive layout
- Small vanilla JavaScript enhancements
- Pytest tests for the core application flow

Important code areas:

- `app/__init__.py` — application factory and database initialization
- `app/models.py` — users, artisans, SHGs, products, transactions and market signals
- `app/routes.py` — thin page and API routes
- `app/services/intelligence.py` — listing, pricing, production and intervention logic
- `app/data/seed.py` — deterministic synthetic demo dataset
- `templates/` — artisan, officer and SIH demo screens
- `static/css/style.css` — responsive visual system
- `static/js/app.js` — minimal browser interactions

The routes delegate decisions to services instead of embedding calculations in templates or controllers.

## 7. Demo Dataset

The seed script creates:

- 20 artisans
- 8 SHGs
- 60 products
- 240 transaction records
- 24 market signals
- Multiple Indian crafts and cities

The data is synthetic and is not presented as real ONDC, Amazon, Flipkart or government data. Transaction records carry the `synthetic_demo` source marker.

The primary demo persona is:

```text
Name: Ravi Kumar
Craft: Kondapalli Toys
Region: Andhra Pradesh
SHG: Sri Lakshmi SHG
```

## 8. Demo Flow

Open `/demo` and then follow this sequence:

1. Start with the problem: artisans need more than a marketplace listing.
2. Open the artisan view and press **Ask Karigar AI**.
3. Open the first product and show listing health at `57/100`.
4. Select **Fix with AI** and show the result at `94/100`.
5. Explain the transparent fair-price calculation and wage source.
6. Open market opportunities and compare cities.
7. Open production recommendations and show what the artisan should make next.
8. Open the officer dashboard and show prioritized SHG interventions.
9. End with the message: “We don't build another marketplace. We build the intelligence layer that helps artisans succeed across digital commerce.”

To restore the deterministic dataset:

```powershell
Invoke-WebRequest -Method Post http://127.0.0.1:5000/demo/reset
```

## 9. Important API Routes

- `GET /api/health` — application and database health
- `POST /api/pricing/recommend` — product pricing calculation
- `POST /api/production/recommend` — production recommendation
- `POST /api/officer/interventions/recommend` — intervention priorities
- `POST /demo/reset` — restore demo data

## 10. AI Design Principles

KARIGAR AI is AI-assisted, not AI-dependent.

Deterministic logic handles:

- Financial calculations
- Listing scores
- Database aggregation
- Market scoring
- Demo recommendations
- Input validation

AI providers can later handle:

- Speech recognition
- Multilingual translation
- Product attribute extraction
- Natural-language explanations
- Conversational business assistance

AI output must be validated, confidence-scored and confirmed where necessary. It must not invent sales, prices, market data or authenticity claims.

## 11. Honest Scope of the Current Version

The current version is a polished, working SIH vertical slice. It demonstrates the core decision flow without requiring external credentials.

The following are intentionally demo or roadmap capabilities:

- Voice processing currently uses a demo interaction rather than live ASR.
- Market and transaction information is synthetic.
- ONDC and WhatsApp are not live integrations.
- Images are not yet persisted through a production upload pipeline.
- Authentication and CSRF hardening are documented next steps.
- The wage benchmark is a proxy and must be replaced by an exact occupation-specific source for production.
- GI and authenticity checks are not official certification.

This separation is intentional: the application never claims a real integration or real-world data source that is unavailable.

## 12. How to Run

From the project directory:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python seed.py
python run.py
```

Then open:

- `http://127.0.0.1:5000` — artisan view
- `http://127.0.0.1:5000/demo` — SIH presentation flow
- `http://127.0.0.1:5000/officer` — government officer dashboard

## 13. Future Production Architecture

A production release would add:

- Flask-Login authentication and role-based access
- CSRF protection and stricter upload validation
- PostgreSQL and database migrations
- Occupation-specific wage benchmark records
- Real multilingual ASR and LLM provider adapters
- Human-confirmation workflows for extracted attributes
- Authorized ONDC and WhatsApp integrations
- Object storage for product images and audio
- Background jobs for forecasting and external synchronization
- Audit logs for officer recommendations and approvals

## 14. One-Line Explanation

> KARIGAR AI is a decision-intelligence platform that helps artisans list better, price fairly, find the right markets, decide what to produce next, and helps governments identify which artisan groups need support first.
