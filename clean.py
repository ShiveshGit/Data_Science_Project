def clean_dataset(data):
    print("Removing outliers")
    data = data[data['wage per hour']<5000]
    data = data[data['capital gains']<15000]
    data = data[data['capital losses']<3500]
    data = data[data['dividends from stocks']<2500]
    print("Data Shape after removing outliers : ",data.shape)
    return data