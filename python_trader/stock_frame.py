import pandas as pd
import numpy as np

from typing import List
from typing import Dict
from typing import Union

from datetime import datetime
from datetime import time
from datetime import timezone

from pandas.core.groupby import DataFrameGroupBy
from pandas.core.window import RollingGroupby

class StockFrame(): 
    def __init__(self, data: List[Dict]):

        self._data = data
        self._frame: pd.DataFrame = self.create_data_frame()
        self._symbol_groups: DataFrameGroupBy = None
        self._symbol_rolling_groups = None


    @property
    def frame(self) -> pd.DataFrame:
        """_summary_

        Returns:
            pd.DataFrame: returns a pandas datafra,e
        """        
        return self._frame
    
    @property
    def group_by_symbols(self) -> DataFrameGroupBy:
        self.self._symbol_groups =  self._frame.groupby(
            by='symbol',
            as_index=False,
            sort=True
        )

        return self._symbol_groups
    
    def symbol_rolling_groups(self, size: int) -> RollingGroupby:
        """Grabs the windows for each group.

        Arguments:
        ----
        size {int} -- The size of the window.

        Returns:
        ----
        {RollingGroupby} -- A `pandas.core.window.RollingGroupby` object.
        """

        # If we don't a symbols group, then create it.
        if not self._symbol_groups:
            self.symbol_groups

        self._symbol_rolling_groups: RollingGroupby = self._symbol_groups.rolling(
            size
        )

        return self._symbol_rolling_groups
    
    def create_data_frame(self) -> pd.DataFrame: 
         
         if isinstance(self._data, dict):
            self._data = [self._data]
         
         price_df = pd.DataFrame(data=self._data)
         price_df = self._parse_datetime_column(price_df=price_df)
         price_df = self.set_multi_index(price_df=price_df)

         return price_df
    
    def _parse_datetime_column(self, price_df: pd.DataFrame) -> pd.DataFrame:

        price_df['datetime'] = pd.to_datetime(
            price_df['datetime'], 
            unit = 'ms',
            origin = 'unix'
        )

        return price_df
    
    def set_multi_index(self, price_df: pd.DataFrame) -> pd.DataFrame:
         price_df = price_df.set_index(keys=['symbol', 'datetime'])
         return price_df
    
    def add_row(self, data: Dict): 

        column_names = ['open', 'close', 'high', 'low', 'volume']

        for quote in data: 
            time_stamp = pd.to_datetime(
                quote['datetime'],
                unit='ms',
                origin='unix'
            )

            row_id = (quote['symbol'], time_stamp)

            row_values = [ quote['open'], quote['close'], quote['high'], quote['low'], quote['volume']]
                
            new_row = pd.Series(data=row_values)

            self.frame.loc[row_id, column_names] = new_row.values

            self.frame.sort_index(inplace=True)

