# SIH26090 — KARIGAR AI
## AI Commerce Copilot for India's Marginalized Artisans

**Tagline:**  
> Don't just put artisans online. Help them succeed online.

---

# 1. Executive Summary

The original SIH26090 concept focused on:

> Voice → AI Catalog → Marketplace

After competitive research, this is not differentiated enough.

Existing solutions already provide combinations of:

- AI product descriptions
- AI titles and tags
- image enhancement
- regional-language support
- voice-based cataloguing
- pricing intelligence
- ONDC connectivity
- artisan marketplaces
- authenticity features

Examples include ONDC seller-enablement infrastructure, eSARAS, IndiaHandmade, Amazon Saheli, Flipkart Samarth, Artisans' Wizard, HeritageVastra, KalaHubIndia, KalaMitra, and voice-first artisan commerce research.

Therefore, the project should be repositioned as:

> **KARIGAR AI — an AI Commerce Copilot that continuously turns an artisan's voice, products and business data into better listings, fairer prices, higher-demand markets, better production decisions, and actionable government interventions.**

The project should **not compete with marketplaces**.

It should become the **intelligence layer above existing digital-commerce infrastructure**.

---

# 2. Core Strategic Change

## Old Concept

```text
Voice
  ↓
AI Catalog
  ↓
Marketplace
```

## New Concept

```text
Artisan
   ↓
AI Commerce Copilot
   ↓
Understand
   ↓
Create
   ↓
Price
   ↓
Find Market
   ↓
Recommend Production
   ↓
Publish
   ↓
Observe Sales
   ↓
Learn
   ↓
Recommend Again
```

The core idea is a **closed-loop artisan commerce intelligence system**.

---

# 3. The Five Questions KARIGAR AI Answers

The entire product should revolve around five questions:

### 1. What do I have?

AI understands the artisan's products.

### 2. How should I sell it?

AI creates and optimizes the listing.

### 3. Where should I sell it?

AI identifies market opportunities.

### 4. What should I charge?

AI calculates a fair and competitive price.

### 5. What should I make next?

AI converts market signals into production recommendations.

The fifth question is the most important differentiator.

---

# 4. Product Architecture

```text
                         KARIGAR AI
                              │
              ┌───────────────┼───────────────┐
              │               │               │
              ▼               ▼               ▼
          VOICE AI         VISION AI        KNOWLEDGE
              │               │               │
              └───────────────┼───────────────┘
                              ▼
                    PRODUCT KNOWLEDGE GRAPH
                              │
          ┌───────────────────┼───────────────────┐
          ▼                   ▼                   ▼
     LISTING AI           PRICE AI            MARKET AI
          │                   │                   │
          ▼                   ▼                   ▼
    Listing Health       Fair Price          Market Map
          │                   │                   │
          └───────────────────┼───────────────────┘
                              ▼
                     PRODUCTION AI
                              │
                              ▼
                  "WHAT SHOULD I MAKE?"
                              │
                              ▼
                    COMMERCE CONNECTOR
                              │
                   ONDC / OTHER CHANNELS
                              │
                              ▼
                     GOVERNMENT AI HUB
                              │
                  ┌───────────┴───────────┐
                  ▼                       ▼
             SHG ANALYTICS        INTERVENTION AI
```

---

# 5. Core AI Engine #1 — Zero-Form Cataloguing

The artisan should not be forced to navigate complex forms.

Example:

> "This is a Kondapalli horse. I made it from poniki wood. It took three days. I sell it for 800 rupees."

AI extracts:

```text
Craft: Kondapalli Toy
Object: Horse
Material: Poniki wood
Production time: 3 days
Price: ₹800
Region: Andhra Pradesh
Dimensions: Missing
```

Instead of presenting a large form, the system asks only for missing information:

> **AI:** "What is the height of the toy?"

> **Artisan:** "Eight inches."

Done.

## Key principle

### Zero-form commerce

The artisan communicates naturally; the AI converts the conversation into structured commerce data.

---

# 6. Confidence-Aware AI

Every AI-extracted attribute should have a confidence score.

Example:

```text
Kondapalli craft       ██████████ 98%
Poniki wood            █████████░ 91%
Horse                  ██████████ 99%
8 inches                ██████████ 97%
Hand-painted            ██████░░░░ 63%
```

