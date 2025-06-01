# Importing necessary libraries
import pandas as pd

# Data logic 
## Dataframe data
data = {
    "DEBITO": [],
    "CREDITO": [],
    "DATA": [],
    "VALOR": [],
    "HISTORICO": [],
    "MATRIZ": [],
    "FILIAL": []
}

## Creating dataframe
df = pd.DataFrame(data)
    
# Users' amount
usersAmountData = {
    'Quantidade de usuários': [13],
    'Data': ['22/05/2025']
}
usersAmount = pd.DataFrame(usersAmountData)

