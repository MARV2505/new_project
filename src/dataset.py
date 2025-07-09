import pandas as pd

# Beispiel-CSV (wir nutzen die bekannte Titanic-Dataset als Standard – du kannst aber auch eine eigene CSV nehmen)
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

df = pd.read_csv(url)

# Die ersten 5 Zeilen anzeigen
df.head()

# Welche Spalten gibt es?
(df.columns)

# Kurzer Überblick (Infos, Anzahl Zeilen, fehlende Werte)
(df.info())
(df.describe())