Low-confidence information should require confirmation.

Example:

> ⚠️ I'm not sure whether this product is hand-painted. Can you confirm?

This prevents hallucinated product information.

### Judge answer

If asked:

> "What happens when AI is wrong?"

Answer:

> "The system never treats generated attributes as facts. Every extracted attribute has a confidence score, and low-confidence fields require human confirmation."

---

# 7. Core AI Engine #2 — Listing Doctor

Every product receives an AI-generated listing quality score.

Example:

# Listing Health — 57/100

```text
❌ Missing dimensions
❌ Poor main image
❌ Weak title
⚠️ Missing care instructions
⚠️ Low search relevance
⚠️ Price may be uncompetitive
```

Then:

## FIX WITH AI

The system automatically improves everything it safely can.

Result:

# Listing Health — 94/100

This creates a strong:

> **Before → AI → After**

live demonstration.

---

# 8. AI Image Enhancement

The system should improve real product photographs without fabricating the product.

Features:

- background removal
- lighting correction
- cropping
- framing
- blur detection
- image quality scoring
- e-commerce aspect-ratio correction

Example:

```text
Before
Image Quality: 41/100

        ↓ AI Enhancement

After
Image Quality: 91/100
```

The system should explicitly communicate:

> **Product-preserving enhancement. No product geometry or design was generated.**

Avoid AI-generated fake product photography.

---

# 9. Core AI Engine #3 — Market Opportunity Engine

Do not simply say:

> "Kalamkari is trending."

Instead calculate a:

# Market Opportunity Score

Example:

| City | Demand | Competition | Opportunity |
|---|---:|---:|---:|
| Hyderabad | 91 | 67 | **86** |
| Pune | 83 | 39 | **88** |
| Bengaluru | 89 | 82 | **72** |
| Chennai | 72 | 31 | **81** |

AI recommendation:

> **Pune is the best expansion market.**

The score should be explainable.

### Example

```text
Market Opportunity = 88/100

+ High demand signal
+ Low competing supply
+ Suitable price range
+ Strong historical performance
+ Upcoming seasonal demand

Confidence: Medium
```

---

# 10. Explainable Market Intelligence

Every recommendation should answer:

- What?
- Where?
- Why?
- Confidence?

Never output an unexplained number.

Example:

> **Why Pune?**

> Demand is strong, competing supply is relatively low, the expected price range fits the artisan's product, and historical sales indicate potential.

This turns the system into explainable decision support rather than a black-box score.

---

# 11. The Hero Feature — "What Should I Make Next?"

The artisan presses:

# Ask Karigar AI 🎙️

and asks:

> "What should I make next?"

The system considers:

- existing products
- production capacity
- material costs
- historical sales
- seasonal demand
- festivals
- geography
- market prices
- competitor supply
- inventory
- product popularity

Example output:

---

## KARIGAR AI PRODUCTION RECOMMENDATION

**Product:** Kalamkari Dupatta

**Recommended quantity:** 25

**Recommended price:** ₹1,899–₹2,099

**Best markets:**
- Hyderabad
- Bengaluru
- Pune

**Demand:** High

**Competition:** Medium

**Best selling period:** September–October

**Reason:**

> Demand for similar products is increasing while comparable supply is relatively low.

---

This is the strongest answer to the question:

> **"Where is the actual market linkage?"**

---

# 12. AI Production Planner

Go one step beyond a recommendation.

Suppose:

```text
Production capacity:
10 units/week

Available cotton:
30 metres

Available labour:
4 days/week
```

AI generates:

## Production Plan — Next 4 Weeks

| Product | Quantity |
|---|---:|
| Kalamkari Dupatta | 20 |
| Small Wall Art | 15 |
| Table Runner | 10 |

Then:

> Estimated revenue: ₹62,400

> Estimated material requirement: 72m

> ⚠️ You may run short of cotton by week 3.

This connects:

**Demand → Inventory → Production → Revenue**

---

# 13. Core AI Engine #4 — Fair Price Intelligence

Do not use only:

```text
Material + Labour + Profit
```

The labour component must be grounded in a **citable wage benchmark**, not an arbitrary multiplier.

## Legal / Reference Floor

