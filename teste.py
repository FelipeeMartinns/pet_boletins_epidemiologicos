import pandas as pd



arquivo= 'sinannet_cnv_zika.csv'


data_frame= pd.read_csv(arquivo,sep=';',encoding='latin-1',skiprows=3)


print(data_frame.columns)

rd=data_frame.head(10)

#print(rd)

print('todos os totais')
print(rd['Total'])

rd=pd.to_numeric(rd['Total'],errors='coerce')
soma_total=rd.sum()

""" data_frame['Total'] = pd.to_numeric(data_frame['Total'],errors='coerce') """

print(f'soma total é igual a: {soma_total}')