import pandas as pd
data_train = pd.read_csv("dataset\\train.csv")  
data_test  = pd.read_csv("dataset\\test.csv")

data = pd.concat([data_train, data_test],axis=0, ignore_index=True)        
print(data.shape)
print(data.columns)

integer_cols = ['age', 'industry code', 'occupation code', 'education', 'wage per hour', 'full or part time employment stat', 'capital gains', 'capital losses', 'live in this house 1 year ago', 'country of birth mother', 'citizenship', 'own business or self employed', '94 or 95']
# continuous col = detailed household summary in household
cont_cols = ['age','wage per hour','capital gains','capital losses','dividends from stocks','num persons worked for employer','weeks worked in year']