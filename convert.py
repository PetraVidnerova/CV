import pandas as pd
import numpy as np

df = pd.read_csv("publikace.csv", encoding="utf-8", sep=";")

#print(df)


#print(df.columns)

#print(df["druh_dokumentu"].unique())
#      'K' 'D'


#selection = df[df["druh_dokumentu"] == "J"]
#selection = df[df["druh_dokumentu"] == "C"]
#selection = df[df["druh_dokumentu"] == "L4"]
## selection = df[df["druh_dokumentu"] == "M"]
selection = df[df["druh_dokumentu"] == "D"]

#print(selection)

wanted = ["autori", "nazev", "zdroj_dok", "cislovani", "isbn", "issn", "rok_vydani", "if"]
#selection = df[wanted]

selection["cislovani"] = selection["cislovani"].astype(str)

for i, row in selection.sort_values("rok_vydani", ascending=False).iterrows():
    # print(row)
    # print(type(row["isbn"]), row["isbn"])

    #    print(row)
    
    print(row["autori"], end=", ")
    nazev = row["nazev"]
    print("{\\em ", end="")
    print(nazev, end="")
    print("}", end=", ")
    print(row["zdroj_dok"], end=", ")
    print(row["cislovani"].replace("Roč.", "").replace("č.", "no.").replace("s.", "pages").replace("S.", "pages"), end="")
    if row["isbn"] is not np.nan:
        print(", ISBN", row["isbn"], end="")
    if row["issn"] is not np.nan:
        print(", ISSN", row["issn"], end="")

    print()    
    print()
    print("\\vspace{2em}")
    print("\\noindent")
