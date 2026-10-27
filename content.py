"""Sorting guide content (English + Tamil) and UI strings."""

CATEGORIES = {
    "wet": {
        "color": "#2e7d32",
        "name": {"en": "Wet waste", "ta": "ஈரக் கழிவு"},
        "yes": {"en": ["Food scraps", "Fruit and vegetable peels", "Tea leaves", "Flowers and leaves"],
                "ta": ["உணவு மிச்சம்", "பழம், காய்கறித் தோல்", "தேயிலைக் கழிவு", "பூ, இலைகள்"]},
        "no": {"en": ["Plastic", "Paper", "Glass", "Batteries"],
               "ta": ["பிளாஸ்டிக்", "காகிதம்", "கண்ணாடி", "பேட்டரி"]},
    },
    "dry": {
        "color": "#1565c0",
        "name": {"en": "Dry waste", "ta": "உலர் கழிவு"},
        "yes": {"en": ["Used tissues and napkins", "Dirty wrappers", "Cloth scraps", "Thermocol"],
                "ta": ["பயன்படுத்திய டிஷ்யூ", "அழுக்கு உறைகள்", "துணித் துண்டுகள்", "தெர்மோகோல்"]},
        "no": {"en": ["Food scraps", "E-waste", "Clean recyclables"],
               "ta": ["உணவு மிச்சம்", "மின்னணுக் கழிவு", "சுத்தமான மறுசுழற்சிப் பொருள்"]},
    },
    "recyclable": {
        "color": "#f9a825",
        "name": {"en": "Recyclable", "ta": "மறுசுழற்சிக் கழிவு"},
        "yes": {"en": ["Clean paper and cardboard", "Plastic bottles (empty)", "Metal cans", "Glass bottles"],
                "ta": ["சுத்தமான காகிதம், அட்டை", "காலி பிளாஸ்டிக் பாட்டில்", "உலோக டப்பா", "கண்ணாடி பாட்டில்"]},
        "no": {"en": ["Food-soiled items", "Tissues", "Batteries"],
               "ta": ["உணவு படிந்த பொருள்", "டிஷ்யூ", "பேட்டரி"]},
    },
    "ewaste": {
        "color": "#c62828",
        "name": {"en": "E-waste", "ta": "மின்னணுக் கழிவு"},
        "yes": {"en": ["Batteries", "Chargers and cables", "Earphones", "Old phones, pen drives"],
                "ta": ["பேட்டரி", "சார்ஜர், கேபிள்", "ஹெட்போன்", "பழைய போன், பென் டிரைவ்"]},
        "no": {"en": ["Food scraps", "Paper", "Plastic bottles"],
               "ta": ["உணவு மிச்சம்", "காகிதம்", "பிளாஸ்டிக் பாட்டில்"]},
    },
}

STATUSES = {
    "overflowing": {"en": "Bin is full or overflowing", "ta": "குப்பைத்தொட்டி நிரம்பிவிட்டது"},
    "wrong_waste": {"en": "Wrong waste inside", "ta": "தவறான கழிவு உள்ளது"},
    "damaged_label": {"en": "Label or QR is damaged", "ta": "லேபிள் / QR சேதமடைந்துள்ளது"},
    "ok": {"en": "Bin is fine", "ta": "தொட்டி சரியாக உள்ளது"},
}

UI = {
    "yes": {"en": "Put in this bin", "ta": "இதில் போடவும்"},
    "no": {"en": "Do not put here", "ta": "இதில் போடாதீர்கள்"},
    "report": {"en": "Report this bin", "ta": "இந்தத் தொட்டியைப் பற்றி தெரிவிக்க"},
    "note": {"en": "Note (optional)", "ta": "குறிப்பு (விருப்பம்)"},
    "send": {"en": "Send report", "ta": "அனுப்பு"},
    "thanks": {"en": "Thank you. Your report was sent.", "ta": "நன்றி. உங்கள் தகவல் அனுப்பப்பட்டது."},
    "location": {"en": "Location", "ta": "இடம்"},
}
