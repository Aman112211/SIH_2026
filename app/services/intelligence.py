from datetime import datetime, timedelta
from . import __name__
from ..models import Artisan, MarketSignal, Product, SHG
from ..extensions import db


def listing_health(product):
    score = product.listing_score or 0
    issues = []
    if not product.dimensions:
        issues.append({"severity": "critical", "message": "Missing dimensions"})
    if not product.description:
        issues.append({"severity": "warning", "message": "Description needs a clear buyer-facing story"})
    if not product.technique:
        issues.append({"severity": "warning", "message": "Technique is not confirmed"})
    if not product.images:
        issues.append({"severity": "warning", "message": "Add a primary product image"})
    if score >= 90:
        issues = [{"severity": "success", "message": "Listing is ready for marketplace publishing"}]
    return {"score": score, "issues": issues}


def price_recommendation(product):
    labour = product.production_time * 550
    material = product.cost or 600
    packaging, logistics, platform = 80, 120, 100
    sustainable = material + labour + packaging + logistics + platform
    recommended = round(max(sustainable * 1.12, product.price or sustainable) / 100) * 100
    return {"material": material, "labour": labour, "packaging": packaging, "logistics": logistics, "platform": platform, "minimum": round(sustainable), "recommended": recommended, "premium": round(recommended * 1.2), "wage_source": "AP Minimum Wages Notification G/3186486/2026", "wage_note": "₹550/day skilled-labour proxy; not legal advice."}


def production_recommendation(artisan):
    craft = artisan.craft if artisan else "Kalamkari"
    return {"product": "Kalamkari Dupatta" if "Kondapalli" not in craft else "Kondapalli Horse Set", "quantity": 25, "price_range": "₹1,899–₹2,099", "markets": ["Hyderabad", "Pune", "Bengaluru"], "period": "September–October", "estimated_margin": "₹31,250", "reason": "Demand is rising while comparable supply is relatively low in the selected markets.", "confidence": "Medium", "source": "Synthetic demo market model"}


def intervention_recommendations():
    return [{"priority": 1, "problem": "Poor product photography", "affected": "23 SHGs", "action": "Organise a district photography support camp", "impact": "High", "confidence": "Medium"}, {"priority": 2, "problem": "Unsustainable pricing", "affected": "12 sellers", "action": "Review labour benchmarks and pricing literacy", "impact": "High", "confidence": "Medium"}, {"priority": 3, "problem": "Demand exceeds supply", "affected": "7 clusters", "action": "Coordinate production planning and raw material access", "impact": "Medium", "confidence": "Medium"}]
