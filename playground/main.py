from mortgage.table import FixMontlyPaymentTable
from income.afford import Income2Mortgage
from mortgage.calculator import FixMonthlyPayment

def get_income():
    data = Income2Mortgage(
        upper_ratio=0.43,
        income_total_boundary=(300000, 350000),
        income_step=1000
    ).gen_data()
    return data

def get_mortgage():
    table = FixMontlyPaymentTable(
        num_payments=360,
        interest_rate_boundary=(0.030, 0.075),
        interest_rate_step=0.125 / 100,
        principal_boundary=(1400000, 1800000),
        principal_step=25000,
        property_rate=0.013,
        monthly_hoa=250,
        monthly_insurance=150,
        monthly_others=0.0,
    )
    return table.gen_table(), table.gen_income_affordable_table()

def get_detail():
    f = FixMonthlyPayment.get_overall_payment_details(initial_principal=1500000, interest_rate=0.06, num_of_payments=360)
    return f

if __name__ == "__main__":
    income = get_income()
    lend_info, income_table = get_mortgage()
    detail = get_detail()
    # for each in income:
    #     print(each)
    # print(lend)
    # print(detail)
    for each in detail:
        print(each)