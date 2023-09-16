from mortgage.calculator import FixMonthlyPayment

def test_calculate_monthly_payment():
    # assert 5995 < FixMonthlyPayment.calculate_monthly_payment(
    #     initial_principal=1e6, interest_rate=0.06, num_of_payments=360
    # ) < 5996
    res = FixMonthlyPayment.get_overall_payment_details(
        initial_principal=1e6, interest_rate=0.06, num_of_payments=360
    )
    print(res[36])

    # print(FixMonthlyPayment.get_overall_payment_details(
    #     initial_principal=1e6, interest_rate=0.06, num_of_payments=360
    # ))


if __name__ == "__main__":
    test_calculate_monthly_payment()