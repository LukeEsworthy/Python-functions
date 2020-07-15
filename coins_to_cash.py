def calc_dollars(**coins):
    for key, value in coins.items():
        pennyValue = 0.01
        nickelValue = 0.05
        dimeValue = 0.10
        quarterValue = 0.25
        dollarAmount = (coins['pennies'] * pennyValue) + (coins['nickels'] * nickelValue) + (
            coins['dimes'] * dimeValue) + (coins['quarters'] * quarterValue)
    print("$", dollarAmount)


calc_dollars(pennies=342, nickels=9, dimes=32, quarters=4)
