# Importing necessary libraries
from classes.widgets.chatbot.model import Model
import pandas as pd

# Fitness class
class Fitness(Model):
    """
    Fitness class to train a machine learing model using two Dataframe columns.

    :param model: Sci-kit model to be trained.
    """
    def __init__(self, model):
        super().__init__(model)

    def model_fit(self, x: pd.DataFrame, y: pd.Series):
        """
        Trains the model using input features `x` and target variable `y`.

        :param x: Features (DataFrame or ndarray).
        :param y: Target values (Series or ndarray).
        :return: Trained model.
        """
        self.model.fit(x, y)
        return self.model