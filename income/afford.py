import numpy as np
from utils.fotmat import float2str
class Income2Mortgage:
    def __init__(self,
                 upper_ratio=0.43,
                 income_total_boundary=(230000+90000, 250000+90000),
                 income_step=2000):
        self._upper_ratio = upper_ratio
        self._income_total_boundary = income_total_boundary
        self._income_step = income_step

    @classmethod
    def calculate_max_annual_affordable(cls, annual_income, ratio=0.43):
        return annual_income * ratio

    @classmethod
    def calculate_max_monthly_affordable(cls, annual_income, ratio=0.43):
        return cls.calculate_max_annual_affordable(annual_income, ratio) / 12

    def gen_data(self):
        data = []
        for income in np.arange(
                self._income_total_boundary[0],
                self._income_total_boundary[1],
                self._income_step):
            lend = income * 0.43 / 12
            key = f"{float2str(income/1000, 1)}k"
            data.append({key: lend})
        return data


