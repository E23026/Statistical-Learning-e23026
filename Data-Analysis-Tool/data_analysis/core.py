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

class PlottingMethods:
    def plot_histogram(self, x, data):
        fig = px.histogram(data, x=x)
        fig.show()

    def plot_bar_chart(self, x, y, data):
        fig = px.bar(data, x=x, y=y)
        fig.show()

    def plot_pie_chart(self, names, values, data):
        fig = px.pie(
            data,
            names=names,
            values=values
        )
        fig.show()
