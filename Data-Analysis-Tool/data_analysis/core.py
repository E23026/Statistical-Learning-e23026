import pandas as pd
import numpy as np

from google.colab import files
import io

import plotly.express as px
import plotly.graph_objects as go

from plotly.subplots import make_subplots

from sklearn.preprocessing import (
    MinMaxScaler,
    StandardScaler,
    RobustScaler,
    OrdinalEncoder
)

from scipy.stats import chi2_contingency