India's minimum-wage framework establishes wage floors, while the applicable rate depends on the scheduled employment, worker category, state, zone and current notification.

For the SIH demonstration, the artisan persona is from **Andhra Pradesh**.

Use the current Andhra Pradesh minimum-wage notification as the source of the wage benchmark shown in the application.

### Demo reference

**Andhra Pradesh Minimum Wages Notification No. G/3186486/2026**

- Issued: 23 March 2026
- Published in Andhra Pradesh Gazette Extraordinary: 25 March 2026
- Effective: 1 April 2026
- Issuing authority: Office of the Commissioner of Labour, Andhra Pradesh
- Next revision: 1 October 2026

For the published **Skilled/Specialised category, Zone I, Shops & Commercial Establishments schedule**, the combined basic + VDA figures are approximately **₹13,467–₹13,669/month**, or roughly **₹520–₹590/day** when converted using a 26-day month.

**Important qualification:** this is a skilled-labour proxy from the Shops & Commercial Establishments schedule, not the exact legal rate for Kondapalli toy-making. The full notification separately covers scheduled employments including handloom weaving and wood working. For a production deployment, KARIGAR AI must use the exact applicable scheduled-employment rate for the artisan's occupation and location.

For the SIH demo, use:

> **Reference skilled-labour benchmark: ₹550/day**

and display the source and the fact that it is a proxy.

### Fair Labour

```text
State: Andhra Pradesh

Reference:
AP Minimum Wages Notification G/3186486/2026
Effective: 1 April 2026

Reference skilled-labour benchmark:
~₹520–₹590/day

Demo calculation:
4 days × ₹550/day = ₹2,200
```

### Why "fair" needs to beat the floor

Independent field research has reported that handicraft and handloom workers earn an average of approximately **₹270/day**, substantially below the skilled-worker benchmark used above.

KARIGAR AI should therefore define:

> **Fair labour = at least the applicable state-notified skilled-worker wage benchmark, where legally applicable, with the system explicitly distinguishing a legal wage floor from a broader living/fair-wage concept.**

The system must never claim that ₹550/day is the exact legal rate for every Andhra Pradesh artisan. It is a demo benchmark until the exact occupation-specific schedule is loaded.

### Pricing example

```text
Material cost              ₹600
Fair labour (4 × ₹550)   ₹2,200
Packaging                   ₹80
Logistics                  ₹120
Platform cost              ₹100
────────────────────────────────
Minimum sustainable cost ₹3,100
```

Then compare market prices:

```text
Market low       ₹2,999
Market median    ₹3,499
Market high      ₹4,299
```

AI recommendation:

# ₹3,499

Explanation:

> This price covers the material and operating costs while recognizing artisan labour using a documented state wage benchmark. The recommendation is also checked against the observed market range.

### UI requirement

The pricing screen must show the wage source.

Example:

```text
FAIR LABOUR

Andhra Pradesh
Skilled-labour reference: ₹550/day

Source:
AP Minimum Wages Notification
G/3186486/2026
Effective 1 Apr 2026

4 days × ₹550
= ₹2,200
```

Add:

> **This is a reference wage benchmark, not legal advice. Exact applicable wages depend on the scheduled employment, worker category, zone and current government notification.**

### Judge answer

If asked:

> "How did you decide what a fair wage is?"

Answer:

> "Fair labour isn't an arbitrary multiplier. For the prototype, we anchor it to a documented Andhra Pradesh skilled-worker minimum-wage benchmark from the state's current notification and explicitly identify it as a proxy where the exact occupation-specific schedule has not yet been loaded. Independent field research reports handicraft workers averaging around ₹270 per day, which highlights the gap our pricing engine is designed to address."

### Wage data model

The implementation should store wage benchmarks as data records rather than hard-coding them inside pricing logic.

Example:

```text
wage_benchmark
├── state
├── occupation
├── category
├── zone
├── basic_wage
├── vda
├── effective_from
├── effective_until
├── source
├── source_url
└── is_proxy
```

This allows the wage database to be updated when government notifications change.

### Sources

- Government of Andhra Pradesh / Commissioner of Labour — Minimum Wages Notification No. G/3186486/2026, effective 1 April 2026.
- Minimum Wages Act, 1948.
- Code on Wages, 2019.
- Independent field research on handicraft/handloom worker earnings.

