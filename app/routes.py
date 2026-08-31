from flask import Blueprint, jsonify, render_template, request, redirect, url_for
from .extensions import db
from .models import Artisan, Product, Transaction, MarketSignal, SHG
from .services.intelligence import listing_health, price_recommendation, production_recommendation, intervention_recommendations

main = Blueprint("main", __name__)


def current_artisan():
    return Artisan.query.filter_by(name="Ravi Kumar").first() or Artisan.query.first()


@main.get("/")
def home():
    artisan = current_artisan()
    return render_template("artisan/home.html", artisan=artisan, products=artisan.products if artisan else [])


@main.get("/artisan")
def artisan():
    return redirect(url_for("main.home"))


@main.get("/products/<int:product_id>")
def product_detail(product_id):
    product = Product.query.get_or_404(product_id)
    health = listing_health(product)
    pricing = price_recommendation(product)
    return render_template("artisan/product.html", product=product, health=health, pricing=pricing)


@main.post("/products/<int:product_id>/fix")
def fix_listing(product_id):
    product = Product.query.get_or_404(product_id)
    product.listing_score = 94
    product.description = product.description or f"Handcrafted {product.name} made by an artisan in {product.artisan.region}."
    product.dimensions = product.dimensions or "8 x 4 x 3 inches"
    product.technique = product.technique or "Hand-painted"
    db.session.commit()
    return redirect(url_for("main.product_detail", product_id=product.id))


@main.get("/markets")
def markets():
    artisan = current_artisan()
    signals = MarketSignal.query.filter_by(product_category=artisan.craft if artisan else "Kalamkari").all()
    if not signals:
        signals = MarketSignal.query.all()
    return render_template("artisan/markets.html", signals=signals, artisan=artisan)


@main.get("/production")
def production():
    artisan = current_artisan()
    recommendation = production_recommendation(artisan)
    return render_template("artisan/production.html", recommendation=recommendation, artisan=artisan)


@main.get("/officer")
def officer():
    artisans = Artisan.query.count()
    products = Product.query.count()
    sales = sum(t.quantity * t.unit_price for t in Transaction.query.all())
    avg_listing = round(sum(p.listing_score for p in Product.query.all()) / products) if products else 0
    return render_template("officer/dashboard.html", artisans=artisans, products=products, sales=sales, avg_listing=avg_listing, shgs=SHG.query.count(), alerts=intervention_recommendations())


@main.post("/api/pricing/recommend")
def pricing_api():
    product = Product.query.get_or_404(request.json.get("product_id"))
    return jsonify(price_recommendation(product))


@main.post("/api/production/recommend")
def production_api():
    return jsonify(production_recommendation(current_artisan()))


@main.post("/api/officer/interventions/recommend")
def interventions_api():
    return jsonify(intervention_recommendations())


@main.get("/demo")
def demo():
    return render_template("demo.html")

@main.route("/demo/reset", methods=["GET", "POST"])
def demo_reset():
    from .data.seed import seed_demo_data
    seed_demo_data(reset=True)
    if request.method == "GET":
        next_page = request.args.get("next", url_for("main.product_detail", product_id=1))
        return redirect(next_page)
    return jsonify({"status": "reset", "message": "Demo dataset restored"})
