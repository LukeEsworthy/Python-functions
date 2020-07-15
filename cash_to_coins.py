dollarAmount = 8.69

piggyBank = {
    "pennies": 0,
    "nickels": 0,
    "dimes": 0,
    "quarters": 0
}


def getCoins(amountToCoins):
    pennyValue = 0.01
    nickelValue = 0.05
    dimeValue = 0.10
    quarterValue = 0.25
    piggyBank['quarters'] = int(amountToCoins / quarterValue)
    piggyBank['dimes'] = int((amountToCoins % quarterValue) / dimeValue)
    piggyBank['nickels'] = int(
        (amountToCoins % quarterValue) % dimeValue / nickelValue)
    piggyBank['pennies'] = int(
        (amountToCoins % quarterValue) % dimeValue % nickelValue / pennyValue)


getCoins(dollarAmount)
print(piggyBank)
