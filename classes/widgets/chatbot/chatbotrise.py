# Import necessary modules
from classes.widgets.chatbot.fitness import Fitness
import pandas as pd

# Chatbot rise
class ChatBotRise(Fitness):
    def __init__(self, model):
        super().__init__(model)

    def predict(self, x: pd.DataFrame):
        """
        Use the trained model to predict output for input features X.

        :param x: Input features for prediction.
        :return: Predicted values.
       """
        predictions = self.model.predict(x)
        return predictions