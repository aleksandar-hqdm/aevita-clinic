"""
Aevita Clinic Skopje — static site generator
Premium blood filtration & IV wellness clinic targeting Southeastern Europe.

Builds the full Country -> City -> Service matrix as static HTML.
"""
from __future__ import annotations

import html
import os
import shutil
from pathlib import Path
from textwrap import dedent

ROOT = Path(__file__).parent
OUT = ROOT  # write to repo root so GitHub Pages serves from main

# --------------------------------------------------------------------------
# Brand
# --------------------------------------------------------------------------

BRAND = "Aevita Clinic"
BRAND_FULL = "Aevita Clinic Skopje"
TAGLINE = "European medicine. Balkan accessibility."
PHONE = "+389 70 555 100"
PHONE_DIGITS = "+38970555100"
EMAIL = "hello@aevitaclinic.mk"
ADDRESS_STREET = "Bul. 8-mi Septemvri 12"
ADDRESS_CITY = "Skopje 1000"
ADDRESS_COUNTRY = "North Macedonia"
GEO_LAT = "41.9981"
GEO_LNG = "21.4254"
DOMAIN = "https://aleksandar-hqdm.github.io/aevita-clinic"  # GitHub Pages URL
BASE_PATH = "/aevita-clinic"  # subdirectory on aleksandar-hqdm.github.io
WHATSAPP = "38970555100"

FOUNDERS_NOTE = (
    "Founded by Nina &amp; Pape, Aevita Clinic brings German-grade "
    "blood-filtration medicine and physician-led IV therapy to "
    "Southeastern Europe at a fraction of Western prices."
)

# --------------------------------------------------------------------------
# Service taxonomy
# --------------------------------------------------------------------------

CORE_SERVICES = {
    "ebo2-blood-filtration": {
        "name": "EBO2 Blood Filtration",
        "short": "EBO2",
        "category": "Signature Procedure",
        "tagline": "Extracorporeal blood oxygenation &amp; ozonation",
        "lede": (
            "EBO2 is the premium end of medical ozone therapy. We draw "
            "your blood through a closed-loop circuit, filter out "
            "fat-soluble toxins and inflammatory debris, oxygenate and "
            "ozonate it, then return it. One session processes the "
            "equivalent of multiple traditional ozone sessions."
        ),
        "duration": "60–90 minutes",
        "price_eu": "EUR 1,200 – 1,500",
        "price_aevita": "EUR 850 – 1,000",
        "course": "Single session or course of 4–6",
        "downtime": "None — light activity same day",
        "benefits": [
            ("Systemic detoxification",
             "Removes fat-soluble waste and oxidised lipids that "
             "standard liver and kidney pathways clear slowly."),
            ("Oxygen delivery upgrade",
             "Increases the oxygen-carrying capacity of red blood "
             "cells, supporting recovery and cognitive clarity."),
            ("Anti-inflammatory effect",
             "Modulates cytokine signalling, helpful for chronic "
             "fatigue, post-viral syndromes and autoimmune profiles."),
            ("Vascular &amp; circulatory benefit",
             "Reported improvements in peripheral circulation and "
             "endothelial function in published clinical literature."),
        ],
        "best_for": [
            "Post-viral fatigue and long-COVID profiles",
            "Chronic inflammation and autoimmune support",
            "Heavy-metal and environmental toxin burden",
            "Athletes seeking recovery acceleration",
            "Executives running on chronic stress load",
        ],
        "process": [
            ("Intake &amp; bloodwork review",
             "Internal-medicine consultation, full panel review, "
             "candidacy confirmation."),
            ("IV access &amp; closed-loop setup",
             "Sterile cannulation and connection to the EBO2 device "
             "under anaesthesiology supervision."),
            ("Filtration cycle",
             "Blood passes through the medical filter, is oxygenated "
             "and ozonated in a sealed circuit, then returned."),
            ("Recovery lounge",
             "20–30 minutes in our recovery lounge with vitals "
             "monitoring and post-procedure debrief."),
        ],
        "faqs": [
            ("Is EBO2 the same as ozone therapy?",
             "No. Standard ozone (MAH) uses a small blood volume "
             "drawn into a bottle, ozonated, and returned. EBO2 runs "
             "your entire circulating volume through a medical filter "
             "and ozonator in a continuous closed loop — far higher "
             "throughput and a filtration step that MAH does not "
             "have."),
            ("Is it safe?",
             "EBO2 is performed by licensed physicians under "
             "anaesthesiology supervision in a registered Private "
             "Health Institution (PZU). We follow strict blood-"
             "handling, sterilisation and emergency protocols."),
            ("How many sessions will I need?",
             "Many patients book a single session for an event or "
             "travel. For chronic conditions we recommend a course "
             "of 4–6 sessions across 2–4 weeks; your physician will "
             "advise after the intake."),
            ("Can I fly in for treatment?",
             "Yes. Most international patients arrive in Skopje, "
             "complete intake and treatment within 24–48 hours, and "
             "fly home. We coordinate hotel, airport transfer and "
             "post-procedure follow-up."),
        ],
    },
    "mah-ozone-therapy": {
        "name": "MAH Ozone Therapy",
        "short": "MAH",
        "category": "Core Therapy",
        "tagline": "Major autohaemotherapy — the classical ozone protocol",
        "lede": (
            "MAH (Major Autohaemotherapy) is the European clinical "
            "standard for medical ozone. We draw a defined volume of "
            "blood, expose it to a precisely dosed ozone-oxygen "
            "mixture, and reinfuse it. It is the most studied ozone "
            "modality with decades of clinical data."
        ),
        "duration": "30–45 minutes",
        "price_eu": "EUR 180 – 250",
        "price_aevita": "EUR 110 – 150",
        "course": "Typical course: 8–10 sessions",
        "downtime": "None",
        "benefits": [
            ("Immune modulation",
             "Stimulates antioxidant defences and balances Th1/Th2 "
             "immune signalling."),
            ("Energy &amp; circulation",
             "Improves tissue oxygenation and red-cell flexibility."),
            ("Antimicrobial activity",
             "Adjunct support in chronic infections and dysbiosis."),
            ("Anti-aging signalling",
             "Upregulates Nrf2 pathway, the body's master "
             "antioxidant response."),
        ],
        "best_for": [
            "Recurrent infections and immune weakness",
            "Chronic fatigue, brain fog, low-grade inflammation",
            "Circulatory issues and metabolic syndrome",
            "Maintenance protocols after a course of EBO2",
        ],
        "process": [
            ("Intake",
             "Brief physician consultation, vitals check, "
             "contraindication screen."),
            ("Blood draw",
             "Defined volume drawn into a medical-grade ozone-"
             "resistant container."),
            ("Ozonation",
             "Precise ozone-oxygen mixture delivered at the dose "
             "your physician has prescribed."),
            ("Reinfusion",
             "Treated blood is returned by gravity drip; total "
             "chair time around 30–45 minutes."),
        ],
        "faqs": [
            ("How does MAH compare to EBO2?",
             "MAH is the entry tier — smaller blood volume, no "
             "filtration step, lower cost, more sessions per course. "
             "EBO2 is the premium tier — full circulating volume, "
             "active filtration, fewer sessions needed."),
            ("Are there side effects?",
             "Most patients feel mild fatigue for a few hours after "
             "the first sessions as detoxification activates. We "
             "screen for G6PD deficiency and other contraindications "
             "before starting."),
            ("Can MAH be combined with IV therapy?",
             "Yes — many patients add a Myers' Cocktail or "
             "Glutathione push on the same day for compounded benefit."),
        ],
    },
    "iv-therapy": {
        "name": "IV Therapy Lounge",
        "short": "IV",
        "category": "Therapy Hub",
        "tagline": "Physician-supervised IV drips and pushes",
        "lede": (
            "Our IV lounge runs the full library of clinical drip "
            "protocols, every one supervised by a licensed physician "
            "and compounded fresh from EU-sourced pharmaceutical-grade "
            "ingredients."
        ),
        "duration": "30–90 minutes per drip",
        "price_eu": "EUR 150 – 600",
        "price_aevita": "EUR 90 – 420",
        "course": "Single drip or membership",
        "downtime": "None",
        "benefits": [
            ("Bioavailability",
             "100% absorption — no gut losses, no first-pass liver "
             "metabolism."),
            ("Speed",
             "Therapeutic plasma levels within minutes, not days of "
             "oral supplementation."),
            ("Physician-led dosing",
             "Every protocol is reviewed by a doctor against your "
             "intake form and recent bloodwork."),
            ("Comfort",
             "Recliners, warmed blankets, refreshments — closer to a "
             "premium lounge than a treatment room."),
        ],
        "best_for": [
            "Energy crashes and burnout recovery",
            "Pre- and post-flight, jet lag, dehydration",
            "Athletic events, recovery weeks",
            "Skin, hair, anti-aging programs",
            "Immune support during travel or illness exposure",
        ],
        "process": [
            ("Intake",
             "Short questionnaire, blood-pressure check, drip "
             "selection with the physician."),
            ("Setup",
             "Sterile cannulation, warmed blanket, settle into "
             "recliner."),
            ("Drip",
             "30–90 minutes depending on protocol; refreshments "
             "available."),
            ("Post-drip",
             "Vitals re-check, hydration, return to your day."),
        ],
        "faqs": [
            ("Do I need bloodwork first?",
             "For most lounge drips a brief intake is enough. For "
             "NAD+ courses and Glutathione pushes we ask for recent "
             "bloodwork or run a basic panel at the clinic."),
            ("Can I combine drips?",
             "Yes — your physician will sequence them safely. Common "
             "stacks: Myers' + Glutathione push, Vitamin C + Zinc, "
             "NAD+ followed by B-complex."),
            ("Is there a membership?",
             "Yes. Monthly drip memberships and pre-paid courses "
             "carry a 15–20% saving over single drips. Ask your "
             "physician at intake."),
        ],
    },
    "medical-weight-loss": {
        "name": "Medical Weight Loss",
        "short": "GLP-1",
        "category": "Medical Program",
        "tagline": "Physician-supervised GLP-1 program — Wegovy, Ozempic, Mounjaro",
        "lede": (
            "Our medical weight-loss program uses GLP-1 receptor "
            "agonists (semaglutide and tirzepatide) prescribed and "
            "monitored by licensed internal-medicine doctors. We "
            "treat obesity and metabolic syndrome as the chronic "
            "medical conditions they are — with bloodwork, dose "
            "titration and structured follow-up."
        ),
        "duration": "12-week starter program",
        "price_eu": "EUR 350 – 600 per month",
        "price_aevita": "EUR 220 – 380 per month",
        "course": "12-week program, then maintenance",
        "downtime": "None — weekly self-administered injection",
        "benefits": [
            ("Clinically validated",
             "Wegovy and Mounjaro show 15–22% mean weight loss in "
             "Phase 3 trials when paired with lifestyle support."),
            ("Appetite recalibration",
             "GLP-1 agonists slow gastric emptying and reduce "
             "food-noise; most patients describe it as a "
             "rebalancing rather than restriction."),
            ("Metabolic upside",
             "Improvements in HbA1c, blood pressure, triglycerides "
             "and liver enzymes in the published evidence base."),
            ("Physician-supervised",
             "Dose titration, side-effect management and bloodwork "
             "every 4 weeks — not a black-market prescription."),
        ],
        "best_for": [
            "BMI 30+ or BMI 27+ with metabolic comorbidities",
            "Pre-diabetes and Type 2 diabetes management",
            "Plateau after diet and exercise programs",
            "Patients seeking medical supervision, not online scripts",
        ],
        "process": [
            ("Intake &amp; bloodwork",
             "Full metabolic panel, HbA1c, lipids, liver, thyroid, "
             "contraindication screen."),
            ("Prescription &amp; first dose",
             "Physician prescription, first injection administered "
             "in clinic, technique training for self-administration."),
            ("Weekly self-administration",
             "Subcutaneous injection at home, weekly. We supply the "
             "medication monthly."),
            ("4-week reviews",
             "In-person or telemedicine check-ins, dose titration, "
             "side-effect management, repeat bloodwork at week 12."),
        ],
        "faqs": [
            ("Wegovy or Ozempic — what's the difference?",
             "Ozempic and Wegovy are both semaglutide. Ozempic is "
             "licensed for Type 2 diabetes; Wegovy for chronic "
             "weight management. Mounjaro is tirzepatide — a dual "
             "GIP/GLP-1 agonist with stronger weight-loss outcomes "
             "in head-to-head trials. Your physician will recommend "
             "based on your profile."),
            ("Will I gain it back if I stop?",
             "Obesity is a chronic condition. Discontinuation "
             "without behavioural change typically results in "
             "partial regain. Our program builds the nutrition and "
             "movement scaffolding so you can step down "
             "progressively, not crash off."),
            ("What about side effects?",
             "Nausea, mild reflux and constipation are the common "
             "ones, usually limited to the titration weeks. Serious "
             "side effects are rare. We screen for pancreatitis "
             "history, MTC and MEN-2 contraindications at intake."),
            ("Is this available to international patients?",
             "Yes. Many of our patients fly in for the intake "
             "consultation and bloodwork, then we ship monthly "
             "supplies and run reviews via telemedicine. Local "
             "delivery is available across the EU."),
        ],
    },
}

