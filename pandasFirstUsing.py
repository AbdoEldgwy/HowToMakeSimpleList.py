import pandas as pd


DataName = []
DataAge = []
DataSpec = []
DataEmail = []

while True:
    inpName = input("type your Name: ")
    inpAge = input("type your age: ")
    inpSpecialty = input("type your specialty: ")
    email = f"{inpName}{inpSpecialty}{inpAge}@ai.com"

    DataName.append(inpName)
    DataAge.append(inpAge)
    DataSpec.append(inpSpecialty)
    DataEmail.append(email)

    RowData = {"name": DataName,
               "age": DataAge,
               "specialty": DataSpec,
               "Email": DataEmail}

    df1 = pd.DataFrame(RowData)
    print(df1)
