from datetime import datetime, timedelta
from ..extensions import db
from ..models import Artisan, MarketSignal, Product, SHG, Transaction, User

CRAFTS = [("Kondapalli Toys", "Poniki wood", "Andhra Pradesh"), ("Kalamkari", "Cotton", "Andhra Pradesh"), ("Channapatna Toys", "Ivory wood", "Karnataka"), ("Pochampally Ikat", "Silk", "Telangana"), ("Madhubani", "Natural pigments", "Bihar"), ("Blue Pottery", "Quartz clay", "Rajasthan"), ("Dhokra", "Bell metal", "Chhattisgarh"), ("Banarasi weaving", "Silk", "Uttar Pradesh")]
CITIES = [("Hyderabad", 91, 67), ("Pune", 83, 39), ("Bengaluru", 89, 82), ("Chennai", 72, 31), ("Delhi", 78, 61), ("Mumbai", 86, 74)]


def seed_demo_data(reset=False):
    if reset:
        db.drop_all(); db.create_all()
    if User.query.first():
        return
    shgs = []
    for index in range(8):
        shg = SHG(name=f"{['Sri Lakshmi','Ujjwala','Srujana','Navjeevan','Mitti','Kala Jyoti','Sakhi','Hastkala'][index]} SHG", district=f"District {index + 1}", state=CRAFTS[index][2], cluster=f"{CRAFTS[index][0]} Cluster", member_count=12 + index)
        db.session.add(shg); shgs.append(shg)
    db.session.flush()
    for index in range(20):
        craft, material, region = CRAFTS[index % len(CRAFTS)]
        user = User(email=f"artisan{index + 1}@demo.karigar.ai", role="artisan")
        artisan = Artisan(name="Ravi Kumar" if index == 0 else f"Artisan {index + 1}", language="Telugu" if index < 4 else "Hindi", region=region, craft=craft, experience_years=8 + index % 13, shg_id=shgs[index % 8].id, user=user)
        db.session.add(user); db.session.add(artisan); db.session.flush()
        for item in range(3):
            product = Product(name=f"{craft} {['Signature Piece','Festival Collection','Everyday Classic'][item]}", craft=craft, material=material, technique="Handcrafted", description=None if index == 0 and item == 0 else f"Made by {artisan.name} using traditional {craft} techniques.", story=f"A contemporary expression of {craft} from {region}.", dimensions=None if index == 0 and item == 0 else "8 x 4 x 3 inches", production_time=3 + item, cost=600 + item * 150, price=1200 + item * 300, inventory=8 + item * 4, listing_score=57 if index == 0 and item == 0 else 78 + item * 5, artisan_id=artisan.id)
            db.session.add(product); db.session.flush()
            for sale in range(4):
                db.session.add(Transaction(product_id=product.id, quantity=1 + sale % 2, unit_price=product.price, channel="Demo channel", region=CITIES[sale % len(CITIES)][0], date=datetime.utcnow() - timedelta(days=sale * 9), data_source="synthetic_demo"))
    for craft, _, _ in CRAFTS:
        for city, demand, competition in CITIES[:3]:
            db.session.add(MarketSignal(product_category=craft, region=city, demand_score=demand, competition_score=competition, seasonal_score=76, source="Synthetic Demo", confidence="Medium"))
    db.session.commit()