IV_DRIPS = {
    "nad-plus-iv": {
        "name": "NAD+ Anti-Aging IV",
        "short": "NAD+",
        "tagline": "Cellular energy &amp; longevity infusion",
        "lede": (
            "Nicotinamide Adenine Dinucleotide (NAD+) is the coenzyme "
            "your mitochondria run on. Levels fall measurably with "
            "age. Direct IV NAD+ bypasses the absorption bottleneck "
            "of oral precursors and rebuilds cellular fuel."
        ),
        "duration": "2–4 hours",
        "dose": "250 mg / 500 mg / 1000 mg options",
        "price": "EUR 280 – 580 per session",
        "best_for": [
            "Cognitive performance and focus",
            "Recovery from burnout, post-viral fatigue",
            "Longevity and biological-age protocols",
            "Athletic recovery between hard blocks",
        ],
        "stack_with": ["myers-cocktail-iv", "glutathione-iv"],
    },
    "myers-cocktail-iv": {
        "name": "Myers' Cocktail",
        "short": "Myers'",
        "tagline": "The classical wellness drip — magnesium, B-complex, C",
        "lede": (
            "The original physician-designed wellness infusion. "
            "High-dose magnesium, the full B-complex, vitamin C and "
            "calcium in a 60-minute drip — the protocol Dr. John "
            "Myers refined in Baltimore in the 1970s and the most "
            "ordered drip in IV medicine today."
        ),
        "duration": "45–60 minutes",
        "dose": "Standard Myers' protocol",
        "price": "EUR 95 – 130 per session",
        "best_for": [
            "Energy crashes and chronic fatigue",
            "Migraine and tension-headache prevention",
            "Fibromyalgia symptom relief",
            "General immune and recovery support",
        ],
        "stack_with": ["glutathione-iv", "immune-booster-iv"],
    },
    "glutathione-iv": {
        "name": "Glutathione Detox IV",
        "short": "Glutathione",
        "tagline": "Master antioxidant — liver, skin, detoxification",
        "lede": (
            "Glutathione is the body's master antioxidant. Oral "
            "supplementation barely moves serum levels — IV pushes "
            "deliver clinically meaningful concentrations directly "
            "to where they're used."
        ),
        "duration": "30 minutes (push) or 45 min (drip)",
        "dose": "1200 mg / 2000 mg options",
        "price": "EUR 110 – 180 per session",
        "best_for": [
            "Liver support and detoxification programs",
            "Skin brightening and pigmentation protocols",
            "Heavy-metal and oxidative-stress reduction",
            "Post-alcohol, post-travel reset",
        ],
        "stack_with": ["myers-cocktail-iv", "nad-plus-iv"],
    },
    "immune-booster-iv": {
        "name": "Immune Booster IV",
        "short": "Immune",
        "tagline": "High-dose vitamin C, zinc, selenium",
        "lede": (
            "A clinically dosed vitamin C drip with zinc and "
            "selenium for acute immune support — far higher serum "
            "levels than oral can reach, used before exposure-heavy "
            "travel or at the first symptom of a cold."
        ),
        "duration": "60–90 minutes",
        "dose": "15 g / 25 g vitamin C options",
        "price": "EUR 90 – 180 per session",
        "best_for": [
            "Pre-flight and pre-event immune loading",
            "Acute upper-respiratory symptom onset",
            "Post-viral recovery acceleration",
            "Patients in high-exposure professions",
        ],
        "stack_with": ["myers-cocktail-iv", "glutathione-iv"],
    },
    "energy-b-complex-iv": {
        "name": "Energy &amp; B-Complex IV",
        "short": "Energy",
        "tagline": "B-complex, B12, taurine, electrolytes",
        "lede": (
            "A focused energy drip — methylated B-vitamins, "
            "high-dose B12, taurine and electrolytes for mental "
            "clarity and physical drive. The single most-requested "
            "drip on Monday mornings."
        ),
        "duration": "30–45 minutes",
        "dose": "Standard energy protocol",
        "price": "EUR 80 – 110 per session",
        "best_for": [
            "Monday-morning resets after a hard weekend",
            "Vegetarian and vegan B12 maintenance",
            "Chronic fatigue and brain fog",
            "Stress and adrenal support",
        ],
        "stack_with": ["nad-plus-iv", "myers-cocktail-iv"],
    },
    "beauty-collagen-iv": {
        "name": "Beauty &amp; Collagen IV",
        "short": "Beauty",
        "tagline": "Biotin, glutathione, vitamin C, hyaluronic acid",
        "lede": (
            "An aesthetic medicine drip pairing high-dose biotin and "
            "vitamin C with a glutathione push and hyaluronic acid "
            "co-factors — designed for skin clarity, hair quality "
            "and the visible markers of inflammation."
        ),
        "duration": "60 minutes",
        "dose": "Standard beauty protocol",
        "price": "EUR 130 – 180 per session",
        "best_for": [
            "Skin brightening and pigmentation",
            "Hair quality and nail strength",
            "Anti-inflammatory aesthetic protocols",
            "Pre-event glow",
        ],
        "stack_with": ["glutathione-iv", "myers-cocktail-iv"],
    },
    "athletic-recovery-iv": {
        "name": "Athletic Performance &amp; Recovery IV",
        "short": "Recovery",
        "tagline": "Amino acids, magnesium, B-complex, electrolytes",
        "lede": (
            "Built for athletes in heavy training blocks and "
            "weekend warriors recovering from a hard race or match. "
            "Branched-chain amino acids, magnesium, electrolytes and "
            "vitamin C in a 60-minute drip."
        ),
        "duration": "60 minutes",
        "dose": "Standard recovery protocol",
        "price": "EUR 120 – 160 per session",
        "best_for": [
            "Marathon, triathlon, cycling event recovery",
            "Crossfit and strength-block deload weeks",
            "Football and team-sport in-season maintenance",
            "Acute soft-tissue inflammation",
        ],
        "stack_with": ["myers-cocktail-iv", "nad-plus-iv"],
    },
    "hangover-recovery-iv": {
        "name": "Hangover Recovery IV",
        "short": "Hangover",
        "tagline": "Rehydration, B-complex, anti-nausea, glutathione",
        "lede": (
            "A clinical-grade rehydration drip — saline, electrolytes, "
            "B-complex, anti-nausea medication and a glutathione push "
            "for the morning after. Most patients walk out feeling "
            "human inside an hour."
        ),
        "duration": "45 minutes",
        "dose": "Standard hangover protocol",
        "price": "EUR 95 – 140 per session",
        "best_for": [
            "Morning after weddings, conferences, big nights",
            "Travel dehydration recovery",
            "Migraine onset relief",
            "Acute viral nausea and dehydration",
        ],
        "stack_with": ["glutathione-iv", "energy-b-complex-iv"],
    },
}

# --------------------------------------------------------------------------
# Geography
# --------------------------------------------------------------------------

LOCATIONS = {
    "north-macedonia": {
        "name": "North Macedonia",
        "name_local": "Северна Македонија",
        "is_home": True,
        "lede": (
            "Aevita's home base. The clinic operates from Skopje and "
            "serves patients from every regional city — we are the "
            "only EBO2-equipped clinic in the country and one of a "
            "handful in the Balkans."
        ),
        "cities": {
            "skopje": {
                "name": "Skopje", "is_hq": True,
                "context": (
                    "Our flagship clinic on Bulevar 8-mi Septemvri, "
                    "12 minutes from Alexander the Great Airport "
                    "(SKP). Patients from Switzerland, Germany and "
                    "Austria are met at the airport with private "
                    "transfer included in the international package."
                ),
            },
            "tetovo": {
                "name": "Tetovo",
                "context": (
                    "45 minutes from the clinic by road. We offer a "
                    "complimentary shuttle for booked patients on "
                    "request and partner with Hotel Lirak for "
                    "overnight stays."
                ),
            },
            "bitola": {
                "name": "Bitola",
                "context": (
                    "Two hours south of Skopje. Many Bitola patients "
                    "combine an EBO2 session with an overnight stay "
                    "at one of our partner boutique hotels in the "
                    "Sirok Sokak quarter."
                ),
            },
            "ohrid": {
                "name": "Ohrid",
                "context": (
                    "Three hours from Skopje, with an airport "
                    "(OHD) seasonal-direct to Vienna and Basel. "
                    "Increasingly the favoured arrival point for "
                    "Swiss patients combining treatment with a "
                    "lake-side stay."
                ),
            },
        },
    },
    "kosovo": {
        "name": "Kosovo",
        "name_local": "Kosova / Косово",
        "lede": (
            "Pristina is 90 minutes from our Skopje clinic. We are "
            "the closest EBO2-equipped facility for Kosovar patients "
            "and the most-booked international corridor outside "
            "Switzerland."
        ),
        "cities": {
            "pristina": {
                "name": "Pristina",
                "context": (
                    "Direct A4/E65 motorway, 90 minutes door-to-door. "
                    "Many Pristina patients arrive in the morning, "
                    "complete a single-session EBO2 with recovery, "
                    "and are home for dinner."
                ),
            },
            "prizren": {
                "name": "Prizren",
                "context": (
                    "Two hours from Skopje via the A2/E65. We "
                    "coordinate a same-day return for most Prizren "
                    "EBO2 patients and offer accommodation packages "
                    "for full IV courses."
                ),
            },
            "peja": {
                "name": "Peja / Peć",
                "context": (
                    "Two and a half hours. We recommend an "
                    "overnight stay in Skopje for Peja patients "
                    "booked for EBO2 or NAD+ protocols, included "
                    "in the international care package."
                ),
            },
        },
    },
    "albania": {
        "name": "Albania",
        "name_local": "Shqipëria",
        "lede": (
            "Tirana to Skopje is a four-hour drive on the A1/SH3 "
            "corridor, or a one-hour flight via Vienna. Aevita is the "
            "closest EBO2-equipped clinic in the Western Balkans for "
            "Albanian patients."
        ),
        "cities": {
            "tirana": {
                "name": "Tirana",
                "context": (
                    "Four hours by road or a single-stop flight from "
                    "Rinas (TIA). Most Tirana patients schedule a "
                    "two-night Skopje stay covering intake, "
                    "treatment and post-care follow-up."
                ),
            },
            "durres": {
                "name": "Durrës",
                "context": (
                    "Add 40 minutes to the Tirana corridor. "
                    "Durrës patients often combine treatment with a "
                    "rest stop in Ohrid, which is roughly halfway."
                ),
            },
            "vlora": {
                "name": "Vlorë",
                "context": (
                    "A longer corridor — most Vlorë patients fly "
                    "Tirana–Skopje. We coordinate airport transfer "
                    "and a recovery hotel as part of the "
                    "international care package."
                ),
            },
        },
    },
    "serbia": {
        "name": "Serbia",
        "name_local": "Србија",
        "lede": (
            "Belgrade to Skopje is a four-and-a-half-hour drive on "
            "the E75 corridor or a one-hour direct flight. We are "
            "the closest EBO2 clinic south of the Sava — a real "
            "alternative to flying to Vienna or Zurich."
        ),
        "cities": {
            "belgrade": {
                "name": "Belgrade",
                "context": (
                    "Direct Air Serbia and Wizz Air flights to "
                    "Skopje several times weekly. Most Belgrade "
                    "patients fly in the morning, complete "
                    "treatment and recovery, and fly home the same "
                    "evening or next morning."
                ),
            },
            "novi-sad": {
                "name": "Novi Sad",
                "context": (
                    "Add 90 minutes to the Belgrade corridor. We "
                    "recommend the one-night Skopje package for "
                    "Novi Sad patients booked on EBO2 or NAD+ "
                    "courses."
                ),
            },
            "nis": {
                "name": "Niš",
                "context": (
                    "Two and a half hours from Skopje on the E75. "
                    "The shortest Serbian corridor — many Niš "
                    "patients drive down for a single EBO2 session "
                    "and return the same day."
                ),
            },
        },
    },
    "bulgaria": {
        "name": "Bulgaria",
        "name_local": "България",
        "lede": (
            "Sofia is three and a half hours from Skopje on the A4 "
            "corridor. Aevita is the only EBO2-equipped facility in "
            "the immediate region — Bulgarian patients save the long "
            "flight to Vienna or Munich."
        ),
        "cities": {
            "sofia": {
                "name": "Sofia",
                "context": (
                    "Direct motorway corridor in three and a half "
                    "hours, or 45-minute flight. We coordinate "
                    "airport transfer and recovery accommodation "
                    "for full-course bookings."
                ),
            },
            "plovdiv": {
                "name": "Plovdiv",
                "context": (
                    "Five hours by road via Sofia. We recommend the "
                    "two-night Skopje package for Plovdiv patients "
                    "to allow proper recovery before the return "
                    "drive."
                ),
            },
            "burgas": {
                "name": "Burgas",
                "context": (
                    "Easiest by air via Sofia. We coordinate the "
                    "full travel package including domestic transfer "
                    "and recovery hotel in Skopje."
                ),
            },
        },
    },
    "montenegro": {
        "name": "Montenegro",
        "name_local": "Crna Gora / Црна Гора",
        "lede": (
            "Podgorica to Skopje is a five-hour drive via Pristina "
            "or a one-stop flight. We hold exclusivity for our "
            "EBO2 device across North Macedonia, Kosovo and "
            "Montenegro — the only authorised clinic in the region."
        ),
        "cities": {
            "podgorica": {
                "name": "Podgorica",
                "context": (
                    "Most Podgorica patients fly via Belgrade or "
                    "Vienna. We coordinate the full international "
                    "care package: flights guidance, transfer, "
                    "two-night recovery stay, post-procedure "
                    "follow-up."
                ),
            },
            "budva": {
                "name": "Budva",
                "context": (
                    "Coastal patients typically fly Tivat–Belgrade–"
                    "Skopje. We work with a local concierge "
                    "partner to handle ground logistics on both "
                    "ends."
                ),
            },
            "kotor": {
                "name": "Kotor",
                "context": (
                    "Same Tivat–Belgrade–Skopje routing as Budva. "
                    "Recovery package includes a two-night Skopje "
                    "stay in our partner hotel."
                ),
            },
        },
    },
    "bosnia-herzegovina": {
        "name": "Bosnia &amp; Herzegovina",
        "name_local": "Bosna i Hercegovina",
        "lede": (
            "Sarajevo to Skopje is a six-hour drive or a one-stop "
            "flight. Aevita is the nearest EBO2-equipped facility "
            "for Bosnian patients — a meaningful alternative to "
            "the standard Vienna and Munich corridors."
        ),
        "cities": {
            "sarajevo": {
                "name": "Sarajevo",
                "context": (
                    "One-stop flight via Vienna or Belgrade. We "
                    "coordinate the full travel package and "
                    "two-night Skopje recovery stay."
                ),
            },
            "banja-luka": {
                "name": "Banja Luka",
                "context": (
                    "Fly Banja Luka–Belgrade–Skopje. We coordinate "
                    "transfer and recovery accommodation in our "
                    "partner hotel network."
                ),
            },
            "mostar": {
                "name": "Mostar",
                "context": (
                    "Drive to Sarajevo and fly, or a long road "
                    "transfer via Podgorica. We recommend the "
                    "two-night Skopje package for proper recovery."
                ),
            },
        },
    },
}

# Western markets — source-market landing pages
SOURCE_MARKETS = {
    "switzerland": {
        "name": "Switzerland",
        "lede": (
            "Swiss patients are our highest-volume source market. "
            "Most book EBO2 in Skopje because the same procedure in "
            "Zurich or Geneva runs CHF 1,800–2,400 — Aevita delivers "
            "the same German-manufactured device, the same medical "
            "protocols, with German-speaking physician support at "
            "30% of the price."
        ),
        "route": "Direct Wizz Air: Basel–Skopje and Zurich–Skopje seasonal",
    },
    "austria": {
        "name": "Austria",
        "lede": (
            "Vienna to Skopje is a one-hour direct flight on Wizz "
            "Air or Austrian. Vienna is the European leader in "
            "ozone medicine and our protocols are aligned with the "
            "Austrian Medical Society for Ozone Therapy guidelines."
        ),
        "route": "Direct Austrian / Wizz Air: Vienna–Skopje daily",
    },
    "germany": {
        "name": "Germany",
        "lede": (
            "Germany invented modern medical ozone — and the EBO2 "
            "device we use is German-manufactured to German medical "
            "standards. Frankfurt, Munich and Düsseldorf all have "
            "direct flights to Skopje. We deliver the same protocol "
            "as the leading German clinics for 30–40% less."
        ),
        "route": "Direct Lufthansa / Wizz Air: Frankfurt, Munich, Düsseldorf, Berlin–Skopje",
    },
}

