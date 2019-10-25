def afterOneYear(balance,annInterestRate,minMonthRate):
    monthInterestRate = annInterestRate / 12.0
    totalPaid = 0.0
    for month in range(1, 13):
        minMonthPaid = round(balance * minMonthRate, 2)
        principlePaid = round(minMonthPaid - monthInterestRate * balance, 2)
        balance = round(balance - principlePaid, 2)
        totalPaid = round(totalPaid + minMonthPaid, 2)
    return totalPaid, balance


def inOneYear(balanceInput, annInterestRate):
    # 请在下面编写代码
    minMonthPaid = 1
    month = 0
    balance = balanceInput
    minMonthRate = annInterestRate / 12
    while True:
        for i in range(12):
            balance = balance*(1+minMonthRate) - minMonthPaid
        if balance < 0:
            break
        balance = balanceInput
        minMonthPaid += 1
    # 请不要修改下面的代码

    return minMonthPaid, month, balance


def inOneYearBiSearch(balanceInput, annInterestRate):
    down = balanceInput / 12
    minMonthPaid = 1
    month = 0
    balance = balanceInput
    minMonthRate = annInterestRate / 12


    return minMonthPaid, month, balance

# def perMonth(balance, )

print(inOneYear(1200, 0.18))