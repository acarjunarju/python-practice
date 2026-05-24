import pandas as pd

df = pd.DataFrame({
"Marks":[70,80,90]
})

print(df["Marks"].mean())