---

# 14. Price Simulator

Add an interactive price slider.

Example:

```text
₹2,999
Expected demand: ███████
Margin: ₹1,099

₹2,799
Expected demand: █████████
Margin: ₹899

₹2,499
Expected demand: ██████████
Margin: ₹599
```

AI:

> Recommended trade-off: ₹2,799

Clearly label demand figures as estimates where applicable.

---

# 15. Artisan AI Business Manager

The artisan should be able to ask business questions using voice.

### Example

> "How are my products doing?"

AI:

> You sold 34 products this month and generated ₹38,420.

---

> "Which product is selling best?"

AI:

> Your Kalamkari dupatta is your best-performing product.

---

> "What should I make?"

AI:

> Produce 20 more Kalamkari dupattas before the upcoming seasonal demand window.

This transforms the product from:

> Cataloguing software

into:

> **AI business intelligence for artisans.**

---

# 16. The Artisan Home Screen

Keep the interface extremely simple.

```text
┌──────────────────────────────┐
│        NAMASTE, RAVI 👋      │
│                              │
│       Ask Karigar AI 🎙️      │
│                              │
│       "What should I make?"  │
│                              │
├──────────────────────────────┤
│                              │
│  📦 My Products              │
│  24 active                   │
│                              │
│  📈 My Business              │
│  ₹38,420 this month          │
│                              │
│  💰 Fair Prices              │
│  3 products need review      │
│                              │
│  🔥 Opportunities            │
│  2 new markets found         │
│                              │
└──────────────────────────────┘
```

The AI should be the primary interface.

---

# 17. Voice as Universal Interface

Examples:

> "How much did I sell this month?"

> "Which product is selling best?"

> "Add 20 more."

> "Make this product unavailable."

> "What should I make next?"

The system should understand conversational commands and confirm risky actions.

---

# 18. WhatsApp Interface

Do not build a giant WhatsApp product.

Build a small deployment bridge:

```text
VOICE NOTE
     ↓
WhatsApp
     ↓
KARIGAR AI
     ↓
PRODUCT / INVENTORY / QUERY
```

Support only essential commands for the prototype.

Examples:

- Add product
- Ask sales
- Ask price
- Ask what to produce
- Update inventory

---

# 19. Universal Product Schema

Create one canonical product object.

Example:

```text
Product
├── Artisan
├── SHG
├── Cluster
├── Craft
├── Technique
├── Material
├── Dimensions
├── Weight
├── Production Time
├── Cost
├── Price
├── Inventory
├── Images
├── Artisan Story
├── GI Information
└── Verification Status
```

This object becomes the source of truth.

---

# 20. Marketplace Adapter Engine

The architecture should be:

```text
             KARIGAR PRODUCT
                    │
             Universal Schema
                    │
        ┌───────────┼───────────┐
        ▼           ▼           ▼
      ONDC       CSV/API     WhatsApp
```

If feasible, implement one genuine commerce integration.

For others, build transparent prototype adapters.

Do not fake production integrations.

---

# 21. Government AI Hub

This is one of the strongest differentiators.

Government officer logs in and sees:

# DISTRICT ARTISAN INTELLIGENCE

```text
ARTISANS
1,248

ACTIVE PRODUCTS
8,421

DIGITAL SALES
₹32.8L

CATALOG HEALTH
76%

MARKET OPPORTUNITY
83/100
```

Then:

# 🚨 AI ALERTS

### 23 SHGs

Need catalogue improvement.

### 7 clusters

Have rising demand but insufficient supply.

### 12 sellers

Appear significantly underpriced.

### 4 clusters

Have products suitable for an upcoming festival.

---

# 22. Intervention AI

Officer asks:

> **"What should the department do?"**

AI responds:

### Priority 1 — Photography Support

23 SHGs have low image-quality scores and strong products.

**Expected impact:** High.

### Priority 2 — Pricing Support

12 SHGs appear to be selling below sustainable price ranges.

### Priority 3 — Production Expansion

7 clusters have strong market demand but insufficient inventory.

This turns the dashboard from:

> Analytics

into:

> **Decision support.**

---

# 23. Impact Simulator

