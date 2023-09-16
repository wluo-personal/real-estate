class FixMonthlyPayment:

    @classmethod
    def _get_accural_principal_ratio(cls, interest_rate, num_of_payments):
        """

        :param interest_rate: The interest rate between payments
        :param num_of_payments:
        :return:
        """
        return (1+interest_rate) ** num_of_payments
    @classmethod
    def _get_accural_payment_ratio(cls, interest_rate, num_of_payments):
        """

        :param interest_rate: The interest rate between payments
        :param num_of_payments:
        :return:
        """
        return ((1+interest_rate) ** num_of_payments - 1) / interest_rate

    @classmethod
    def get_remain_principal(cls, initial_principal=1.0, interest_rate=0.05, monthly_payment=0.001, num_of_payments=1):
        """
        The method will return the remaining principal after num_of_payments.
        Fomula:
        p(1+r)^j - x[  (1+r)^j / r  ]
        Proof:
            Given that p is principal, r is monthly interest rate, x is the fixed monthly payment
            Pi(1+r) - x = Pi+1
            Principal
                after 1st payment:  p(1+r) -x
                after 2nd payment: p(1+r)^2 - (1+r)x - x
                after 3rd payment: p(1+r)^3 - x[(1+r)^2 + (1+r)^1 + (1+r)^0]
                after jth payment: p(1+r)^j - x[(1+r)^(j-1) + ... + (1+r)^0 ]
                                    = p(1+r)^j - x[  (1 - (1+r)^j) / (1 - (1+r))  ]
                                    = p(1+r)^j - x[  ((1+r)^j - 1) / r  ]

        :param initial_principal: Start Principal
        :param interest_rate: float, annual interest rate
        :param monthly_payment: float, monthly fixed payment
        :param num_of_payments: int, number of payment
        :return: float. The remaining principal
        """
        monthly_ir = interest_rate / 12
        ratio_principal = cls._get_accural_principal_ratio(interest_rate=monthly_ir, num_of_payments=num_of_payments)
        ratio_payment = cls._get_accural_payment_ratio(interest_rate=monthly_ir, num_of_payments=num_of_payments)
        return initial_principal * ratio_principal - monthly_payment * ratio_payment

    @classmethod
    def calculate_monthly_payment(cls, initial_principal=1.0, interest_rate=0.05, num_of_payments=1):
        monthly_ir = interest_rate / 12
        ratio_principal = cls._get_accural_principal_ratio(
            interest_rate=monthly_ir, num_of_payments=num_of_payments)
        ratio_payment = cls._get_accural_payment_ratio(
            interest_rate=monthly_ir, num_of_payments=num_of_payments)
        return initial_principal * ratio_principal / ratio_payment

    @classmethod
    def calculate_principal(cls, monthly_payment, interest_rate=0.05, num_of_payments=360, fee=0.0):
        """
        Given the monthly_payment return the principal that can be borrowed from the bank
        :param monthly_payment: the total amount

        :param interest_rate: annual rate
        :param num_of_payments:
        :param fee: (monthly_payment - fee) is the amount paid to the bank
        :return:
        """
        bank_payment = monthly_payment - fee
        monthly_ir = interest_rate / 12
        ratio_principal = cls._get_accural_principal_ratio(
            interest_rate=monthly_ir, num_of_payments=num_of_payments)
        ratio_payment = cls._get_accural_payment_ratio(
            interest_rate=monthly_ir, num_of_payments=num_of_payments)
        return bank_payment * ratio_payment / ratio_principal

    @classmethod
    def get_overall_payment_details(cls, initial_principal=1.0, interest_rate=0.05, num_of_payments=1):
        monthly_payment = cls.calculate_monthly_payment(
            initial_principal=initial_principal, interest_rate=interest_rate, num_of_payments=num_of_payments)
        payment_plan = []
        monthly_ir = interest_rate / 12
        remain_principal = initial_principal
        paid_total_principal = 0.0
        paid_total_interest = 0.0

        for nth in range(num_of_payments):
            paid_interest = remain_principal * monthly_ir
            paid_principal = monthly_payment - paid_interest
            paid_total_principal += paid_principal
            paid_total_interest += paid_interest
            remain_principal -= paid_principal

            payment_plan.append(
                {"paid_principal": paid_principal,
                 "paid_interest": paid_interest,
                 "paid_total_principal": paid_total_principal,
                 "paid_total_interest": paid_total_interest,
                 "remaining_total_principal": remain_principal,
                 "nth_payment": nth + 1
                 })
        return payment_plan
