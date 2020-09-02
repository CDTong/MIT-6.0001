# O(logn)
def main():
    annual_salary = float(input('Enter your starting salary: '))
    semi_annual_raise = 0.07
    r = 0.04
    total_cost = 0.25*1000000
    current_savings = 0

    low = 0
    high = 10000
    steps = 0

    rate = 0
    months = 0

    while abs(current_savings-total_cost) > 100 and rate < 9999:
        if current_savings > total_cost:
            high = rate
        else:
            low = rate

        rate = (low+high)/2
        steps += 1
        current_savings = 0

        for months in range(1, 37):
            current_savings = current_savings * (1 + 0.04 / 12) + rate / 10000 * annual_salary / 12 * 1.07 ** (abs(months / 6))

    if rate < 9999:
        rate = int(rate)
        print("Best savings rate", rate/10000)
        print("Steps in bisection search: ", steps)
    else:
        print("It is not possible to pay the down payment in three years.")


main()