Allow the officer to simulate interventions.

Example:

> Improve catalogue quality for 100 SHGs.

AI displays:

```text
Current average listing score:
58

Estimated post-intervention score:
86

Potential products improved:
1,240

Estimated market visibility improvement:
+31%
```

Always label this as:

> **Simulation / estimated impact**

Never present estimates as guaranteed outcomes.

---

# 24. Craft Knowledge Base

Build a structured knowledge layer for crafts.

Example:

```text
Kondapalli Toys

Region:
Andhra Pradesh

Traditional material:
Poniki wood

Craft techniques:
...

GI:
...

Traditional products:
...

Associated artisan clusters:
...
```

The AI can use this to detect inconsistencies.

Example:

> ⚠️ Traditional Kondapalli toys are generally associated with poniki wood. Please verify the material you entered.

The system should assist verification, not claim to certify authenticity.

---

# 25. Authenticity Assistant

Do not claim:

> "AI verifies GI authenticity."

Instead use:

# Authenticity Risk Assessment

```text
Craft claim          ✓ Consistent
Region               ✓ Consistent
Material             ✓ Plausible
GI information       ⚠ Not verified
Seller identity      ✓ Verified
```

Output:

> Verification status: Pending

This is safer and more defensible.

---

# 26. Artisan Digital Identity

Each artisan can have a profile:

```text
Ravi Kumar
Kondapalli Craftsperson

Craft:
Kondapalli Toys

Cluster:
Krishna District

Experience:
18 years

SHG:
XYZ SHG

Products:
24

Digital Sales:
₹2.8L

Verified:
✓ Identity
✓ SHG
✓ Craft Cluster
```

Keep advanced authentication for the future.

---

# 27. Closed-Loop Intelligence

This should become the central diagram in the presentation:

```text
CREATE
  ↓
LIST
  ↓
SELL
  ↓
OBSERVE
  ↓
LEARN
  ↓
RECOMMEND
  ↓
PRODUCE
  ↓
SELL MORE
```

The system continuously feeds market outcomes back into production and listing decisions.

---

# 28. Data Architecture

Do not claim access to private Amazon/Flipkart/marketplace transaction data unless actually authorized.

Use four data categories.

## Level 1 — Verified

- Test seller data
- Authorized partner data
- Accessible ONDC environment data
- Government/open datasets

## Level 2 — Partner-provided

- SHG data
- Federation data
- Pilot partner data

## Level 3 — Public market signals

- Public trend signals
- Festival calendars
- Public product/category data
- GI information

## Level 4 — Simulation

Controlled data created for the SIH prototype.

Always label demo data as:

> **Demo dataset / simulated data**

---

# 29. Data Confidence

Every important AI recommendation should have a confidence indicator.

Example:

> Pune Market Opportunity: **88/100**

> Confidence: 🟡 Medium

> Based on:
> - historical seller data
> - public market signals
> - seasonal demand
> - category data

This makes the system more trustworthy.

---

# 30. Technical Stack

## Frontend

- React Native or React
- Simple artisan UI
- Separate officer dashboard

## Backend

- FastAPI or Node.js
- REST/WebSocket APIs

## Database

- PostgreSQL / Supabase

## AI

Potential components:

- Whisper / IndicConformer / Bhashini / suitable multilingual ASR
- LLM for extraction and reasoning
- Computer vision for image quality
- Embeddings/vector search for craft knowledge
- Recommendation engine
- Lightweight forecasting

## Image

- Background removal
- Enhancement
- Quality scoring

## Commerce

- ONDC-compatible integration where feasible
- Universal product schema
- Adapter architecture

## Messaging

- WhatsApp Cloud API for limited prototype functionality

---

# 31. MVP vs Demo vs Production

## MVP

Must actually work:

1. Voice → structured product
2. Missing-field conversation
3. Listing Health Score
4. Image enhancement
5. Fair Price Intelligence
6. Market Opportunity Map
7. "What should I make next?"
8. Officer dashboard
9. Intervention AI

## Demo-only

Can be simulated carefully:

- Multi-marketplace adapters
- Large-scale transaction data
- Large SHG datasets
- Forecasting scenarios

## Production

Future:

