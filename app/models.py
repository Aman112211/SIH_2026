from datetime import datetime
from .extensions import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(160), unique=True, nullable=False)
    role = db.Column(db.String(30), nullable=False, default="artisan")
    artisan = db.relationship("Artisan", backref="user", uselist=False)


class SHG(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(160), nullable=False)
    district = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(100), nullable=False)
    cluster = db.Column(db.String(120), nullable=False)
    member_count = db.Column(db.Integer, default=12)
    artisans = db.relationship("Artisan", backref="shg", lazy=True)


class Artisan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(160), nullable=False)
    language = db.Column(db.String(30), default="Telugu")
    region = db.Column(db.String(100), default="Andhra Pradesh")
    craft = db.Column(db.String(120), nullable=False)
    experience_years = db.Column(db.Integer, default=10)
    verification_status = db.Column(db.String(40), default="Verified")
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    shg_id = db.Column(db.Integer, db.ForeignKey("shg.id"))
    products = db.relationship("Product", backref="artisan", lazy=True)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(160), nullable=False)
    craft = db.Column(db.String(120), nullable=False)
    material = db.Column(db.String(120), nullable=False)
    technique = db.Column(db.String(120))
    description = db.Column(db.Text)
    story = db.Column(db.Text)
    dimensions = db.Column(db.String(80))
    production_time = db.Column(db.Integer, default=3)
    cost = db.Column(db.Float, default=600)
    price = db.Column(db.Float, default=1200)
    inventory = db.Column(db.Integer, default=10)
    listing_score = db.Column(db.Integer, default=57)
    verification_status = db.Column(db.String(40), default="Pending")
    artisan_id = db.Column(db.Integer, db.ForeignKey("artisan.id"), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    images = db.relationship("ProductImage", backref="product", lazy=True)


class ProductImage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.String(255), nullable=False)
    quality_score = db.Column(db.Integer, default=41)
    is_primary = db.Column(db.Boolean, default=True)
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"), nullable=False)


class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"), nullable=False)
    quantity = db.Column(db.Integer, default=1)
    unit_price = db.Column(db.Float, default=1000)
    channel = db.Column(db.String(60), default="Demo channel")
    region = db.Column(db.String(100), default="Hyderabad")
    date = db.Column(db.DateTime, default=datetime.utcnow)
    data_source = db.Column(db.String(40), default="synthetic_demo")
    product = db.relationship("Product")


class MarketSignal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_category = db.Column(db.String(120), nullable=False)
    region = db.Column(db.String(100), nullable=False)
    demand_score = db.Column(db.Integer, default=70)
    competition_score = db.Column(db.Integer, default=50)
    seasonal_score = db.Column(db.Integer, default=70)
    source = db.Column(db.String(80), default="Synthetic Demo")
    confidence = db.Column(db.String(20), default="Medium")
    date = db.Column(db.DateTime, default=datetime.utcnow)


class Recommendation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    artisan_id = db.Column(db.Integer, db.ForeignKey("artisan.id"))
    recommendation_type = db.Column(db.String(60), nullable=False)
    score = db.Column(db.Integer, default=80)
    reason = db.Column(db.Text, nullable=False)
    confidence = db.Column(db.String(20), default="Medium")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class Intervention(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    shg_id = db.Column(db.Integer, db.ForeignKey("shg.id"))
    priority = db.Column(db.Integer, default=1)
    problem = db.Column(db.String(200), nullable=False)
    recommended_action = db.Column(db.Text, nullable=False)
    expected_impact = db.Column(db.String(40), default="Medium")
    confidence = db.Column(db.String(20), default="Medium")
    status = db.Column(db.String(30), default="Review")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    shg = db.relationship("SHG")
