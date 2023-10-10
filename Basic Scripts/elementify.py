import pandas as pd

df = pd.read_csv("https://gist.githubusercontent.com/GoodmanSciences/c2dd862cd38f21b0ad36b8f96b4bf1ee/raw/1d92663004489a5b6926e944c1b3d9ec5c40900e/Periodic%2520Table%2520of%2520Elements.csv")

flag1 = False

df["Symbol"] = df['Symbol'].str.lower()

text = input("enter text: ") 
text = text.lower() + "0"

for i in range(len(text)-1):
    n1 = text[i]
    n2 = text[i]+text[i+1]
    
    if flag1:
        flag1 = False
    
    elif n2 in list(df["Symbol"]):
        name = df["Element"][df.index[df["Symbol"]==n2].tolist()[0]]
        print(n2,name)
        flag1 = True
        continue
    
    elif n1 in list(df["Symbol"]):
        name = df["Element"][df.index[df["Symbol"]==n1].tolist()[0]]
        print(n1,name)
    elif n1==" ":
        print()
    else:
        print(n1)

        
    