- Authorized marketplace integrations
- Real SHG federation data
- More regional languages
- Offline inference
- Advanced authentication
- Advanced GI verification
- Logistics optimization

---

# 32. What NOT to Build

Remove from the SIH MVP:

- Full marketplace
- Checkout
- Payment system
- AR/VR
- AI-generated product photography
- Blockchain
- Complex GI authentication
- Ten marketplace integrations
- Giant WhatsApp platform
- Overcomplicated ML forecasting

These consume time without strengthening the core innovation.

---

# 33. What Must Be Built

## Priority 1

### Voice → Structured Product

Real.

## Priority 2

### AI Missing-Field Conversation

Real.

## Priority 3

### Listing Health + Auto Fix

Real.

## Priority 4

### Fair Price Intelligence

Real.

## Priority 5

### Market Opportunity Engine

Real enough for a convincing controlled demo.

## Priority 6

### "What Should I Make Next?"

Real recommendation pipeline.

## Priority 7

### Officer Dashboard

Real.

## Priority 8

### Intervention AI

Real.

## Priority 9

### One commerce connector

Real if feasible.

---

# 34. Six-Minute SIH Demo

## 0:00–0:30 — Problem

Show an artisan.

> "I can make the product. I don't know how to sell it digitally."

Show:

- language barrier
- catalogue difficulty
- pricing uncertainty
- market uncertainty

---

## 0:30–1:20 — Voice

Artisan speaks Telugu.

AI creates:

> Kondapalli Toy

Automatically.

AI asks one missing question.

Product is completed.

---

## 1:20–1:50 — Listing Doctor

Show:

> Listing Health: 57/100

Click:

> Fix with AI

Result:

> Listing Health: 94/100

---

## 1:50–2:30 — Fair Price

Show:

- production cost
- fair labour
- packaging
- logistics
- market range

AI:

> Recommended price: ₹1,199

Then demonstrate the price simulator.

---

## 2:30–3:30 — Market Intelligence

Ask:

> "Where should I sell this?"

Show market map.

Then:

> "What should I make next?"

AI recommends:

> Produce 25 more units before seasonal demand.

This is the main WOW moment.

---

## 3:30–4:15 — Commerce

Click:

> Publish

Show:

```text
Universal Product
       ↓
ONDC-compatible catalogue
```

Show the adapter architecture.

---

## 4:15–5:15 — Government Dashboard

Switch to officer.

Show:

- artisan count
- products
- sales
- listing health

Then show:

> 23 SHGs need catalogue support.

> 7 clusters have unmet demand.

> 12 sellers may be underpricing.

---

## 5:15–5:45 — Intervention AI

Officer asks:

> "What should we do?"

AI creates a prioritized intervention plan.

---

## 5:45–6:00 — Close

Show:

# WE DON'T BUILD ANOTHER MARKETPLACE.

# WE BUILD THE INTELLIGENCE LAYER THAT HELPS ARTISANS SUCCEED ACROSS DIGITAL COMMERCE.

---

# 35. Competitive Positioning

| Existing Solution | Main Strength | KARIGAR AI Opportunity |
|---|---|---|
| ONDC | Open commerce/interoperability | Add decision intelligence above the network |
| eSARAS | SHG marketplace and government ecosystem | Add AI business intelligence and intervention |
| IndiaHandmade | Government artisan marketplace | Add continuous optimization |
| Amazon Saheli | Seller enablement | Not marketplace-specific |
| Flipkart Samarth | Artisan market access | Cross-channel intelligence |
| Artisans' Wizard | AI cataloguing, voice, BI, ONDC | Differentiate through production + government intervention loop |
| HeritageVastra | AI inventory, pricing, authenticity | Broader government/SHG intelligence |
| KalaHubIndia | AI, pricing, demand, commerce | Stronger closed-loop production and intervention model |
| KalaMitra | Voice, AI shopping, AR | Focus on operational intelligence rather than consumer experience |
| Gram Sootra | Voice-first rural commerce | Extend voice beyond listing into continuous business management |

---

# 36. What Is Actually Unique?

Do NOT claim that these are individually unique:

- Voice cataloguing
- AI descriptions
- AI image enhancement
- ONDC integration
- Regional language
- Basic fair pricing

Instead claim differentiation around:

## 1. AI Production Intelligence

