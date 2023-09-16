import pandas as pd
import numpy as np
from mortgage.calculator import FixMonthlyPayment as _F
from income.afford import Income2Mortgage as _I
from utils.fotmat import float2str

class FixMontlyPaymentTable:
    def __init__(self,
                 num_payments=360,
                 interest_rate_boundary=(0.04, 0.075),
                 interest_rate_step=0.125/100,
                 principal_boundary=(1e6, 1500000),
                 principal_step=50000,
                 property_rate=0.013,
                 monthly_hoa=250,
                 monthly_insurance=150,
                 monthly_others=0.0,
                 lend_ratio=0.43,
                 income_total_boundary=(230000 + 90000, 250000 + 90000),
                 income_step=2000,
                 fix_monthly_property_tax=2000,

                 ):
        self._num_payments = num_payments
        self._interest_rate_boundary = interest_rate_boundary
        self._interest_rate_step = interest_rate_step
        self._principal_boundary = principal_boundary
        self._principal_step = principal_step
        self._property_rate = property_rate
        self._monthly_hoa = monthly_hoa
        self._monthly_insurance = monthly_insurance
        self._monthly_others = monthly_others
        self._lend_ratio = lend_ratio
        self._income_total_boundary = income_total_boundary
        self._income_step = income_step
        self._fix_monthly_property_tax = fix_monthly_property_tax


    def gen_table(self):
        data = {}
        indices = []
        _bool_calc_indices = True
        for interest_rate in np.arange(self._interest_rate_boundary[0], self._interest_rate_boundary[1],
                                       self._interest_rate_step):
            col_name = f"{float2str(interest_rate * 100, 3)}%"
            cols = []
            for principal in np.arange(self._principal_boundary[0], self._principal_boundary[1], self._principal_step):
                payment = _F.calculate_monthly_payment(
                    initial_principal=principal,
                    interest_rate=interest_rate,
                    num_of_payments=self._num_payments)
                property_tax = principal * self._property_rate / 12
                payment += (property_tax +
                            self._monthly_hoa +
                            self._monthly_insurance +
                            self._monthly_others)
                cols.append(float2str(payment, 0))
                if _bool_calc_indices:
                    index = float2str(principal, 0)
                    indices.append(index)
            data[col_name] = cols
            _bool_calc_indices = False
        return pd.DataFrame(data, index=indices)

    def gen_income_affordable_table(self):
        data = {}
        indices = []
        _bool_calc_indices = True
        for interest_rate in np.arange(self._interest_rate_boundary[0], self._interest_rate_boundary[1],
                                       self._interest_rate_step):
            col_name = f"{float2str(interest_rate * 100, 3)}%"
            cols = []
            for income in np.arange(self._income_total_boundary[0], self._income_total_boundary[1], self._income_step):
                adjustment = (self._fix_monthly_property_tax +
                            self._monthly_hoa +
                            self._monthly_insurance +
                            self._monthly_others)
                monthly_pay_total = _I.calculate_max_monthly_affordable(income, self._lend_ratio)
                principal = _F.calculate_principal(monthly_payment=monthly_pay_total,
                                                   interest_rate=interest_rate,
                                                   num_of_payments=self._num_payments,
                                                   fee=adjustment)

                cols.append(float2str(principal, 2))
                if _bool_calc_indices:
                    index = float2str(income, 0)
                    indices.append(index)
            data[col_name] = cols
            _bool_calc_indices = False
        return pd.DataFrame(data, index=indices)