# --------------------------------------------------------------------------
# Template helpers
# --------------------------------------------------------------------------

CSS = r"""
:root {
  --teal-900: #0a3f3d;
  --teal-700: #155957;
  --teal-500: #1f7d79;
  --teal-100: #d8e8e6;
  --teal-50: #eef4f3;
  --gold: #b8935f;
  --gold-dark: #8f6e3f;
  --gold-light: #e7d4b3;
  --cream: #faf7f1;
  --warm-white: #fefdfb;
  --ink: #14201f;
  --ink-soft: #4c5856;
  --line: #e5dccc;
  --line-soft: #f0e9da;
  --danger: #b54a3a;
  --shadow-sm: 0 1px 2px rgba(20,32,31,.06);
  --shadow: 0 8px 28px -12px rgba(20,32,31,.18);
  --shadow-lg: 0 24px 60px -24px rgba(20,32,31,.28);
  --radius: 4px;
  --radius-lg: 10px;
  --container: 1180px;
}

* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  margin: 0;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  font-size: 16px;
  line-height: 1.65;
  color: var(--ink);
  background: var(--cream);
  -webkit-font-smoothing: antialiased;
}
img { max-width: 100%; height: auto; display: block; }
a { color: var(--teal-700); text-decoration: none; transition: color .15s; }
a:hover { color: var(--gold-dark); }

h1, h2, h3, h4, h5 {
  font-family: 'Cormorant Garamond', 'Garamond', Georgia, serif;
  font-weight: 500;
  color: var(--teal-900);
  line-height: 1.15;
  margin: 0 0 .6em;
  letter-spacing: -0.005em;
}
h1 { font-size: clamp(2.2rem, 4.5vw, 3.6rem); font-weight: 500; }
h2 { font-size: clamp(1.8rem, 3.2vw, 2.6rem); }
h3 { font-size: 1.45rem; font-weight: 600; }
h4 { font-size: 1.15rem; font-weight: 600; }
p { margin: 0 0 1em; color: var(--ink-soft); }
strong { color: var(--ink); font-weight: 600; }

.container {
  max-width: var(--container);
  margin: 0 auto;
  padding: 0 24px;
}

/* Utility bar */
.utility-bar {
  background: var(--teal-900);
  color: var(--teal-100);
  font-size: 13px;
  padding: 8px 0;
  letter-spacing: 0.01em;
}
.utility-bar .container {
  display: flex;
  justify-content: space-between;
  gap: 24px;
  flex-wrap: wrap;
}
.utility-bar a { color: var(--cream); }
.utility-bar a:hover { color: var(--gold-light); }
.utility-bar .langs { color: var(--teal-100); }
.utility-bar .langs span { padding: 0 4px; opacity: .65; }

/* Header */
.site-header {
  background: var(--warm-white);
  border-bottom: 1px solid var(--line);
  position: sticky;
  top: 0;
  z-index: 50;
  box-shadow: var(--shadow-sm);
}
.site-header .container {
  display: flex;
  align-items: center;
  gap: 28px;
  padding-top: 16px;
  padding-bottom: 16px;
}
.brand {
  display: flex;
  align-items: center;
  gap: 12px;
  flex-shrink: 0;
  text-decoration: none;
}
.brand-mark {
  width: 36px; height: 36px;
  border-radius: 50%;
  background: linear-gradient(135deg, var(--teal-500), var(--teal-900));
  display: grid;
  place-items: center;
  color: var(--gold-light);
  font-family: 'Cormorant Garamond', serif;
  font-size: 20px;
  font-weight: 600;
  letter-spacing: -0.02em;
}
.brand-text {
  display: flex;
  flex-direction: column;
  line-height: 1.1;
}
.brand-text .name {
  font-family: 'Cormorant Garamond', serif;
  font-size: 22px;
  color: var(--teal-900);
  font-weight: 600;
  letter-spacing: 0.01em;
}
.brand-text .loc {
  font-size: 10px;
  color: var(--gold-dark);
  text-transform: uppercase;
  letter-spacing: 0.18em;
}
.site-nav {
  flex: 1;
  display: flex;
  gap: 26px;
  font-size: 14px;
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 0.06em;
}
.site-nav a {
  color: var(--ink);
  padding: 8px 0;
  border-bottom: 1px solid transparent;
}
.site-nav a:hover {
  color: var(--teal-700);
  border-bottom-color: var(--gold);
}
.btn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 12px 22px;
  font-weight: 600;
  font-size: 14px;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  border: 1px solid transparent;
  border-radius: var(--radius);
  transition: all .2s;
  cursor: pointer;
  text-decoration: none;
  white-space: nowrap;
}
.btn-primary {
  background: var(--teal-700);
  color: var(--cream);
}
.btn-primary:hover {
  background: var(--teal-900);
  color: var(--gold-light);
}
.btn-gold {
  background: var(--gold);
  color: var(--warm-white);
}
.btn-gold:hover {
  background: var(--gold-dark);
  color: var(--warm-white);
}
.btn-ghost {
  background: transparent;
  color: var(--teal-700);
  border-color: var(--teal-700);
}
.btn-ghost:hover {
  background: var(--teal-700);
  color: var(--cream);
}
.btn-light {
  background: transparent;
  color: var(--cream);
  border-color: var(--gold-light);
}
.btn-light:hover {
  background: var(--gold-light);
  color: var(--teal-900);
}

/* Hero */
.hero {
  background: linear-gradient(135deg, var(--teal-900) 0%, var(--teal-700) 100%);
  color: var(--cream);
  padding: 100px 0 110px;
  position: relative;
  overflow: hidden;
}
.hero::before {
  content: '';
  position: absolute;
  inset: 0;
  background:
    radial-gradient(circle at 90% 10%, rgba(184,147,95,0.15) 0%, transparent 40%),
    radial-gradient(circle at 10% 90%, rgba(184,147,95,0.08) 0%, transparent 50%);
  pointer-events: none;
}
.hero .container { position: relative; }
.eyebrow {
  display: inline-block;
  font-size: 12px;
  font-weight: 600;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: var(--gold-light);
  margin-bottom: 22px;
  padding-bottom: 8px;
  border-bottom: 1px solid var(--gold);
}
.hero h1 {
  color: var(--cream);
  max-width: 820px;
  margin-bottom: 0.4em;
}
.hero h1 em {
  color: var(--gold-light);
  font-style: italic;
}
.hero-lede {
  font-size: 1.2rem;
  line-height: 1.6;
  color: var(--teal-100);
  max-width: 680px;
  margin-bottom: 36px;
}
.hero-actions {
  display: flex;
  gap: 14px;
  flex-wrap: wrap;
}

/* Trust strip */
.trust-strip {
  background: var(--warm-white);
  border-bottom: 1px solid var(--line);
  padding: 28px 0;
}
.trust-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 30px;
}
.trust-item {
  display: flex;
  flex-direction: column;
  gap: 4px;
}
.trust-item .label {
  font-size: 11px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.18em;
  color: var(--gold-dark);
}
.trust-item .value {
  font-family: 'Cormorant Garamond', serif;
  font-size: 1.3rem;
  color: var(--teal-900);
}

/* Section */
section { padding: 80px 0; }
section.tight { padding: 50px 0; }
.section-head {
  max-width: 720px;
  margin-bottom: 50px;
}
.section-head.center {
  text-align: center;
  margin-left: auto;
  margin-right: auto;
}
.section-head .eyebrow {
  color: var(--gold-dark);
  border-color: var(--gold);
}

/* Service cards */
.service-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 28px;
}
.service-card {
  background: var(--warm-white);
  border: 1px solid var(--line);
  border-radius: var(--radius-lg);
  padding: 36px;
  transition: all .25s;
  display: flex;
  flex-direction: column;
  position: relative;
}
.service-card:hover {
  border-color: var(--gold);
  box-shadow: var(--shadow);
  transform: translateY(-2px);
}
.service-card .category {
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--gold-dark);
  margin-bottom: 8px;
}
.service-card h3 {
  margin-bottom: 8px;
}
.service-card .tagline {
  font-style: italic;
  color: var(--teal-700);
  margin-bottom: 16px;
}
.service-card .lede {
  flex: 1;
  font-size: 0.95rem;
}
.service-card .meta {
  display: flex;
  gap: 14px;
  font-size: 0.85rem;
  color: var(--ink-soft);
  border-top: 1px solid var(--line-soft);
  padding-top: 16px;
  margin-top: 16px;
  flex-wrap: wrap;
}
.service-card .meta .pip { color: var(--gold-dark); }
.service-card .more {
  margin-top: 18px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  font-size: 13px;
}
.service-card .more::after { content: ' →'; }

/* Two col */
.two-col {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 60px;
  align-items: start;
}
.two-col.split-7-5 {
  grid-template-columns: 7fr 5fr;
}

/* Boxed sections */
.boxed {
  background: var(--warm-white);
  border: 1px solid var(--line);
  border-radius: var(--radius-lg);
  padding: 40px;
}
.boxed.dark {
  background: var(--teal-900);
  color: var(--cream);
  border: 0;
}
.boxed.dark h2, .boxed.dark h3 { color: var(--cream); }
.boxed.dark p { color: var(--teal-100); }
.boxed.dark .eyebrow { color: var(--gold-light); border-color: var(--gold); }

/* Cards row */
.cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 22px;
}
.card {
  background: var(--warm-white);
  border: 1px solid var(--line);
  border-radius: var(--radius);
  padding: 24px;
}
.card h4 {
  margin-bottom: 8px;
  color: var(--teal-900);
  font-family: 'Cormorant Garamond', serif;
  font-size: 1.2rem;
  font-weight: 600;
}
.card p { font-size: 0.92rem; margin: 0; }

/* Process steps */
.process {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 20px;
  counter-reset: step;
}
.process-step {
  position: relative;
  padding: 26px 22px 22px;
  background: var(--warm-white);
  border: 1px solid var(--line);
  border-radius: var(--radius);
}
.process-step::before {
  counter-increment: step;
  content: counter(step, decimal-leading-zero);
  position: absolute;
  top: -14px;
  left: 22px;
  background: var(--gold);
  color: var(--warm-white);
  font-family: 'Cormorant Garamond', serif;
  font-size: 14px;
  font-weight: 600;
  padding: 2px 10px;
  letter-spacing: 0.1em;
  border-radius: 2px;
}
.process-step h4 {
  margin: 4px 0 6px;
  color: var(--teal-900);
}

/* List with check */
.checklist {
  list-style: none;
  padding: 0;
  margin: 0;
}
.checklist li {
  padding: 10px 0 10px 28px;
  position: relative;
  border-bottom: 1px solid var(--line-soft);
  color: var(--ink);
}
.checklist li:last-child { border-bottom: 0; }
.checklist li::before {
  content: '';
  position: absolute;
  left: 0; top: 18px;
  width: 12px; height: 7px;
  border-left: 2px solid var(--gold);
  border-bottom: 2px solid var(--gold);
  transform: rotate(-45deg);
}

/* FAQ */
.faq details {
  background: var(--warm-white);
  border: 1px solid var(--line);
  border-radius: var(--radius);
  margin-bottom: 12px;
  padding: 0 24px;
  transition: all .2s;
}
.faq details[open] {
  border-color: var(--gold);
  box-shadow: var(--shadow-sm);
}
.faq summary {
  cursor: pointer;
  list-style: none;
  padding: 20px 0;
  font-family: 'Cormorant Garamond', serif;
  font-size: 1.2rem;
  font-weight: 600;
  color: var(--teal-900);
  position: relative;
  padding-right: 32px;
}
.faq summary::-webkit-details-marker { display: none; }
.faq summary::after {
  content: '+';
  position: absolute;
  right: 0; top: 50%;
  transform: translateY(-50%);
  font-size: 1.4rem;
  color: var(--gold-dark);
  font-weight: 300;
}
.faq details[open] summary::after { content: '–'; }
.faq details > div {
  padding: 0 0 22px;
  border-top: 1px solid var(--line-soft);
  padding-top: 18px;
  color: var(--ink-soft);
}

/* Tables */
.table-wrap { overflow-x: auto; }
table.price {
  width: 100%;
  border-collapse: collapse;
  background: var(--warm-white);
  border: 1px solid var(--line);
  border-radius: var(--radius);
  overflow: hidden;
}
table.price th, table.price td {
  padding: 16px 20px;
  text-align: left;
  border-bottom: 1px solid var(--line-soft);
}
table.price th {
  background: var(--teal-50);
  font-weight: 600;
  font-size: 13px;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--teal-900);
}
table.price td.num { text-align: right; }
table.price tr:last-child td { border-bottom: 0; }
table.price tr:hover td { background: var(--teal-50); }
.price-aevita { color: var(--gold-dark); font-weight: 700; }
.price-eu { color: var(--ink-soft); text-decoration: line-through; }

/* Locations grid */
.country-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 20px;
}
.country-card {
  background: var(--warm-white);
  border: 1px solid var(--line);
  border-radius: var(--radius-lg);
  padding: 28px;
  transition: all .2s;
}
.country-card:hover {
  border-color: var(--gold);
  box-shadow: var(--shadow);
}
.country-card h3 {
  margin-bottom: 4px;
  color: var(--teal-900);
}
.country-card .local {
  color: var(--gold-dark);
  font-style: italic;
  font-size: 0.92rem;
  margin-bottom: 14px;
}
.country-card ul {
  list-style: none;
  padding: 0;
  margin: 0;
}
.country-card ul li {
  padding: 6px 0;
  font-size: 0.92rem;
  border-bottom: 1px dotted var(--line);
}
.country-card ul li:last-child { border-bottom: 0; }
.country-card .home-flag {
  display: inline-block;
  background: var(--gold);
  color: var(--warm-white);
  font-size: 10px;
  font-weight: 600;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  padding: 2px 8px;
  border-radius: 2px;
  margin-left: 6px;
}

/* City service matrix */
.matrix {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 16px;
}
.matrix-cell {
  background: var(--warm-white);
  border: 1px solid var(--line);
  padding: 22px;
  border-radius: var(--radius);
  display: flex;
  flex-direction: column;
  gap: 6px;
  transition: all .2s;
}
.matrix-cell:hover {
  border-color: var(--gold);
  box-shadow: var(--shadow-sm);
}
.matrix-cell strong {
  font-family: 'Cormorant Garamond', serif;
  font-size: 1.2rem;
  color: var(--teal-900);
}
.matrix-cell p { font-size: 0.9rem; margin: 0; }

/* Breadcrumb */
.crumbs {
  font-size: 13px;
  color: var(--ink-soft);
  padding: 18px 0;
  background: var(--cream);
  border-bottom: 1px solid var(--line-soft);
}
.crumbs a { color: var(--ink-soft); }
.crumbs a:hover { color: var(--teal-700); }
.crumbs .sep { padding: 0 8px; color: var(--gold-dark); }
.crumbs .current { color: var(--ink); }

/* Final CTA band */
.cta-band {
  background: linear-gradient(135deg, var(--teal-700) 0%, var(--teal-900) 100%);
  color: var(--cream);
  padding: 70px 0;
  text-align: center;
}
.cta-band h2 { color: var(--cream); }
.cta-band p { color: var(--teal-100); max-width: 620px; margin: 0 auto 28px; }

/* Footer */
.site-footer {
  background: var(--teal-900);
  color: var(--teal-100);
  padding: 64px 0 30px;
  font-size: 0.92rem;
}
.site-footer a { color: var(--cream); }
.site-footer a:hover { color: var(--gold-light); }
.footer-grid {
  display: grid;
  grid-template-columns: 1.4fr 1fr 1fr 1fr 1fr;
  gap: 36px;
  padding-bottom: 40px;
  border-bottom: 1px solid rgba(184,147,95,0.2);
}
.site-footer h4 {
  color: var(--gold-light);
  font-family: 'Inter', sans-serif;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  margin-bottom: 18px;
}
.footer-grid ul {
  list-style: none;
  padding: 0;
  margin: 0;
}
.footer-grid ul li { padding: 4px 0; }
.footer-bottom {
  padding-top: 24px;
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 12px;
  font-size: 12px;
  color: var(--teal-100);
  opacity: 0.7;
}
.footer-brand {
  font-family: 'Cormorant Garamond', serif;
  font-size: 22px;
  color: var(--cream);
  margin-bottom: 12px;
}
.footer-disclaimer {
  font-size: 11px;
  color: var(--teal-100);
  opacity: 0.6;
  margin-top: 16px;
  line-height: 1.55;
}

/* Pill list */
.pill-list { display: flex; gap: 8px; flex-wrap: wrap; }
.pill {
  display: inline-block;
  background: var(--teal-50);
  color: var(--teal-700);
  font-size: 12px;
  font-weight: 600;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  padding: 6px 12px;
  border-radius: 100px;
  border: 1px solid var(--teal-100);
}

/* Quote */
blockquote {
  border-left: 3px solid var(--gold);
  padding: 8px 0 8px 24px;
  margin: 24px 0;
  font-family: 'Cormorant Garamond', serif;
  font-size: 1.3rem;
  font-style: italic;
  color: var(--teal-900);
}

/* Mobile */
@media (max-width: 920px) {
  .service-grid,
  .two-col,
  .two-col.split-7-5,
  .trust-grid,
  .footer-grid {
    grid-template-columns: 1fr;
  }
  .site-nav { display: none; }
  .hero { padding: 70px 0 80px; }
  .footer-grid { gap: 28px; }
  .utility-bar { font-size: 11px; }
  section { padding: 56px 0; }
}

/* Print-friendly */
@media print {
  .site-header, .site-footer, .cta-band, .utility-bar { display: none; }
  .hero { background: white; color: black; }
  .hero h1, .hero h1 em, .hero-lede { color: black; }
}
"""


