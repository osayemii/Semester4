import pandas as pd
import matplotlib.pyplot as plt
from nlp_sa_ml_confMatrix import *

feature_names = vectorizer.get_feature_names_out()
coefficients = model.coef_[0]

coef_df = pd.DataFrame({
    "Word": feature_names,
    "Coefficient": coefficients
})

top_positive = coef_df.nlargest(10, "Coefficient")
top_negative = coef_df.nsmallest(10, "Coefficient")

plt.figure(figsize=(10,5))

plt.barh(top_positive["Word"], top_positive["Coefficient"], color="green")
plt.title("Top Positive Words")
plt.xlabel("Coefficient")
plt.show()

plt.figure(figsize=(10,5))

plt.barh(top_negative["Word"], top_negative["Coefficient"], color="red")
plt.title("Top Negative Words")
plt.xlabel("Coefficient")
plt.show()