import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules



transactions = [
    ['bread', 'milk'],
    ['bread', 'diapers', 'beer', 'eggs'],
    ['milk', 'diapers', 'beer', 'cola'],
    ['bread', 'milk', 'diapers', 'beer'],
    ['bread', 'milk', 'diapers', 'cola']
]



te = TransactionEncoder()
te_data = te.fit(transactions).transform(transactions)

df = pd.DataFrame(te_data, columns=te.columns_)

print("Дані:")
print(df)



frequent_itemsets = apriori(df, min_support=0.4, use_colnames=True)

print("\nЧасті набори:")
print(frequent_itemsets)



rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.6)

print("\nАсоціативні правила:")
print(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']])