def slugify(s: str) -> str:
    return s.lower().replace(" ", "-").replace("&amp;", "and").replace("&", "and").replace("/", "-")


def url(path: str) -> str:
    """Internal URL — prepends BASE_PATH so GitHub Pages subdir routing works."""
    if path.startswith("http"):
        return path
    if not path.startswith("/"):
        path = "/" + path
    return BASE_PATH + path


def head(title: str, description: str, canonical: str, schema: str = "") -> str:
    """Standard head block."""
    # Source content uses pre-escaped &amp; for body HTML use; unescape
    # here so html.escape() doesn't double-encode in meta tags.
    title = title.replace("&amp;", "&")
    description = description.replace("&amp;", "&")
    canonical_full = DOMAIN + canonical
    og_image = DOMAIN + "/assets/og.jpg"
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(description)}">
<link rel="canonical" href="{canonical_full}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(description)}">
<meta property="og:type" content="website">
<meta property="og:url" content="{canonical_full}">
<meta property="og:image" content="{og_image}">
<meta property="og:site_name" content="{BRAND_FULL}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0a3f3d">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500&family=Inter:wght@400;500;600;700&display=swap">
<link rel="stylesheet" href="{url('/assets/style.css')}">
<link rel="icon" type="image/svg+xml" href="{url('/assets/favicon.svg')}">
{schema}
</head>
"""


def header_block() -> str:
    return f"""
<div class="utility-bar">
  <div class="container">
    <div class="langs">EN<span>·</span>DE<span>·</span>SR<span>·</span>AL<span>·</span>МК<span>·</span>BG</div>
    <div>
      <a href="tel:{PHONE_DIGITS}">{PHONE}</a>
      &nbsp;·&nbsp;
      <a href="mailto:{EMAIL}">{EMAIL}</a>
    </div>
  </div>
</div>
<header class="site-header">
  <div class="container">
    <a class="brand" href="{url('/')}">
      <div class="brand-mark">A</div>
      <div class="brand-text">
        <span class="name">Aevita Clinic</span>
        <span class="loc">Skopje · Southeastern Europe</span>
      </div>
    </a>
    <nav class="site-nav">
      <a href="{url('/services/')}">Services</a>
      <a href="{url('/services/iv-therapy/')}">IV Lounge</a>
      <a href="{url('/services/medical-weight-loss/')}">Weight Loss</a>
      <a href="{url('/locations/')}">Locations</a>
      <a href="{url('/about/')}">About</a>
    </nav>
    <a class="btn btn-gold" href="{url('/consultation/')}">Book Consultation</a>
  </div>
</header>
"""


def footer_block() -> str:
    countries_links = "\n".join(
        f'<li><a href="{url("/locations/" + slug + "/")}">{c["name"]}</a></li>'
        for slug, c in LOCATIONS.items()
    )
    service_links = "\n".join(
        f'<li><a href="{url("/services/" + slug + "/")}">{s["name"]}</a></li>'
        for slug, s in CORE_SERVICES.items()
    )
    iv_links = "\n".join(
        f'<li><a href="{url("/services/iv-therapy/" + slug + "/")}">{d["name"]}</a></li>'
        for slug, d in IV_DRIPS.items()
    )
    return f"""
<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <div class="footer-brand">Aevita Clinic</div>
        <p>{html.escape("Premium blood-filtration and IV wellness medicine in Skopje, North Macedonia. Serving patients from Switzerland, Austria, Germany and the Balkans.").replace("&amp;", "&")}</p>
        <p style="margin-top:12px"><a href="tel:{PHONE_DIGITS}">{PHONE}</a><br>
        <a href="mailto:{EMAIL}">{EMAIL}</a></p>
        <p style="margin-top:6px">{ADDRESS_STREET}<br>{ADDRESS_CITY}, {ADDRESS_COUNTRY}</p>
      </div>
      <div>
        <h4>Core Services</h4>
        <ul>{service_links}</ul>
      </div>
      <div>
        <h4>IV Lounge</h4>
        <ul>{iv_links}</ul>
      </div>
      <div>
        <h4>Locations</h4>
        <ul>{countries_links}</ul>
      </div>
      <div>
        <h4>Clinic</h4>
        <ul>
          <li><a href="{url('/about/')}">About &amp; Founders</a></li>
          <li><a href="{url('/pricing/')}">Pricing</a></li>
          <li><a href="{url('/consultation/')}">Book Consultation</a></li>
          <li><a href="{url('/contact/')}">Contact</a></li>
          <li><a href="{url('/from/switzerland/')}">From Switzerland</a></li>
          <li><a href="{url('/from/germany/')}">From Germany</a></li>
          <li><a href="{url('/from/austria/')}">From Austria</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <div>© 2026 Aevita Clinic Skopje · ПЗУ Аевита</div>
      <div>Licensed Private Health Institution (PZU) · German medical equipment</div>
    </div>
    <p class="footer-disclaimer">
      Medical disclaimer: information on this site is for general
      educational purposes and is not a substitute for medical advice,
      diagnosis or treatment. Procedures discussed are performed
      under licensed physician supervision in our registered Private
      Health Institution. GLP-1 weight-loss medications (Wegovy,
      Ozempic, Mounjaro) are prescription-only and dispensed
      following physician evaluation. Individual results vary.
    </p>
  </div>
</footer>
</body></html>
"""


def crumbs(items: list[tuple[str, str | None]]) -> str:
    """items: [(label, href_or_None)] — last item should have href=None."""
    parts = []
    for i, (label, href) in enumerate(items):
        if href:
            parts.append(f'<a href="{url(href)}">{label}</a>')
        else:
            parts.append(f'<span class="current">{label}</span>')
        if i < len(items) - 1:
            parts.append('<span class="sep">/</span>')
    return f'<div class="crumbs"><div class="container">{"".join(parts)}</div></div>'


def trust_strip() -> str:
    return """
<div class="trust-strip">
  <div class="container">
    <div class="trust-grid">
      <div class="trust-item">
        <span class="label">Equipment</span>
        <span class="value">German-manufactured</span>
      </div>
      <div class="trust-item">
        <span class="label">Staff</span>
        <span class="value">Licensed physicians</span>
      </div>
      <div class="trust-item">
        <span class="label">Registration</span>
        <span class="value">PZU — Private Health Institution</span>
      </div>
      <div class="trust-item">
        <span class="label">Pricing</span>
        <span class="value">25–30% below EU average</span>
      </div>
    </div>
  </div>
</div>
"""


def final_cta(headline="Speak to a physician about your protocol",
              text="A 20-minute consultation with our internal medicine team — review your goals, bloodwork and candidacy. No obligation.") -> str:
    return f"""
<div class="cta-band">
  <div class="container">
    <h2>{headline}</h2>
    <p>{text}</p>
    <div style="display:flex;gap:14px;justify-content:center;flex-wrap:wrap">
      <a class="btn btn-gold" href="{url('/consultation/')}">Book a Consultation</a>
      <a class="btn btn-light" href="tel:{PHONE_DIGITS}">{PHONE}</a>
    </div>
  </div>
</div>
"""


# --------------------------------------------------------------------------
# Schema.org helpers
# --------------------------------------------------------------------------

def schema_medical_business() -> str:
    return f"""<script type="application/ld+json">{{
  "@context": "https://schema.org",
  "@type": "MedicalClinic",
  "name": "{BRAND_FULL}",
  "alternateName": "Aevita Clinic",
  "description": "Premium blood filtration (EBO2), ozone therapy (MAH), IV drips and medical weight loss in Skopje, North Macedonia.",
  "url": "{DOMAIN}/",
  "telephone": "{PHONE}",
  "email": "{EMAIL}",
  "address": {{
    "@type": "PostalAddress",
    "streetAddress": "{ADDRESS_STREET}",
    "addressLocality": "Skopje",
    "postalCode": "1000",
    "addressCountry": "MK"
  }},
  "geo": {{
    "@type": "GeoCoordinates",
    "latitude": "{GEO_LAT}",
    "longitude": "{GEO_LNG}"
  }},
  "medicalSpecialty": ["InternalMedicine", "PreventiveMedicine"],
  "priceRange": "$$$",
  "areaServed": [
    {{"@type": "Country", "name": "North Macedonia"}},
    {{"@type": "Country", "name": "Kosovo"}},
    {{"@type": "Country", "name": "Albania"}},
    {{"@type": "Country", "name": "Serbia"}},
    {{"@type": "Country", "name": "Bulgaria"}},
    {{"@type": "Country", "name": "Montenegro"}},
    {{"@type": "Country", "name": "Bosnia and Herzegovina"}},
    {{"@type": "Country", "name": "Switzerland"}},
    {{"@type": "Country", "name": "Austria"}},
    {{"@type": "Country", "name": "Germany"}}
  ]
}}</script>"""


def schema_procedure(name: str, description: str) -> str:
    return f"""<script type="application/ld+json">{{
  "@context": "https://schema.org",
  "@type": "MedicalProcedure",
  "name": "{name}",
  "description": "{description}",
  "procedureType": "https://schema.org/TherapeuticProcedure",
  "performedBy": {{
    "@type": "MedicalClinic",
    "name": "{BRAND_FULL}",
    "url": "{DOMAIN}/"
  }}
}}</script>"""


def schema_breadcrumb(items: list[tuple[str, str]]) -> str:
    elements = []
    for i, (name, path) in enumerate(items):
        elements.append(
            '{"@type":"ListItem","position":' + str(i + 1) +
            ',"name":"' + name + '","item":"' + DOMAIN + path + '"}')
    return ('<script type="application/ld+json">{"@context":"https://schema.org",'
            '"@type":"BreadcrumbList","itemListElement":[' + ",".join(elements) + ']}</script>')


def schema_faq(faqs: list[tuple[str, str]]) -> str:
    items = []
    for q, a in faqs:
        a_clean = a.replace('"', "'").replace('&amp;', '&')
        q_clean = q.replace('"', "'").replace('&amp;', '&')
        items.append(
            '{"@type":"Question","name":"' + q_clean +
            '","acceptedAnswer":{"@type":"Answer","text":"' + a_clean + '"}}')
    return ('<script type="application/ld+json">{"@context":"https://schema.org",'
            '"@type":"FAQPage","mainEntity":[' + ",".join(items) + ']}</script>')


# --------------------------------------------------------------------------
# Page components
# --------------------------------------------------------------------------

def service_card(slug: str, s: dict) -> str:
    return f"""
<a class="service-card" href="{url(f'/services/{slug}/')}">
  <span class="category">{s['category']}</span>
  <h3>{s['name']}</h3>
  <p class="tagline">{s['tagline']}</p>
  <p class="lede">{s['lede']}</p>
  <div class="meta">
    <span><span class="pip">●</span> {s['duration']}</span>
    <span><span class="pip">●</span> {s['price_aevita']}</span>
  </div>
  <span class="more">Explore protocol</span>
</a>
"""


def iv_card(slug: str, d: dict) -> str:
    return f"""
