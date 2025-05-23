# Importing necessary libraries
import plotly.express as px 
from model import usersAmount

# Amount of users in last 30 days
usersAmountFig = px.bar(usersAmount, x='Quantidade de usuários', y='Data', title='Quantidade de usuários nos últimos 30 dias', barmode='group', color_discrete_sequence=['red'])