import pandas as pd
Fruit_sales = pd.DataFrame([[35, 21], [41, 34]], columns=['Apples', 'Bananas'],
index=['2017 Sales', '2018 Sales'])
Fruit_sales.to_csv('fruit.csv')
print("DataFrame written to fruit.csv")