<a class="service-card" href="{url(f'/services/iv-therapy/{slug}/')}">
  <span class="category">IV Drip · {d['short']}</span>
  <h3>{d['name']}</h3>
  <p class="tagline">{d['tagline']}</p>
  <p class="lede">{d['lede']}</p>
  <div class="meta">
    <span><span class="pip">●</span> {d['duration']}</span>
    <span><span class="pip">●</span> {d['price']}</span>
  </div>
  <span class="more">View drip details</span>
</a>
"""


def country_card(slug: str, c: dict) -> str:
    cities_li = "\n".join(
        f'<li><a href="{url("/locations/" + slug + "/" + cslug + "/")}">{city["name"]}{" — HQ" if city.get("is_hq") else ""}</a></li>'
        for cslug, city in c["cities"].items()
    )
    home = '<span class="home-flag">Home Base</span>' if c.get("is_home") else ""
    return f"""
<div class="country-card">
  <h3>{c['name']} {home}</h3>
  <div class="local">{c['name_local']}</div>
  <ul>{cities_li}</ul>
  <div style="margin-top:14px">
    <a class="more" href="{url('/locations/' + slug + '/')}" style="font-weight:600;font-size:13px;letter-spacing:.08em;text-transform:uppercase">All cities →</a>
  </div>
</div>
"""


def faq_block(faqs: list[tuple[str, str]]) -> str:
    items = "\n".join(
        f'<details><summary>{q}</summary><div>{a}</div></details>'
        for q, a in faqs
    )
    return f'<div class="faq">{items}</div>'


# --------------------------------------------------------------------------
# Page builders
# --------------------------------------------------------------------------

def write_page(path: str, html_str: str):
    full = OUT / path.lstrip("/")
    full.parent.mkdir(parents=True, exist_ok=True)
    full.write_text(html_str, encoding="utf-8")


def page_home():
    schemas = (
        schema_medical_business()
        + schema_breadcrumb([("Home", "/")])
    )
    body = head(
        f"{BRAND_FULL} — EBO2 Blood Filtration, MAH Ozone, IV Therapy &amp; Medical Weight Loss",
        "Premium blood-filtration medicine (EBO2 &amp; MAH ozone), physician-led IV therapy and medical weight loss (Wegovy, Ozempic) in Skopje. Serving Switzerland, Austria, Germany, Kosovo, Albania, Serbia and Bulgaria at 25–30% below EU prices.",
        "/",
        schemas,
    )
    body += "<body>"
    body += header_block()

    # Hero
    body += f"""
<section class="hero">
  <div class="container">
    <span class="eyebrow">Skopje · Southeastern Europe</span>
    <h1>Premium blood-filtration medicine <em>at a fraction of EU prices.</em></h1>
    <p class="hero-lede">
      Aevita Clinic delivers EBO2, MAH ozone, physician-led IV therapy
      and medically supervised GLP-1 weight loss — German equipment,
      licensed doctors, 25–30% below the Vienna and Zurich rates.
      Patients fly in from Switzerland, Austria, Germany and across
      the Balkans.
    </p>
    <div class="hero-actions">
      <a class="btn btn-gold" href="{url('/consultation/')}">Book a Consultation</a>
      <a class="btn btn-light" href="{url('/services/ebo2-blood-filtration/')}">Explore EBO2 →</a>
    </div>
  </div>
</section>
"""
    body += trust_strip()

    # Umbrella service intro
    body += f"""
<section>
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">The umbrella</span>
      <h2>One clinic. Four programs. Built for medical tourism done right.</h2>
      <p>
        Aevita is registered as a <strong>Private Health Institution
        (PZU)</strong> in North Macedonia — internal medicine,
        transfusion medicine and anaesthesiology. Every procedure on
        this site is performed by a licensed physician under sterile,
        regulated conditions. We are the only EBO2-equipped clinic in
        the country and one of the few in the Balkans.
      </p>
    </div>
    <div class="service-grid">
      {''.join(service_card(slug, s) for slug, s in CORE_SERVICES.items())}
    </div>
  </div>
</section>
"""

    # IV teaser section
    iv_cards_html = "".join(iv_card(slug, d) for slug, d in list(IV_DRIPS.items())[:4])
    body += f"""
<section style="background:var(--warm-white)">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">The IV lounge</span>
      <h2>Eight clinical drip protocols, every one physician-supervised.</h2>
      <p>From the classical Myers' Cocktail to high-dose NAD+ longevity protocols — all compounded fresh from EU-sourced pharmaceutical-grade ingredients in our infusion lounge.</p>
    </div>
    <div class="service-grid">
      {iv_cards_html}
    </div>
    <div style="margin-top:36px;text-align:center">
      <a class="btn btn-ghost" href="{url('/services/iv-therapy/')}">View all 8 IV protocols →</a>
    </div>
  </div>
</section>
"""

    # Locations / matrix preview
    body += f"""
<section>
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Who we serve</span>
      <h2>Skopje is the hub. Seven countries are the catchment.</h2>
      <p>
        Pristina is 90 minutes away. Sofia is three and a half hours.
        Belgrade and Tirana are four-hour drives or one-hour flights.
        Vienna, Zurich and Munich are direct hops. We are positioned
        to serve a region of 30 million people, with the cost
        structure to deliver EU-quality medicine at Balkan prices.
      </p>
    </div>
    <div class="country-grid">
      {''.join(country_card(slug, c) for slug, c in LOCATIONS.items())}
    </div>
  </div>
</section>
"""

    # Pricing comparison
    body += f"""
<section style="background:var(--warm-white)">
  <div class="container">
    <div class="two-col split-7-5">
      <div>
        <span class="eyebrow">Why Skopje</span>
        <h2>Same equipment. Same protocols. 30% less.</h2>
        <p>
          Our EBO2 device is manufactured in Germany, used by leading
          longevity clinics in Vienna, Zurich and Düsseldorf. Our
          ozone generator is the same model favoured by the German
          Medical Ozone Society. The medicine is identical to what you
          would receive in the EU — the cost structure is not.
        </p>
        <p>
          Skopje rent is a fifth of Zurich rent. Macedonian physician
          salaries are a quarter of German equivalents. The clinic
          passes that arithmetic on to patients without compromising
          any of the medicine.
        </p>
        <ul class="checklist">
          <li>German EBO2 device — same manufacturer as our EU peers</li>
          <li>Licensed internal medicine, anaesthesiology, transfusion physicians on site</li>
          <li>Sterile procedure room, dedicated recovery lounge, 24/7 emergency protocol</li>
          <li>International patient package: airport transfer, hotel, follow-up</li>
        </ul>
      </div>
      <div>
        <table class="price">
          <thead>
            <tr><th>Procedure</th><th class="num">EU average</th><th class="num">Aevita</th></tr>
          </thead>
          <tbody>
            <tr><td>EBO2 (single session)</td>
                <td class="num price-eu">EUR 1,200–1,500</td>
                <td class="num price-aevita">EUR 850–1,000</td></tr>
            <tr><td>MAH Ozone</td>
                <td class="num price-eu">EUR 180–250</td>
                <td class="num price-aevita">EUR 110–150</td></tr>
            <tr><td>NAD+ 500 mg IV</td>
                <td class="num price-eu">EUR 480–650</td>
                <td class="num price-aevita">EUR 280–400</td></tr>
            <tr><td>Myers' Cocktail</td>
                <td class="num price-eu">EUR 160–220</td>
                <td class="num price-aevita">EUR 95–130</td></tr>
            <tr><td>Wegovy program (monthly)</td>
                <td class="num price-eu">EUR 450–600</td>
                <td class="num price-aevita">EUR 280–380</td></tr>
          </tbody>
        </table>
        <p style="font-size:13px;color:var(--ink-soft);margin-top:14px">
          Prices indicative; physician confirms after intake.
          International packages include airport transfer and hotel
          partner rates.
        </p>
      </div>
    </div>
  </div>
</section>
"""

    body += final_cta()
    body += footer_block()
    write_page("index.html", body)


def page_services_hub():
    schemas = schema_breadcrumb([
        ("Home", "/"),
        ("Services", "/services/"),
    ])
    body = head(
        f"All Services — {BRAND_FULL}",
        "Every program we offer: EBO2 blood filtration, MAH ozone therapy, the IV lounge with eight clinical drip protocols, and physician-supervised GLP-1 medical weight loss (Wegovy, Ozempic, Mounjaro).",
        "/services/",
        schemas,
    )
    body += "<body>"
    body += header_block()
    body += crumbs([("Home", "/"), ("Services", None)])

    body += f"""
<section>
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Programs</span>
      <h1>Every program Aevita offers.</h1>
      <p>Four core programs and eight clinical IV drips — each delivered by licensed physicians in our registered Private Health Institution in Skopje.</p>
    </div>
    <div class="service-grid">
      {''.join(service_card(slug, s) for slug, s in CORE_SERVICES.items())}
    </div>
  </div>
</section>
"""

    iv_cards_html = "".join(iv_card(slug, d) for slug, d in IV_DRIPS.items())
    body += f"""
<section style="background:var(--warm-white)">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">IV Therapy Lounge</span>
      <h2>Eight clinical drip protocols.</h2>
      <p>Compounded fresh, physician-supervised, EU-sourced pharmaceutical-grade.</p>
    </div>
    <div class="service-grid">
      {iv_cards_html}
    </div>
  </div>
</section>
"""

    body += final_cta()
    body += footer_block()
    write_page("services/index.html", body)


def page_core_service(slug: str, s: dict):
    related_ivs = list(IV_DRIPS.items())[:4]
    schemas = (
        schema_procedure(s["name"], s["lede"][:200])
        + schema_breadcrumb([
            ("Home", "/"),
            ("Services", "/services/"),
            (s["name"], f"/services/{slug}/"),
        ])
        + schema_faq(s["faqs"])
    )
    body = head(
        f"{s['name']} in Skopje — {BRAND_FULL}",
        f"{s['lede'][:155]}".replace("&amp;", "&"),
        f"/services/{slug}/",
        schemas,
    )
    body += "<body>"
    body += header_block()
    body += crumbs([("Home", "/"), ("Services", "/services/"), (s["name"], None)])

    body += f"""
<section class="hero">
  <div class="container">
    <span class="eyebrow">{s['category']}</span>
    <h1>{s['name']}</h1>
    <p class="hero-lede">{s['lede']}</p>
    <div class="hero-actions">
      <a class="btn btn-gold" href="{url('/consultation/')}">Book {s['short']} Consultation</a>
      <a class="btn btn-light" href="tel:{PHONE_DIGITS}">{PHONE}</a>
    </div>
  </div>
</section>
"""
    body += trust_strip()

    # Quick facts
    body += f"""
<section class="tight">
  <div class="container">
    <div class="trust-grid">
      <div class="trust-item"><span class="label">Duration</span><span class="value">{s['duration']}</span></div>
      <div class="trust-item"><span class="label">EU price</span><span class="value">{s['price_eu']}</span></div>
      <div class="trust-item"><span class="label">Aevita price</span><span class="value">{s['price_aevita']}</span></div>
      <div class="trust-item"><span class="label">Downtime</span><span class="value">{s['downtime']}</span></div>
    </div>
  </div>
</section>
"""

    # Benefits + Best for two-col
    benefits_html = "".join(
        f'<div class="card"><h4>{name}</h4><p>{desc}</p></div>'
        for name, desc in s["benefits"]
    )
    bestfor_html = "".join(f'<li>{x}</li>' for x in s["best_for"])
    body += f"""
<section style="background:var(--warm-white)">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">What it does</span>
      <h2>Clinical benefits</h2>
    </div>
    <div class="cards">{benefits_html}</div>

    <div class="two-col" style="margin-top:60px">
      <div>
        <span class="eyebrow">Best candidates</span>
        <h2>Who this is built for</h2>
        <p>
          {s['name']} is a medical intervention, not a wellness add-on.
          Your physician will confirm candidacy at intake against your
          medical history and recent bloodwork. The following profiles
          are the most common at our clinic.
        </p>
      </div>
      <div>
        <ul class="checklist">{bestfor_html}</ul>
      </div>
    </div>
  </div>
</section>
"""

    # Process
    process_html = "".join(
        f'<div class="process-step"><h4>{name}</h4><p>{desc}</p></div>'
        for name, desc in s["process"]
    )
    body += f"""
<section>
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">How it works</span>
      <h2>The protocol, step by step</h2>
      <p>Course duration: <strong>{s['course']}</strong>. Every step is medically supervised and documented.</p>
    </div>
    <div class="process">{process_html}</div>
  </div>
</section>
"""

    # Pricing
    body += f"""
<section style="background:var(--warm-white)">
  <div class="container">
    <div class="two-col split-7-5">
      <div>
        <span class="eyebrow">Pricing</span>
        <h2>{s['name']}: EU-quality, Balkan accessibility</h2>
        <p>
          The arithmetic is straightforward — same German manufacturer,
          same EU pharmaceutical-grade consumables, same licensed
          physician model, lower Macedonian cost structure. Patients
          flying in from Western Europe typically save more than the
          cost of flights and a two-night stay combined.
        </p>
        <p><a class="more" href="{url('/pricing/')}" style="font-weight:600;text-transform:uppercase;letter-spacing:.08em;font-size:13px">See full pricing schedule →</a></p>
      </div>
      <div class="boxed">
        <h3 style="margin-top:0">{s['name']}</h3>
        <p style="margin-top:18px"><strong>Comparable EU pricing</strong><br>
        <span style="text-decoration:line-through;color:var(--ink-soft)">{s['price_eu']}</span></p>
        <p style="margin-top:8px"><strong>Aevita pricing</strong><br>
        <span style="color:var(--gold-dark);font-size:1.5rem;font-family:'Cormorant Garamond',serif;font-weight:600">{s['price_aevita']}</span></p>
        <p style="margin-top:18px;font-size:13px">Course: {s['course']}. International package available — includes airport transfer and partner-hotel rates.</p>
      </div>
    </div>
  </div>
</section>
"""

    # FAQ
    body += f"""
<section>
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Frequently asked</span>
      <h2>Questions patients ask before booking {s['short']}</h2>
    </div>
    {faq_block(s['faqs'])}
  </div>
</section>
"""

    # Related cross-links
    if slug == "iv-therapy":
        body += f"""
<section style="background:var(--warm-white)">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">All eight protocols</span>
      <h2>Every drip in the lounge</h2>
    </div>
    <div class="service-grid">
      {''.join(iv_card(s2, d) for s2, d in IV_DRIPS.items())}
    </div>
  </div>
</section>
"""
    else:
        body += f"""
<section style="background:var(--warm-white)">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Stack &amp; combine</span>
      <h2>Often combined with</h2>
      <p>Many patients pair {s['short']} with an IV protocol on the same day.</p>
    </div>
    <div class="service-grid">
      {''.join(iv_card(s2, d) for s2, d in related_ivs)}
    </div>
  </div>