> What should this artisan make next?

## 2. AI Intervention Intelligence

> Which SHGs should the government help first, and why?

## 3. Zero-Form Commerce

> Natural voice interaction instead of complex digital forms.

## 4. Explainable Market Intelligence

> What → Where → Why → Confidence.

## 5. Closed-Loop Commerce

> Product → Listing → Market → Sale → Feedback → Recommendation → Production.

---

# 37. Strongest USP

## Existing systems

> "Here is how to list your product."

## KARIGAR AI

> **"Here is what you should do next."**

This is the conceptual leap.

---

# 38. Judge Question — "Why don't artisans just use ONDC?"

Recommended answer:

> "ONDC solves network interoperability and digital market access. KARIGAR AI operates one layer above that. We help the artisan decide what to produce, how to present it, how to price it, which market to target, and help government officers identify which artisan groups need intervention. We are not replacing ONDC; we are making digital commerce more actionable for people who currently lack the digital skills and business intelligence to use it effectively."

---

# 39. Judge Question — "Artisans' Wizard already does this."

Recommended answer:

> "We recognize that AI cataloguing, voice and business intelligence are not individually novel, and existing solutions demonstrate their feasibility. Our differentiation is the closed-loop decision layer: market opportunity → fair pricing → production recommendation → artisan action, combined with government intervention intelligence."

---

# 40. Judge Question — "Where does your data come from?"

Recommended answer:

> "We do not claim access to private marketplace transaction data. Our architecture separates verified transaction data, partner-provided data, public market signals and simulated demo data. The prototype demonstrates the intelligence pipeline using controlled datasets, while the production architecture can ingest authorized seller and network data as integrations become available."

---

# 41. Judge Question — "What if AI is wrong?"

Recommended answer:

> "We use confidence-aware extraction. High-confidence attributes can be auto-filled, while low-confidence attributes require artisan confirmation. Recommendations also expose their evidence and confidence level. The system is decision support, not an authority."

---

# 42. Judge Question — "Why should the government deploy you?"

Recommended answer:

> "We don't just show government officers sales dashboards. We identify which SHGs need support, what problem they have, and what intervention should be prioritized. This converts fragmented commerce data into actionable program-management intelligence."

---

# 43. Judge Question — "What is your moat?"

Recommended answer:

> "The moat is not the LLM or voice recognition model. It is the structured artisan commerce graph and the closed-loop feedback system connecting artisan capability, product attributes, market signals, prices, inventory, production recommendations and government interventions."

---

# 44. Measurable KPIs

Track:

- Listing creation time
- Percentage of listings completed
- Listing Health Score
- Average cataloguing time
- Number of channels reached
- Percentage of AI fields requiring correction
- Price recommendation acceptance rate
- Market recommendation accuracy
- Demand-to-inventory match rate
- Production recommendation usefulness
- Officer intervention time
- Number of SHGs identified for support

---

# 45. Suggested Impact Metrics for the Demo

Demonstrate:

### Before KARIGAR AI

> 15–30 minutes to create a professional listing

### After KARIGAR AI

> Target: under 2 minutes

---

### Before

> Manual form filling

### After

> Natural voice conversation

---

### Before

> Guessing price

### After

> Cost + fair labour + market intelligence

---

### Before

> "I think this product will sell."

### After

> "The system identifies three target markets and explains why."

---

### Before

> Officer sees sales numbers.

### After

> Officer receives prioritized intervention recommendations.

---

# 46. Long-Term Roadmap

## Phase 1 — SIH Prototype

- Voice cataloguing
- Listing Health
- Fair Price
- Market Opportunity
- Production Recommendation
- Officer dashboard
- Intervention AI

## Phase 2 — Pilot

- SHG/federation integration
- Real seller data
- More languages
- Offline support
- ONDC integration
- WhatsApp

## Phase 3 — Ecosystem

- More commerce networks
- Government APIs
- GI/identity verification
- Logistics intelligence
- Advanced demand forecasting
- Cluster-level production planning

---

# 47. Final Product Definition

## KARIGAR AI

### AI Commerce Copilot for India's Marginalized Artisans

KARIGAR AI sits between artisans and India's existing digital-commerce ecosystem.

