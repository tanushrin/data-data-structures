# pylint: disable=missing-docstring
RATES = {"USDEUR":0.85, "GBPEUR":1.13, "CHFEUR":0.86, "EURGBP": 0.885}

def convert(amount, currency):
    """returns the converted amount in the given currency
    amount is a tuple like (100, "EUR")
    currency is a string
    """
    return round(amount[0] * RATES.get(amount[1]+currency)) if amount[1]+currency in RATES else None
