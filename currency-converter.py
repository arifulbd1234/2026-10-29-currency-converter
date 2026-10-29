"""
Day 23 - 2026-10-29
Tool: Currency Converter (to and from Taka)
What it does: Converts amounts between Bangladeshi taka (BDT) and a
few common currencies using a small rate table, and shows how to
update the rates in one place when they change.
Who it helps: Freelancers paid from abroad, online shoppers, and
families receiving remittance who want a quick taka estimate.
Note: Rates below are EXAMPLES for learning - check a live rate
before real money decisions.
"""

# Example rates: how many taka 1 unit of the currency buys
RATES_TO_BDT = {
    "USD": 120.00,
    "EUR": 130.00,
    "GBP": 152.00,
    "INR": 1.42,
    "SAR": 32.00,
}


def to_bdt(amount, currency):
    rate = RATES_TO_BDT[currency.upper()]
    return round(amount * rate, 2)


def from_bdt(amount_bdt, currency):
    rate = RATES_TO_BDT[currency.upper()]
    return round(amount_bdt / rate, 2)


def convert(amount, from_currency, to_currency):
    """Convert between any two listed currencies, via taka."""
    if from_currency.upper() == "BDT":
        return from_bdt(amount, to_currency)
    in_bdt = to_bdt(amount, from_currency)
    if to_currency.upper() == "BDT":
        return in_bdt
    return from_bdt(in_bdt, to_currency)


if __name__ == "__main__":
    print("100 USD =", to_bdt(100, "USD"), "taka")
    print("50000 taka =", from_bdt(50000, "USD"), "USD")
    print("250 EUR =", convert(250, "EUR", "USD"), "USD")
