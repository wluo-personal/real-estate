class Calculator:
    @classmethod
    def get_loan_monthly_payment(cls,
                                 loan_amount,
                                 interest_rate,
                                 n_payment=12*30,
                                 fix_amount=0.0):
        """
        0	principal
        1 	principal * (1 + r) - (monthly_payment - montly_fix)
        2  	principal * (1 + r)^2 - (monthly_payment - montly_fix) * (1+r) - (monthly_payment - montly_fix)
        n 	principal * (1 + r)^n - (monthly_payment - montly_fix) * (1+r)^(n-1) - ... - (monthly_payment - montly_fix) * (1+r)^0
        -->

        principal * (1 + r)^n 	= (monthly_payment - montly_fix) * (1+r)^(n-1) + ... + (monthly_payment - montly_fix) * (1+r)^0
        principal * (1 + r)^n	=   (monthly_payment - montly_fix) * （1 - （1+r)^n）    / (1 - (1+r))
        principal * (1 + r)^n * r / ((1+r)^n - 1) + monthly_fix	= monthly_payment
        :return:
        """
        r = interest_rate / 12
        n = n_payment
        return loan_amount * ((1 + r) ** n) * r / ((1+r)**n - 1) + fix_amount
    @classmethod
    def get_monthly_payment(cls,
                            total_price=1500000,
                            down_pay_ratio=0.2,
                            interest_rate=0.05,
                            n_payment=12*30,
                            tax_rate=0.03):
        loan_amount = total_price * (1 - down_pay_ratio)
        fix_amount = total_price * tax_rate / 12
        return cls.get_loan_monthly_payment(
            loan_amount=loan_amount,
            interest_rate=interest_rate,
            n_payment=n_payment,
            fix_amount=fix_amount)


if __name__ == "__main__":
    from utils.solver import bsearch_solver
    Taxes_tax = 0.035
    California_tax = 0.014
    down_ratio = 0.2
    interest_rate = 0.0
    n_payment = 12 * 30

    California_house_price = 2000000
    Taxes_house_price = 1500000

    California_monthly_payment = Calculator.get_monthly_payment(
        total_price=California_house_price,
        down_pay_ratio=down_ratio,
        interest_rate=interest_rate,
        n_payment=n_payment,
        tax_rate=California_tax)

    fn = lambda x: Calculator.get_monthly_payment(
        total_price=x,
        down_pay_ratio=down_ratio,
        interest_rate=interest_rate,
        n_payment=n_payment,
        tax_rate=Taxes_tax)

    Taxes_house_price = bsearch_solver(fn, x_min=0, x_max=1e10, target=California_monthly_payment)

    # Taxes_monthly_payment = Calculator.get_monthly_payment(
    #     total_price=Taxes_house_price,
    #     down_pay_ratio=down_ratio,
    #     interest_rate=interest_rate,
    #     n_payment=n_payment,
    #     tax_rate=Taxes_tax)



    print(f"interest rate: {interest_rate}")
    print(f"California House Price: {California_house_price}, monthly payment: {California_monthly_payment}")
    print(f"Taxes House Price: {Taxes_house_price}, monthly payment: {California_monthly_payment}")

