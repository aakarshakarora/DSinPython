class CurrencyConverter:
    def convert(self, amount):
        raise NotImplementedError("Subclasses must implement abstract method")


class USDConverter(CurrencyConverter):
    def convert(self, amount):
        return amount / 74.65  # Sample conversion rate


class EURConverter(CurrencyConverter):
    def convert(self, amount):
        return amount / 88.74  # Sample conversion rate


class GBPConverter(CurrencyConverter):
    def convert(self, amount):
        return amount / 103.41  # Sample conversion rate


class CurrencyConverterFactory:
    @staticmethod
    def get_converter(currency):
        if currency == "USD":
            return USDConverter()
        elif currency == "EUR":
            return EURConverter()
        elif currency == "GBP":
            return GBPConverter()
        else:
            raise ValueError("Unsupported currency")


if __name__ == "__main__":
    amount = 1000  # Amount in INR

    # Convert to USD
    usd_converter = CurrencyConverterFactory.get_converter("USD")
    print(f"{amount} INR is approximately {usd_converter.convert(amount):.2f} USD")

    # Convert to EUR
    eur_converter = CurrencyConverterFactory.get_converter("EUR")
    print(f"{amount} INR is approximately {eur_converter.convert(amount):.2f} EUR")

    # Convert to GBP
    gbp_converter = CurrencyConverterFactory.get_converter("GBP")
    print(f"{amount} INR is approximately {gbp_converter.convert(amount):.2f} GBP")