</section>
"""

    body += final_cta(
        f"Speak to a doctor about {s['short']}",
        "Twenty-minute consultation with the physician who will run your protocol. We confirm candidacy, schedule and pricing.",
    )
    body += footer_block()
    write_page(f"services/{slug}/index.html", body)


def page_iv_drip(slug: str, d: dict):
    schemas = (
        schema_procedure(d["name"], d["lede"][:200])
        + schema_breadcrumb([
            ("Home", "/"),
            ("Services", "/services/"),
            ("IV Therapy", "/services/iv-therapy/"),
            (d["name"], f"/services/iv-therapy/{slug}/"),
        ])
    )
    body = head(
        f"{d['name']} — {BRAND_FULL} IV Lounge Skopje",
        f"{d['lede'][:155]}".replace("&amp;", "&"),
        f"/services/iv-therapy/{slug}/",
        schemas,
    )
    body += "<body>"
    body += header_block()
    body += crumbs([
        ("Home", "/"),
        ("Services", "/services/"),
        ("IV Therapy", "/services/iv-therapy/"),
        (d["name"], None),
    ])

    body += f"""
<section class="hero">
  <div class="container">
    <span class="eyebrow">IV Drip · {d['short']}</span>
    <h1>{d['name']}</h1>
    <p class="hero-lede">{d['lede']}</p>
    <div class="hero-actions">
      <a class="btn btn-gold" href="{url('/consultation/')}">Book this Drip</a>
      <a class="btn btn-light" href="{url('/services/iv-therapy/')}">All IV protocols →</a>
    </div>
  </div>
</section>
"""

    body += f"""
<section class="tight">
  <div class="container">
    <div class="trust-grid">
      <div class="trust-item"><span class="label">Duration</span><span class="value">{d['duration']}</span></div>
      <div class="trust-item"><span class="label">Dose options</span><span class="value">{d['dose']}</span></div>
      <div class="trust-item"><span class="label">Aevita price</span><span class="value">{d['price']}</span></div>
      <div class="trust-item"><span class="label">Recovery</span><span class="value">No downtime</span></div>
    </div>
  </div>
</section>
"""

    bestfor_html = "".join(f"<li>{x}</li>" for x in d["best_for"])
    body += f"""
<section style="background:var(--warm-white)">
  <div class="container">
    <div class="two-col">
      <div>
        <span class="eyebrow">Indications</span>
        <h2>Who this drip is built for</h2>
        <p>Every drip in the lounge is reviewed by your physician against your intake form and recent bloodwork. {d['name']} is most commonly booked for:</p>
      </div>
      <div>
        <ul class="checklist">{bestfor_html}</ul>
      </div>
    </div>
  </div>
</section>
"""

    # Stack with
    stack_items = "".join(
        iv_card(s2, IV_DRIPS[s2])
        for s2 in d["stack_with"]
        if s2 in IV_DRIPS
    )
    body += f"""
<section>
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Often stacked with</span>
      <h2>Common drip combinations</h2>
      <p>Many patients combine {d['short']} with one or two complementary drips on the same visit — your physician will sequence them safely.</p>
    </div>
    <div class="service-grid">{stack_items}</div>
  </div>
</section>
"""

    body += final_cta(
        f"Book {d['name']}",
        "Same-day appointments available most weekdays. Walk-in patients welcome with a brief physician intake.",
    )
    body += footer_block()
    write_page(f"services/iv-therapy/{slug}/index.html", body)


def page_locations_hub():
    schemas = schema_breadcrumb([
        ("Home", "/"),
        ("Locations", "/locations/"),
    ])
    body = head(
        f"Locations We Serve — {BRAND_FULL}",
        "Aevita Clinic Skopje serves patients from across Southeastern Europe — North Macedonia, Kosovo, Albania, Serbia, Bulgaria, Montenegro and Bosnia &amp; Herzegovina — plus Switzerland, Austria and Germany.",
        "/locations/",
        schemas,
    )
    body += "<body>"
    body += header_block()
    body += crumbs([("Home", "/"), ("Locations", None)])

    body += f"""
<section>
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Where our patients come from</span>
      <h1>Seven Balkan countries. Three Western European source markets. One clinic.</h1>
      <p>Aevita operates from a single physical clinic in Skopje and coordinates care for patients across Southeastern Europe. Pick your country and city below — every city page details travel logistics, accommodation partners and the protocols best suited to your trip.</p>
    </div>
    <div class="country-grid">
      {''.join(country_card(slug, c) for slug, c in LOCATIONS.items())}
    </div>
  </div>
</section>
"""

    # Source markets
    source_cards = "".join(
        f"""
<div class="country-card">
  <h3>{m['name']}</h3>
  <div class="local">{m['route']}</div>
  <p style="font-size:0.92rem">{m['lede'][:180]}…</p>
  <a class="more" href="{url('/from/' + slug + '/')}" style="font-weight:600;font-size:13px;letter-spacing:.08em;text-transform:uppercase">View travel guide →</a>
</div>
"""
        for slug, m in SOURCE_MARKETS.items()
    )
    body += f"""
<section style="background:var(--warm-white)">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">From Western Europe</span>
      <h2>Travel guides for our Swiss, Austrian and German patients</h2>
      <p>Direct flights to Skopje from every major DACH hub. Travel guides cover routing, schedule, airport transfer and recovery accommodation.</p>
    </div>
    <div class="country-grid">{source_cards}</div>
  </div>
</section>
"""

    body += final_cta()
    body += footer_block()
    write_page("locations/index.html", body)


def page_country(slug: str, c: dict):
    schemas = schema_breadcrumb([
        ("Home", "/"),
        ("Locations", "/locations/"),
        (c["name"], f"/locations/{slug}/"),
    ])
    description = f"{BRAND_FULL} serves patients across {c['name']} for EBO2, MAH ozone, IV therapy and medical weight loss. " + c["lede"][:80]
    body = head(
        f"{c['name']} — EBO2, IV Therapy &amp; Medical Wellness | {BRAND_FULL}",
        description,
        f"/locations/{slug}/",
        schemas,
    )
    body += "<body>"
    body += header_block()
    body += crumbs([
        ("Home", "/"),
        ("Locations", "/locations/"),
        (c["name"], None),
    ])

    home_flag = "Our home base — " if c.get("is_home") else ""
    body += f"""
<section class="hero">
  <div class="container">
    <span class="eyebrow">{c['name_local']}</span>
    <h1>{c['name']}</h1>
    <p class="hero-lede">{home_flag}{c['lede']}</p>
    <div class="hero-actions">
      <a class="btn btn-gold" href="{url('/consultation/')}">Book a Consultation</a>
      <a class="btn btn-light" href="tel:{PHONE_DIGITS}">{PHONE}</a>
    </div>
  </div>
</section>
"""
    body += trust_strip()

    # Cities in this country
    city_cards = "".join(
        f"""
<a class="matrix-cell" href="{url(f'/locations/{slug}/{cslug}/')}">
  <strong>{city['name']}{' — Clinic HQ' if city.get('is_hq') else ''}</strong>
  <p>{city['context'][:140]}…</p>
</a>
"""
        for cslug, city in c["cities"].items()
    )
    body += f"""
<section>
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Cities we serve in {c['name']}</span>
      <h2>Travel logistics for every major city</h2>
    </div>
    <div class="matrix">{city_cards}</div>
  </div>
</section>
"""

    # Services for this country
    service_cells = "".join(
        f"""
<a class="matrix-cell" href="{url(f'/services/{sslug}/')}">
  <strong>{s['name']}</strong>
  <p>{s['tagline']}</p>
  <p style="font-size:0.85rem"><span style="color:var(--gold-dark);font-weight:600">{s['price_aevita']}</span> · {s['duration']}</p>
</a>
"""
        for sslug, s in CORE_SERVICES.items()
    )
    body += f"""
<section style="background:var(--warm-white)">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Programs available</span>
      <h2>Every Aevita program is available for {c['name']} patients</h2>
      <p>The clinic is a short drive or one-hour flight from {c['name']}. International patient packages cover transfer and accommodation.</p>
    </div>
    <div class="matrix">{service_cells}</div>
  </div>
</section>
"""

    body += final_cta()
    body += footer_block()
    write_page(f"locations/{slug}/index.html", body)


def page_city(country_slug: str, city_slug: str, country: dict, city: dict):
    schemas = schema_breadcrumb([
        ("Home", "/"),
        ("Locations", "/locations/"),
        (country["name"], f"/locations/{country_slug}/"),
        (city["name"], f"/locations/{country_slug}/{city_slug}/"),
    ])
    title_suffix = "Aevita Clinic Skopje" if city.get("is_hq") else f"{BRAND_FULL}"
    body = head(
        f"{city['name']} — EBO2, IV Therapy &amp; Wegovy Weight Loss | {title_suffix}",
        f"{BRAND_FULL} for {city['name']} patients: EBO2 blood filtration, MAH ozone, NAD+ and IV therapy, and medical weight loss. {city['context'][:80]}",
        f"/locations/{country_slug}/{city_slug}/",
        schemas,
    )
    body += "<body>"
    body += header_block()
    body += crumbs([
        ("Home", "/"),
        ("Locations", "/locations/"),
        (country["name"], f"/locations/{country_slug}/"),
        (city["name"], None),
    ])

    hq_badge = '<span class="pill" style="background:var(--gold);color:var(--warm-white);border:0;margin-right:8px">Clinic HQ</span>' if city.get("is_hq") else ''
    body += f"""
<section class="hero">
  <div class="container">
    <span class="eyebrow">{country['name']} · {country['name_local']}</span>
    <h1>{hq_badge}{city['name']}</h1>
    <p class="hero-lede">{city['context']}</p>
    <div class="hero-actions">
      <a class="btn btn-gold" href="{url('/consultation/')}">Book from {city['name']}</a>
      <a class="btn btn-light" href="tel:{PHONE_DIGITS}">{PHONE}</a>
    </div>
  </div>
</section>
"""
    body += trust_strip()

    # Core service matrix for this city
    service_matrix = "".join(
        f"""
<a class="matrix-cell" href="{url(f'/locations/{country_slug}/{city_slug}/{sslug}/')}">
  <strong>{s['short']} · {s['name']}</strong>
  <p>{s['tagline']}</p>
  <p style="font-size:0.85rem"><span style="color:var(--gold-dark);font-weight:600">{s['price_aevita']}</span> · {s['duration']}</p>
</a>
"""
        for sslug, s in CORE_SERVICES.items()
    )
    body += f"""
<section>
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Programs for {city['name']} patients</span>
      <h2>Every Aevita program — from {city['name']}</h2>
      <p>Tap any program for the full clinical detail plus travel and recovery logistics specific to {city['name']}.</p>
    </div>
    <div class="matrix">{service_matrix}</div>
  </div>
</section>
"""

    # Logistics narrative
    if city.get("is_hq"):
        logistics = f"""
        <p>Aevita's clinic sits on Bulevar 8-mi Septemvri, twelve minutes from Skopje International Airport (SKP). Patients arriving from Switzerland, Germany or Austria are met at the airport by our medical concierge with private transfer included in the international package.</p>
        <p>Our partner hotel network covers central Skopje, the Aerodrom district and the Vodno foothills — every property is within fifteen minutes of the clinic and offers Aevita-rate recovery stays.</p>
        <p>For Skopje residents, the clinic operates morning and afternoon shifts. Most IV drip protocols can be booked same-day; EBO2 and MAH require a 24-hour booking lead time for physician scheduling and consumables prep.</p>
        """
    else:
        logistics = f"""
        <p>{city['context']}</p>
        <p>The clinic operates a complimentary medical concierge for patients traveling from {city['name']}: we coordinate transfer, partner-hotel recovery rates and post-procedure follow-up by telemedicine after you return home.</p>
        <p>For EBO2, MAH and NAD+ protocols we recommend a minimum 24-hour stay in Skopje for proper recovery before the return trip.</p>
        """
    body += f"""
<section style="background:var(--warm-white)">
  <div class="container">
    <div class="two-col">
      <div>
        <span class="eyebrow">Logistics</span>
        <h2>Travel &amp; recovery from {city['name']}</h2>
        {logistics}
      </div>
      <div class="boxed">
        <h3 style="margin-top:0">{city['name']} patient package</h3>
        <ul class="checklist">
          <li>Free medical concierge — booking, intake, paperwork</li>
          <li>Airport or border transfer (international package)</li>
          <li>Partner-hotel recovery rates within 15 min of clinic</li>
          <li>Same-day return triage for single-session EBO2</li>
          <li>Telemedicine follow-up at week 1 and week 4</li>
          <li>Medication shipping for GLP-1 weight-loss patients</li>
        </ul>
        <a class="btn btn-primary" href="{url('/consultation/')}" style="margin-top:20px;width:100%;justify-content:center">Start with a Consultation</a>
      </div>
    </div>
  </div>
</section>
"""

    # IV teaser
    iv_cards_html = "".join(iv_card(slug, d) for slug, d in list(IV_DRIPS.items())[:4])
    body += f"""
<section>
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">{city['name']} IV lounge bookings</span>
      <h2>Same-day IV drips for visiting patients</h2>
      <p>Most IV protocols can be booked same-day during your Skopje stay — pair with an EBO2 session or book a standalone visit.</p>
    </div>
    <div class="service-grid">{iv_cards_html}</div>
    <div style="margin-top:32px;text-align:center">
      <a class="btn btn-ghost" href="{url('/services/iv-therapy/')}">All eight IV drips →</a>
    </div>
  </div>
</section>
"""

    body += final_cta(
        f"Plan your trip from {city['name']}",
        "Twenty-minute consultation — we confirm candidacy, scope the right protocol and lock in your travel logistics.",
    )
    body += footer_block()
    write_page(f"locations/{country_slug}/{city_slug}/index.html", body)


def page_city_service(country_slug: str, city_slug: str, service_slug: str,
                       country: dict, city: dict, service: dict):
    schemas = (
        schema_procedure(service["name"], service["lede"][:200])
        + schema_breadcrumb([
            ("Home", "/"),
            ("Locations", "/locations/"),
            (country["name"], f"/locations/{country_slug}/"),
            (city["name"], f"/locations/{country_slug}/{city_slug}/"),
            (service["name"], f"/locations/{country_slug}/{city_slug}/{service_slug}/"),
        ])
    )
    body = head(
        f"{service['name']} for {city['name']} Patients — {BRAND_FULL}",
        f"{service['short']} for {city['name']} patients at {BRAND_FULL}. {service['tagline']}. Aevita price {service['price_aevita']} vs EU {service['price_eu']}.",
        f"/locations/{country_slug}/{city_slug}/{service_slug}/",
        schemas,
    )
    body += "<body>"
    body += header_block()
    body += crumbs([
        ("Home", "/"),
        ("Locations", "/locations/"),
        (country["name"], f"/locations/{country_slug}/"),
        (city["name"], f"/locations/{country_slug}/{city_slug}/"),
        (service["name"], None),
    ])

    body += f"""