It understands artisans through voice and images, converts their products into structured digital catalogues, evaluates listing quality, calculates sustainable prices, identifies promising markets, recommends what they should produce next, and continuously learns from business outcomes.

For government and SHG federations, the same system transforms fragmented artisan-commerce information into an AI command centre that identifies underperforming listings, emerging demand, underpricing and artisan groups requiring intervention.

The system does not replace ONDC, eSARAS, IndiaHandmade, Amazon, Flipkart or other commerce infrastructure.

> **It makes that infrastructure intelligent and usable for the people who need it most.**

---

# 48. Final One-Line Pitch

> **KARIGAR AI is an AI Commerce Copilot that doesn't just help artisans list products—it tells them what to sell, where to sell it, what price to charge, what to make next, and tells governments which artisan groups need help.**

---

# 49. Final Winning Message

# FROM LISTING AI → TO DECISION AI

### Product

**What do I have?**

↓

### Listing

**How should I sell it?**

↓

### Market

**Where should I sell it?**

↓

### Price

**What should I charge?**

↓

### Production

**What should I make next?**

↓

### Government

**Who needs support?**

↓

# CONTINUOUSLY IMPROVE ARTISAN LIVELIHOODS

---

# 49A. Wage-Data Implementation Rule

The wage benchmark is a **time-sensitive regulatory input**.

For the SIH prototype:

- Store the benchmark in the database.
- Display its effective date.
- Display its source.
- Mark it as a proxy if the exact occupation-specific schedule has not been verified.
- Use ₹550/day only as the midpoint demo benchmark described above.
- Do not describe ₹550/day as the exact statutory wage for Kondapalli toy-making.
- For production deployment, load the exact applicable state + occupation + category + zone notification.

This protects the project from the judge objection:

> "Where did that wage number come from?"

The application should be able to answer that question directly on the pricing screen.

---

# 50. Research Sources

The competitive strategy should be grounded in primary or authoritative sources wherever possible.

## Government / Infrastructure

- ONDC — Seller Network Participants  
  https://www.ondc.org/pages/seller-network-participants.html

- ONDC — Impact / Grassroots Commerce  
  https://www.ondc.org/pages/impact-retail.html

- PIB — eSARAS / DAY-NRLM ecosystem  
  https://www.pib.gov.in/PressReleasePage.aspx?PRID=2279692&lang=1&reg=6

- Digital India — IndiaHandmade  
  https://www.digitalindia.gov.in/initiative/india-handmade/

- IP India — Geographical Indications  
  https://ipindia.gov.in/geographical-indications-before-you-apply-forms

- Smart India Hackathon problem statement  
  https://sih26ps.vercel.app/

## Commercial / Competitive Research

- Artisans' Wizard  
  https://www.artisanswizard.com/

- HeritageVastra  
  https://www.heritagevastra.com/

- KalaHubIndia  
  https://kalahubindia.com/about

- KalaMitra  
  https://www.kalamitra.store/about

- Amazon Saheli  
  https://sell.amazon.in/grow-your-business/amazon-saheli

- Flipkart Samarth  
  https://stories.flipkart.com/flipkart-samarth-indian-artisans-weavers-craftsmen

## Research / Technical Evidence

- Engineering for Change — Voice Recognition for Rural Textile Producers / Gram Sootra  
  https://www.engineeringforchange.org/projects/voice-recognition-feature-for-rural-textile-producers/

- 2026 research on voice-first AI artisan marketplaces  
  https://www.jetir.org/view?paper=JETIR2608006

---

# Final Strategic Decision

## BUILD

**KARIGAR AI — AI Commerce Copilot**

## DO NOT BUILD

Another artisan marketplace.

## CORE INNOVATION

**Closed-loop decision intelligence.**

## HERO DEMO

> "What should I make next?"

## GOVERNMENT WOW MOMENT

> "Which SHGs should we help first?"

## TECHNICAL WOW MOMENT

> Voice → structured product → confidence → listing health → market intelligence → production recommendation.

## SOCIAL IMPACT WOW MOMENT

> Fair price based on material + labour + market reality rather than arbitrary marketplace pricing.

## FINAL MESSAGE

> **We don't build another marketplace. We build the intelligence layer that helps marginalized artisans succeed across India's digital-commerce ecosystem.**
