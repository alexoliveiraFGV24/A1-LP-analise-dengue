import pandas as pd
import numpy as np
import os
import sys
import concurrent.futures
sys.path.append(os.getcwd())
from src.utils.statistic import contigency_coefficient
from src.config import OUTPUT_FOLDER


def hypothesis3(df: pd.DataFrame) -> None:
    ...