<section class="hero">
  <div class="container">
    <span class="eyebrow">{city['name']} · {country['name']}</span>
    <h1>{service['name']} <em>from {city['name']}</em></h1>
    <p class="hero-lede">{service['lede']}</p>
    <div class="hero-actions">
      <a class="btn btn-gold" href="{url('/consultation/')}">Book {service['short']} from {city['name']}</a>
      <a class="btn btn-light" href="{url(f'/services/{service_slug}/')}">Full protocol detail →</a>
    </div>
  </div>
</section>
"""
    body += trust_strip()

    # Quick facts
    body += f"""
<section class="tight">
  <div class="container">
    <div class="trust-grid">
      <div class="trust-item"><span class="label">Duration</span><span class="value">{service['duration']}</span></div>
      <div class="trust-item"><span class="label">EU price</span><span class="value">{service['price_eu']}</span></div>
      <div class="trust-item"><span class="label">Aevita price</span><span class="value">{service['price_aevita']}</span></div>
      <div class="trust-item"><span class="label">Downtime</span><span class="value">{service['downtime']}</span></div>
    </div>
  </div>
</section>
"""

    # Why travel from this city
    if city.get("is_hq"):
        travel_para = (f"Skopje patients have the simplest path of all — our clinic on "
                       f"Bulevar 8-mi Septemvri is your home clinic. Book {service['short']} morning or "
                       f"afternoon shift, walk in, recover in our lounge, walk home.")
    else:
        travel_para = (f"{city['context']} For {service['short']} specifically, we recommend "
                       f"factoring in {service['downtime']} of post-procedure observation before the "
                       f"return trip — covered in your patient package.")

    body += f"""
<section style="background:var(--warm-white)">
  <div class="container">
    <div class="two-col">
      <div>
        <span class="eyebrow">From {city['name']}</span>
        <h2>Why {city['name']} patients travel to Aevita</h2>
        <p>{travel_para}</p>
        <p>The arithmetic alone justifies the trip: comparable EU pricing for {service['name']} runs <strong>{service['price_eu']}</strong>. Aevita pricing is <strong style="color:var(--gold-dark)">{service['price_aevita']}</strong>. The difference covers transport, accommodation and follow-up for most {city['name']} patients with room to spare.</p>
      </div>
      <div class="boxed">
        <h3 style="margin-top:0">{service['short']} from {city['name']} — what to expect</h3>
        <ul class="checklist">
          <li>Pre-visit intake by video — physician confirms candidacy</li>
          <li>Day-of arrival, intake bloodwork if not already submitted</li>
          <li>{service['name']} session — {service['duration']}</li>
          <li>Recovery in our lounge with monitored observation</li>
          <li>Post-procedure debrief and home-care plan</li>
          <li>Telemedicine follow-up at week 1 and week 4</li>
        </ul>
        <a class="btn btn-primary" href="{url('/consultation/')}" style="margin-top:20px;width:100%;justify-content:center">Start with a Consultation</a>
      </div>
    </div>
  </div>
</section>
"""

    # Related programs
    related = [(s, CORE_SERVICES[s]) for s in CORE_SERVICES if s != service_slug][:3]
    related_cards = "".join(
        f"""
<a class="matrix-cell" href="{url(f'/locations/{country_slug}/{city_slug}/{s2_slug}/')}">
  <strong>{s2['name']}</strong>
  <p>{s2['tagline']}</p>
  <p style="font-size:0.85rem"><span style="color:var(--gold-dark);font-weight:600">{s2['price_aevita']}</span></p>
</a>
"""
        for s2_slug, s2 in related
    )
    body += f"""
<section>
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Other programs from {city['name']}</span>
      <h2>{city['name']} patients also book</h2>
    </div>
    <div class="matrix">{related_cards}</div>
  </div>
</section>
"""

    body += final_cta(
        f"{service['short']} consultation — {city['name']} patients",
        "Twenty-minute video consultation with the physician who will run your protocol. We confirm candidacy, schedule and travel logistics.",
    )
    body += footer_block()
    write_page(f"locations/{country_slug}/{city_slug}/{service_slug}/index.html", body)


def page_source_market(slug: str, m: dict):
    schemas = schema_breadcrumb([
        ("Home", "/"),
        ("Locations", "/locations/"),
        (f"From {m['name']}", f"/from/{slug}/"),
    ])
    body = head(
        f"From {m['name']} to Skopje — EBO2 &amp; IV Therapy at Balkan Prices | {BRAND_FULL}",
        f"How {m['name']} patients travel to Aevita Clinic Skopje for EBO2, MAH and IV therapy. " + m['lede'][:80],
        f"/from/{slug}/",
        schemas,
    )
    body += "<body>"
    body += header_block()
    body += crumbs([
        ("Home", "/"),
        ("Locations", "/locations/"),
        (f"From {m['name']}", None),
    ])

    body += f"""
<section class="hero">
  <div class="container">
    <span class="eyebrow">For patients from {m['name']}</span>
    <h1>From {m['name']} to Skopje — the medical-tourism math</h1>
    <p class="hero-lede">{m['lede']}</p>
    <div class="hero-actions">
      <a class="btn btn-gold" href="{url('/consultation/')}">Book a Consultation</a>
      <a class="btn btn-light" href="tel:{PHONE_DIGITS}">{PHONE}</a>
    </div>
  </div>
</section>
"""
    body += trust_strip()

    body += f"""
<section>
  <div class="container">
    <div class="two-col">
      <div>
        <span class="eyebrow">Routing</span>
        <h2>Getting to Skopje from {m['name']}</h2>
        <p><strong>{m['route']}</strong></p>
        <p>Skopje International Airport (SKP) is 12 minutes from the clinic. Our medical concierge meets every international patient at arrivals with the consent forms ready, transfer arranged and accommodation confirmed.</p>
        <p>Most patients schedule a two-night Skopje stay — Day 1: intake and bloodwork; Day 2: procedure and recovery; Day 3: return travel. Single-session EBO2 patients can compress to 36 hours total if needed.</p>
      </div>
      <div class="boxed">
        <h3 style="margin-top:0">International patient package</h3>
        <ul class="checklist">
          <li>Medical concierge from arrival to departure</li>
          <li>Private airport transfer (SKP-clinic-hotel)</li>
          <li>Two-night partner-hotel recovery stay at Aevita rates</li>
          <li>Pre-visit intake by video so you arrive ready</li>
          <li>English- and German-speaking physician</li>
          <li>Telemedicine follow-up at week 1 and week 4</li>
        </ul>
      </div>
    </div>
  </div>
</section>
"""

    # Service grid for this source market
    service_cells = "".join(
        f"""
<a class="matrix-cell" href="{url(f'/services/{sslug}/')}">
  <strong>{s['name']}</strong>
  <p>{s['tagline']}</p>
  <p style="font-size:0.85rem">
    EU: <span style="text-decoration:line-through">{s['price_eu']}</span> ·
    Aevita: <span style="color:var(--gold-dark);font-weight:600">{s['price_aevita']}</span>
  </p>
</a>
"""
        for sslug, s in CORE_SERVICES.items()
    )
    body += f"""
<section style="background:var(--warm-white)">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">The price arithmetic</span>
      <h2>{m['name']} pricing vs Aevita pricing</h2>
      <p>The price differential alone covers flights, two-night recovery stay and ground transfer for most patients — with room to spare.</p>
    </div>
    <div class="matrix">{service_cells}</div>
  </div>
</section>
"""

    body += final_cta(
        f"Plan your trip from {m['name']}",
        "Twenty-minute video consultation in English or German. We confirm candidacy and lock in your travel package.",
    )
    body += footer_block()
    write_page(f"from/{slug}/index.html", body)


def page_about():
    schemas = schema_breadcrumb([
        ("Home", "/"),
        ("About", "/about/"),
    ])
    body = head(
        f"About — Founders, Equipment &amp; Medical Team | {BRAND_FULL}",
        "About Aevita Clinic Skopje: founders Nina &amp; Pape, our German medical equipment, licensed physician team and the regulatory framework that makes Aevita the only EBO2-equipped clinic in North Macedonia.",
        "/about/",
        schemas,
    )
    body += "<body>"
    body += header_block()
    body += crumbs([("Home", "/"), ("About", None)])

    body += f"""
<section class="hero">
  <div class="container">
    <span class="eyebrow">The clinic</span>
    <h1>Built for the Balkans, by people who know both sides of the border.</h1>
    <p class="hero-lede">{FOUNDERS_NOTE}</p>
  </div>
</section>
"""

    body += f"""
<section>
  <div class="container">
    <div class="two-col">
      <div>
        <span class="eyebrow">Founders</span>
        <h2>Nina &amp; Pape</h2>
        <p>Aevita was founded by a husband-and-wife team who spent two decades watching the same pattern repeat: Balkan patients flying to Vienna or Zurich for procedures their home region was not equipped to deliver, at prices their home region could not justify.</p>
        <p>The plan was simple. Bring the German equipment in. License the German protocols in. Hire the best Macedonian physicians. Pass the cost arithmetic on to the patient. Add the medical-tourism logistics layer that EU clinics, frankly, do not bother with.</p>
        <p>The clinic opened as a registered Private Health Institution (ПЗУ) under Macedonian law, with internal medicine, anaesthesiology and transfusion medicine on the licence. Every procedure is documented, every consumable traceable, every protocol on the wall.</p>
      </div>
      <div class="boxed">
        <span class="eyebrow">Regulatory framework</span>
        <h3>ПЗУ — Private Health Institution</h3>
        <p>Aevita operates under Macedonian Ministry of Health regulation as a registered Private Health Institution (Приватна здравствена установа). Our licence covers:</p>
        <ul class="checklist">
          <li>Internal medicine outpatient practice</li>
          <li>Transfusion medicine — blood handling and processing</li>
          <li>Anaesthesiology — supervised sedation where required</li>
          <li>Sterile procedure environment, documented protocols</li>
          <li>Medical-waste contract with licensed disposal partner</li>
          <li>Compliant with EU pharmaceutical-grade consumables</li>
        </ul>
      </div>
    </div>
  </div>
</section>
"""

    body += f"""
<section style="background:var(--warm-white)">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Equipment</span>
      <h2>German-manufactured medical devices</h2>
      <p>Every piece of clinical equipment on site comes from the manufacturer trusted by the leading German, Swiss and Austrian clinics.</p>
    </div>
    <div class="cards">
      <div class="card">
        <h4>EBO2 device</h4>
        <p>German-manufactured closed-loop extracorporeal blood oxygenation &amp; ozonation system. The same device favoured by Vienna, Zurich and Düsseldorf longevity clinics.</p>
      </div>
      <div class="card">
        <h4>Medical ozone generator</h4>
        <p>German-manufactured precision ozone generator for MAH protocols. Calibrated to the German Medical Ozone Society dosing standards.</p>
      </div>
      <div class="card">
        <h4>Patient monitoring</h4>
        <p>Continuous BP, SpO₂, ECG and temperature monitoring during every EBO2 and MAH session under anaesthesiology supervision.</p>
      </div>
      <div class="card">
        <h4>Sterilisation &amp; consumables</h4>
        <p>Autoclave sterilisation cycle for reusable equipment; single-use consumables sourced from EU pharmaceutical-grade suppliers only.</p>
      </div>
    </div>
  </div>
</section>
"""

    body += f"""
<section>
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Team</span>
      <h2>Licensed medical staff on every shift</h2>
    </div>
    <div class="cards">
      <div class="card">
        <h4>Internal medicine physician</h4>
        <p>Patient intake, candidacy review, IV therapy supervision, GLP-1 weight-loss program oversight and post-procedure care.</p>
      </div>
      <div class="card">
        <h4>Anaesthesiologist</h4>
        <p>On site for every EBO2 and MAH session — vitals monitoring, sedation management where required, emergency protocol leadership.</p>
      </div>
      <div class="card">
        <h4>Transfusion physician</h4>
        <p>Blood-handling protocols, EBO2 circuit oversight, transfusion-medicine standards compliance.</p>
      </div>
      <div class="card">
        <h4>Two clinical nurses</h4>
        <p>IV access, drip preparation, sterilisation cycles, patient comfort and recovery-lounge supervision.</p>
      </div>
    </div>
  </div>
</section>
"""

    body += final_cta()
    body += footer_block()
    write_page("about/index.html", body)


def page_pricing():
    schemas = schema_breadcrumb([
        ("Home", "/"),
        ("Pricing", "/pricing/"),
    ])
    body = head(
        f"Pricing — EBO2, MAH, IV Therapy &amp; Wegovy | {BRAND_FULL}",
        "Full price list for every Aevita program: EBO2 blood filtration, MAH ozone, eight IV drip protocols and the GLP-1 medical weight-loss program. Compared against EU averages.",
        "/pricing/",
        schemas,
    )
    body += "<body>"
    body += header_block()
    body += crumbs([("Home", "/"), ("Pricing", None)])

    body += f"""
<section class="hero">
  <div class="container">
    <span class="eyebrow">Transparent pricing</span>
    <h1>Every program. Every price. Compared.</h1>
    <p class="hero-lede">Aevita publishes every list price on this page. Final pricing is confirmed at intake after physician review of bloodwork and protocol — but the ranges below are accurate to within ten percent.</p>
  </div>
</section>
"""

    # Core services table
    core_rows = "".join(
        f"<tr><td><a href='{url(f'/services/{slug}/')}'>{s['name']}</a></td>"
        f"<td>{s['duration']}</td>"
        f"<td class='num price-eu'>{s['price_eu']}</td>"
        f"<td class='num price-aevita'>{s['price_aevita']}</td></tr>"
        for slug, s in CORE_SERVICES.items()
    )
    body += f"""
<section>
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Core programs</span>
      <h2>EBO2, MAH ozone, IV hub &amp; weight loss</h2>
    </div>
    <div class="table-wrap">
      <table class="price">
        <thead>
          <tr><th>Program</th><th>Duration</th><th class="num">EU average</th><th class="num">Aevita</th></tr>
        </thead>
        <tbody>{core_rows}</tbody>
      </table>
    </div>
  </div>
</section>
"""

    # IV table
    iv_rows = "".join(
        f"<tr><td><a href='{url(f'/services/iv-therapy/{slug}/')}'>{d['name']}</a></td>"
        f"<td>{d['duration']}</td>"
        f"<td>{d['dose']}</td>"
        f"<td class='num price-aevita'>{d['price']}</td></tr>"
        for slug, d in IV_DRIPS.items()
    )
    body += f"""
