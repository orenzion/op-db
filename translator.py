PENSION_HEB_TO_ENG = {
    "אג\"ח קונצרני": "Corporate Bond",
    "אופציות": "Option",
    "ארץ": "Country",
    "אתר": "Web",
    "גוף מוסדי": "Institutional body",
    "דירוג": "Rating",
    "הלוואות": "Loans",
    "הצמדה": "Protected",
    "השקעה בחברות מוחזקות": "Investee Companies",
    "השקעות אחרות": "Other Investments",
    "זכויות מקרקעין": "Real Estate",
    "חברות": "Commercial Country",
    "חוזים עתידיים": "Future",
    "יעודיות": "Designated Bond",
    "כתבי אופציה": "Warrant",
    "כתובת הנכס": "Real Estate address",
    "מוצרים מובנים": "Structured",
    "מזומנים": "Cash",
    "מח\"מ": "Duration",
    "ממשלה": "Government Bond",
    "מניות": "Stock",
    "מספר מנפיק": "Issuer Nunber",
    "מספר ני\"ע": "Instrument Number",
    "מספר קרן": "Fund Number",
    "נדלן": "Real Estate Type",
    "נכס בסיס": "Underlying",
    "סוג הלוואה": "Loan Type",
    "סוג מוצר": "Structured Type",
    "סוג מטבע": "Currency",
    "סוג נגזר": "Derivative Type",
    "סוג קרן": "Investmnet Fund Type",
    "סחירות": "Tradable",
    "ענף פעילות": "Industry",
    "ערך נקוב": "Nominal Value",
    "פקדונות מעל 3 חודשים": "Deposits",
    "קונסורציום כן/לא": "Consortium",
    "קרנות השקעה": "Private Equity",
    "שווי הוגן": "Fair Value",
    "שווי שוק": "Market Value",
    "שייך למדד": "Index",
    "שיעור ריבית": "Rate",
    "שם המדרג": "Rating Agencies",
    "שם המנפיק/שם נייר ערך": "Instrument Name",
    "שם מנפיק": "Issuer Mane",
    "שם קרן": "Fund Nane",
    "שעור מנכסי אפיק ההשקעה": "Rate of Instrument Type",
    "שעור מסך נכסי השקעה": "Rafe of Funde Holding",
    "שעור מערך נקוב מונפק": "Rafe of Register",
    "שער": "Price",
    "תעודות השתתפות בקרנות נאמנות": "Mutual Fund",
    "תעודות התחייבות ממשלתיות": "Government Bond",
    "תעודות חוב מסחריות": "Commercial Debt",
    "תעודות סל": "ETF",
    "תשואה לפידיון": "yield",

    "תאריך הדיווח": "Date",
    "החברה המדווחת": "Institutional body",
    "שם מסלול/קרן/קופה": "Fund Name",
    "מספר מסלול/קרן/קופה": "Fund Number",
    "1.ד. הלוואות": "Loans",
    "1.ה. פקדונות מעל 3 חודשים": "Deposits",
    "1. ו. זכויות במקרקעין": "1. Real Estate",
    "1. ז. השקעה בחברות מוחזקות": "Portfolio Companies",
    "1. ט. יתרות התחייבות להשקעה": "Investment commitments",
    'שם נ"ע': "Instrument Name",
    "שם מדרג": "Rating Agencies",
    "שיעור מנכסי אפיק ה השקעה": "Rate of Instrument Type",
    "שעור מנכסי השקעה": "Rafe of Funde Holding",
    "עלות מתואמת מסגרות אשראי ללווים": "Fair Value",
    "שיעור מנכסי אפיק ההשקעה": "Rate of Instrument Type",
    "עלות מותאמת": "Fair Value",
    "ריבית אפקטיבית": "Effective Interests",
    "תאריך רכישה": "Purchase date",
    "ענף מסחר": "Industry",
    'עלות מתואמת אג"ח קונצרני ל.סחיר': "Fair Value",
    "מנכסי אפיק ההשקעה": "Rate of Instrument Type",
    'עלות מתואמת אג"ח קונצרני סחיר': "Fair Value",
    'תאריך סיום ההתחייבות': "Date of Investment commitments",
    'מנפיק': "Issuer Mane",
    'תאריך שערוך אחרון': "Date of valuation",
    'אופי הנכס': "Real Estate Type",
    'שיעור התשואה במהלך התקופה': "yield over period",
    'שווי משוערך': "Fair Value",
    'ספק מידע': "Information provider",
    'זירת מסחר': "Market name",
}


def translate_from_hebrew(word):
    if word in PENSION_HEB_TO_ENG:
        return PENSION_HEB_TO_ENG[word]

    # Todo: Pulling translation from the back office.