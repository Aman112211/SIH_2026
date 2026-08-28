# API

`GET /api/health` returns application and database status.

`POST /api/pricing/recommend` accepts `{ "product_id": number }` and returns a transparent cost breakdown.

`POST /api/production/recommend` returns the current artisan's recommended product, quantity, markets, price range, reason and confidence.

`POST /api/officer/interventions/recommend` returns explainable priorities. `POST /demo/reset` restores the synthetic dataset.