<section style="background:var(--warm-white)">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">IV lounge</span>
      <h2>Drip protocols</h2>
    </div>
    <div class="table-wrap">
      <table class="price">
        <thead>
          <tr><th>Drip</th><th>Duration</th><th>Dose options</th><th class="num">Price</th></tr>
        </thead>
        <tbody>{iv_rows}</tbody>
      </table>
    </div>
  </div>
</section>
"""

    body += f"""
<section>
  <div class="container">
    <div class="section-head center">
      <span class="eyebrow">Packages</span>
      <h2>Course pricing and international packages</h2>
    </div>
    <div class="cards">
      <div class="card">
        <h4>EBO2 Course of 4</h4>
        <p>Four EBO2 sessions across 2–4 weeks. <strong>EUR 3,200</strong> (saving EUR 400 vs single-session pricing).</p>
      </div>
      <div class="card">
        <h4>MAH Course of 10</h4>
        <p>Ten MAH sessions across 4–6 weeks. <strong>EUR 1,100</strong> (saving EUR 400 vs single sessions).</p>
      </div>
      <div class="card">
        <h4>IV Drip Membership</h4>
        <p>Four drips per month, any protocols. <strong>EUR 320 / month</strong> (saving 20% vs single drips).</p>
      </div>
      <div class="card">
        <h4>Wegovy 12-week starter</h4>
        <p>Full program with bloodwork, titration and 4-week reviews. <strong>EUR 1,180 total</strong> (medication included).</p>
      </div>
      <div class="card">
        <h4>International package — DACH</h4>
        <p>Adds airport transfer, two-night partner-hotel stay, English/German physician. <strong>+ EUR 450</strong> on any program.</p>
      </div>
      <div class="card">
        <h4>International package — Balkans</h4>
        <p>Adds border transfer, one-night partner-hotel stay, regional-language support. <strong>+ EUR 290</strong> on any program.</p>
      </div>
    </div>
  </div>
</section>
"""

    body += final_cta()
    body += footer_block()
    write_page("pricing/index.html", body)


def page_consultation():
    schemas = schema_breadcrumb([
        ("Home", "/"),
        ("Book Consultation", "/consultation/"),
    ])
    body = head(
        f"Book a Consultation — {BRAND_FULL}",
        "Book a 20-minute consultation with an Aevita Clinic physician — review your goals, bloodwork and candidacy for EBO2, MAH, IV therapy or the GLP-1 weight-loss program.",
        "/consultation/",
        schemas,
    )
    body += "<body>"
    body += header_block()
    body += crumbs([("Home", "/"), ("Book Consultation", None)])

    body += f"""
<section class="hero">
  <div class="container">
    <span class="eyebrow">Step one</span>
    <h1>Book a 20-minute consultation.</h1>
    <p class="hero-lede">Video call with the physician who will run your protocol. We review your goals, current bloodwork and medical history, confirm candidacy and scope the right program. No obligation.</p>
  </div>
</section>
"""

    body += f"""
<section>
  <div class="container">
    <div class="two-col split-7-5">
      <div>
        <span class="eyebrow">Patient intake</span>
        <h2>Request a consultation</h2>
        <form style="background:var(--warm-white);border:1px solid var(--line);border-radius:var(--radius-lg);padding:32px;display:flex;flex-direction:column;gap:18px" onsubmit="event.preventDefault();alert('Thank you. Our medical concierge will contact you within one business day.')">
          <div>
            <label style="display:block;font-size:13px;font-weight:600;color:var(--teal-900);margin-bottom:6px">Full name *</label>
            <input type="text" required style="width:100%;padding:12px;border:1px solid var(--line);border-radius:var(--radius);font-family:inherit;font-size:15px;background:var(--cream)">
          </div>
          <div>
            <label style="display:block;font-size:13px;font-weight:600;color:var(--teal-900);margin-bottom:6px">Email *</label>
            <input type="email" required style="width:100%;padding:12px;border:1px solid var(--line);border-radius:var(--radius);font-family:inherit;font-size:15px;background:var(--cream)">
          </div>
          <div>
            <label style="display:block;font-size:13px;font-weight:600;color:var(--teal-900);margin-bottom:6px">Phone (WhatsApp preferred)</label>
            <input type="tel" style="width:100%;padding:12px;border:1px solid var(--line);border-radius:var(--radius);font-family:inherit;font-size:15px;background:var(--cream)">
          </div>
          <div>
            <label style="display:block;font-size:13px;font-weight:600;color:var(--teal-900);margin-bottom:6px">Country &amp; city</label>
            <input type="text" placeholder="e.g. Belgrade, Serbia" style="width:100%;padding:12px;border:1px solid var(--line);border-radius:var(--radius);font-family:inherit;font-size:15px;background:var(--cream)">
          </div>
          <div>
            <label style="display:block;font-size:13px;font-weight:600;color:var(--teal-900);margin-bottom:6px">Program of interest</label>
            <select style="width:100%;padding:12px;border:1px solid var(--line);border-radius:var(--radius);font-family:inherit;font-size:15px;background:var(--cream)">
              <option>EBO2 Blood Filtration</option>
              <option>MAH Ozone Therapy</option>
              <option>IV Therapy (drip lounge)</option>
              <option>NAD+ Anti-Aging IV</option>
              <option>Medical Weight Loss (Wegovy / Ozempic)</option>
              <option>Not sure — I'd like a physician's recommendation</option>
            </select>
          </div>
          <div>
            <label style="display:block;font-size:13px;font-weight:600;color:var(--teal-900);margin-bottom:6px">Anything else you'd like the doctor to know?</label>
            <textarea rows="4" style="width:100%;padding:12px;border:1px solid var(--line);border-radius:var(--radius);font-family:inherit;font-size:15px;background:var(--cream);resize:vertical"></textarea>
          </div>
          <button type="submit" class="btn btn-gold" style="margin-top:8px;justify-content:center">Request Consultation</button>
          <p style="font-size:12px;color:var(--ink-soft);margin:0">By submitting you consent to be contacted by our medical concierge regarding your enquiry. We do not share your data with third parties.</p>
        </form>
      </div>
      <div>
        <div class="boxed dark">
          <span class="eyebrow">Speed</span>
          <h3 style="margin-top:8px">Within one business day</h3>
          <p>Our medical concierge replies to every consultation request within one business day — usually within four hours during Skopje business hours.</p>
        </div>
        <div class="boxed" style="margin-top:20px">
          <h3 style="margin-top:0">Prefer to talk now?</h3>
          <p style="margin-bottom:14px">Call our concierge directly or message us on WhatsApp.</p>
          <p><a class="btn btn-primary" href="tel:{PHONE_DIGITS}" style="width:100%;justify-content:center">{PHONE}</a></p>
          <p style="margin-top:10px"><a class="btn btn-ghost" href="https://wa.me/{WHATSAPP}" style="width:100%;justify-content:center">WhatsApp</a></p>
          <p style="margin-top:14px;font-size:13px">Languages: English, German, Serbian, Albanian, Macedonian, Bulgarian.</p>
        </div>
      </div>
    </div>
  </div>
</section>
"""

    body += footer_block()
    write_page("consultation/index.html", body)


def page_contact():
    schemas = schema_breadcrumb([
        ("Home", "/"),
        ("Contact", "/contact/"),
    ])
    body = head(
        f"Contact — {BRAND_FULL}",
        f"Reach Aevita Clinic Skopje — call {PHONE}, email {EMAIL}, or visit us at {ADDRESS_STREET}, {ADDRESS_CITY}, {ADDRESS_COUNTRY}.",
        "/contact/",
        schemas,
    )
    body += "<body>"
    body += header_block()
    body += crumbs([("Home", "/"), ("Contact", None)])

    body += f"""
<section class="hero">
  <div class="container">
    <span class="eyebrow">Reach us</span>
    <h1>Contact Aevita Clinic Skopje.</h1>
    <p class="hero-lede">Phone, email, WhatsApp or walk-in — our medical concierge replies within one business day.</p>
  </div>
</section>
"""

    body += f"""
<section>
  <div class="container">
    <div class="two-col">
      <div>
        <span class="eyebrow">Clinic</span>
        <h2>Skopje location</h2>
        <p><strong>{ADDRESS_STREET}</strong><br>{ADDRESS_CITY}<br>{ADDRESS_COUNTRY}</p>
        <p style="margin-top:24px"><strong>Phone:</strong> <a href="tel:{PHONE_DIGITS}">{PHONE}</a><br>
        <strong>Email:</strong> <a href="mailto:{EMAIL}">{EMAIL}</a><br>
        <strong>WhatsApp:</strong> <a href="https://wa.me/{WHATSAPP}">{PHONE}</a></p>
        <p style="margin-top:24px"><strong>Hours:</strong><br>
        Monday–Friday: 08:00–20:00<br>
        Saturday: 09:00–14:00<br>
        Sunday: by appointment only</p>
        <p style="margin-top:24px"><strong>Languages spoken:</strong> English, German, Serbian, Albanian, Macedonian, Bulgarian.</p>
      </div>
      <div>
        <div class="boxed dark">
          <h3 style="margin-top:0">Booking a consultation?</h3>
          <p>The fastest route is the consultation form — our physician team reviews every request and replies the same business day.</p>
          <a class="btn btn-gold" href="{url('/consultation/')}" style="margin-top:14px;width:100%;justify-content:center">Book a Consultation</a>
        </div>
        <div class="boxed" style="margin-top:20px">
          <h3 style="margin-top:0">Press &amp; partnerships</h3>
          <p>Hotel partners, corporate wellness programs, medical-tourism agencies — we work with established partners across the region. Reach out at <a href="mailto:partners@aevitaclinic.mk">partners@aevitaclinic.mk</a>.</p>
        </div>
      </div>
    </div>
  </div>
</section>
"""

    body += footer_block()
    write_page("contact/index.html", body)


def page_404():
    body = head(
        f"Page not found — {BRAND_FULL}",
        "The page you were looking for could not be found.",
        "/404.html",
        "",
    )
    body += "<body>"
    body += header_block()
    body += f"""
<section class="hero">
  <div class="container">
    <span class="eyebrow">404</span>
    <h1>That page is not on our books.</h1>
    <p class="hero-lede">The page you were looking for may have moved, or never existed. Try one of these instead.</p>
    <div class="hero-actions">
      <a class="btn btn-gold" href="{url('/')}">Home</a>
      <a class="btn btn-light" href="{url('/services/')}">All Services</a>
      <a class="btn btn-light" href="{url('/locations/')}">All Locations</a>
    </div>
  </div>
</section>
"""
    body += footer_block()
    write_page("404.html", body)


def page_assets():
    # CSS
    (OUT / "assets").mkdir(exist_ok=True)
    (OUT / "assets" / "style.css").write_text(CSS, encoding="utf-8")

    # Favicon SVG
    favicon = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">'
        '<rect width="64" height="64" rx="12" fill="#0a3f3d"/>'
        '<text x="32" y="44" text-anchor="middle" '
        'font-family="Georgia,serif" font-size="36" font-weight="600" '
        'fill="#e7d4b3">A</text></svg>'
    )
    (OUT / "assets" / "favicon.svg").write_text(favicon, encoding="utf-8")

    # OG image placeholder (SVG, browsers will render)
    og = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 630">'
        '<defs><linearGradient id="g" x1="0" x2="1" y1="0" y2="1">'
        '<stop offset="0" stop-color="#0a3f3d"/>'
        '<stop offset="1" stop-color="#155957"/></linearGradient></defs>'
        '<rect width="1200" height="630" fill="url(#g)"/>'
        '<text x="60" y="200" font-family="Georgia,serif" font-size="80" '
        'fill="#e7d4b3" font-weight="600">Aevita Clinic</text>'
        '<text x="60" y="280" font-family="Georgia,serif" font-size="44" '
        'fill="#faf7f1" font-style="italic">Premium blood filtration &amp; IV wellness</text>'
        '<text x="60" y="360" font-family="Inter,sans-serif" font-size="28" '
        'fill="#d8e8e6">Skopje · Southeastern Europe</text>'
        '<text x="60" y="560" font-family="Inter,sans-serif" font-size="22" '
        'fill="#b8935f" font-weight="600" letter-spacing="3">EBO2 · MAH · IV · GLP-1</text>'
        '</svg>'
    )
    (OUT / "assets" / "og.jpg.svg").write_text(og, encoding="utf-8")
    # write also as og.jpg for OG path (browsers won't render svg as jpg, but we'll
    # keep it as a placeholder file). Better to just point OG to .svg.

    # robots
    (OUT / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml\n",
        encoding="utf-8",
    )


def page_sitemap():
    urls = ["/"]
    urls += ["/services/", "/locations/", "/about/", "/pricing/",
             "/consultation/", "/contact/"]
    for slug in CORE_SERVICES:
        urls.append(f"/services/{slug}/")
    for slug in IV_DRIPS:
        urls.append(f"/services/iv-therapy/{slug}/")
    for cslug, c in LOCATIONS.items():
        urls.append(f"/locations/{cslug}/")
        for citySlug in c["cities"]:
            urls.append(f"/locations/{cslug}/{citySlug}/")
            for serviceSlug in CORE_SERVICES:
                urls.append(f"/locations/{cslug}/{citySlug}/{serviceSlug}/")
    for slug in SOURCE_MARKETS:
        urls.append(f"/from/{slug}/")

    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for path in urls:
        lines.append(
            f"  <url><loc>{DOMAIN}{path}</loc><changefreq>weekly</changefreq>"
            f"<priority>{'1.0' if path == '/' else '0.7'}</priority></url>"
        )
    lines.append('</urlset>')
    (OUT / "sitemap.xml").write_text("\n".join(lines), encoding="utf-8")


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------

def main():
    print("Building Aevita Clinic site...")
    page_assets()
    page_home()
    page_services_hub()
    for slug, s in CORE_SERVICES.items():
        page_core_service(slug, s)
    for slug, d in IV_DRIPS.items():
        page_iv_drip(slug, d)
    page_locations_hub()
    for cslug, c in LOCATIONS.items():
        page_country(cslug, c)
        for city_slug, city in c["cities"].items():
            page_city(cslug, city_slug, c, city)
            for service_slug, service in CORE_SERVICES.items():
                page_city_service(cslug, city_slug, service_slug, c, city, service)
    for slug, m in SOURCE_MARKETS.items():
        page_source_market(slug, m)
    page_about()
    page_pricing()
    page_consultation()
    page_contact()
    page_404()
    page_sitemap()

    # Count pages
    pages = list(OUT.rglob("*.html"))
    print(f"Built {len(pages)} HTML pages.")


if __name__ == "__main__":
    main()
