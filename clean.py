# def clean_dataset(data,categorical_features,numerical_features):
#     print("Removing outliers")
#     data = data[data['HeightInMeters']>=1]
#     data = data[data['HeightInMeters']<=2.2]

#     data = data[data['WeightInKilograms']>=10]
#     data = data[data['WeightInKilograms']<=270]

#     data = data[data['SleepHours']>=0]
#     data = data[data['SleepHours']<=20]
#     print("Imputing missing values ")
#     for col in categorical_features:
#         data[col].fillna(data[col].mode()[0],inplace=True)
#     for col in numerical_columns:
#         data[col].fillna(data[col].median(), inplace=True)
    
    