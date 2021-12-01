from enum import Enum


class Prediction(Enum):
    bullish = "Price Will Increase"
    bearish = "Price Will Decrease"
    none = "No Prediction"
