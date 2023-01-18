# [(200, 289), (117, 242), (19, 74), (282, 287), (176, 276), (37, 275), (27, 286), (239, 242), (39, 111), (60, 277), (68, 113), (38, 172), (52, 277), (68, 166), (137, 251), (148, 292), (21, 137), (111, 258), (69, 182), (152, 178), (79, 100)]

import json
import quantlib.indicators_cal as indicators_cal
import pandas as pd

class Lbmom:

    def __init__(self, instruments_config, historical_df, simulation_start, vol_target):
        self.pairs = [(200, 289), (117, 242), (19, 74), (282, 287), (176, 276), (37, 275), (27, 286), (239, 242), (39, 111), (60, 277), (68, 113), (38, 172), (52, 277), (68, 166), (137, 251), (148, 292), (21, 137), (111, 258), (69, 182), (152, 178), (79, 100)]
        self.instruments_config = instruments_config
        self.historical_df = historical_df
        self.simulation_start = simulation_start
        self.vol_target = vol_target
        with open(instruments_config) as f:
            self.instruments_config = json.load(f)
        self.sysname = "LBMOM"

        """
        1. Function to get data and indicators specific to strategy.
        2. Function to run backtest and get positions.
        """

    def extend_historicals(self, instruments, historical_data):
        # We want the moving averages, which is a proxy for momentum factor.
        # We also want a univariate statistical factor as an indicator of regime. We use the ADX as a proxy for momentum regime indicator.
        for inst in instruments:
            historical_data["{} adx".format(inst)] = indicators_cal.adx_series(
                high=historical_data["{} high".format(inst)],
                low=historical_data["{} low".format(inst)],
                close=historical_data["{} close".format(inst)],
                n=14
            )
            for pair in self.pairs:
                historical_data["{} ema{}".format(inst, str(pair))] = indicators_cal.ema_series(historical_data["{} close".format(inst)], n=pair[0]) - \
                    indicators_cal.ema_series(historical_data["{} close".format(inst)], n=pair[1])
        return historical_data

    def run_simulation(self, historical_data):
        """
        Init Params
        """

        instruments = self.instruments_config["instruments"]

        """
        Pre-processing
        """

        historical_data = self.extend_historicals(instruments=instruments, historical_data=historical_data)
        print(historical_data)
        portfolio_df = pd.DataFrame(index=historical_data[self.simulation_start:].index).reset_index()
        portfolio_df.loc[0, "capital"] = 10000
        print(portfolio_df)

    def get_subsys_pos(self):
        self.run_simulation(historical_data=self.historical_df)
