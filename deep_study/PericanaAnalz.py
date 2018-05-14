import pandas as pd

filename = 'C:/Users/user/PycharmProjects/deeplearning/deep_study/pericana.csv'
pericana_table = pd.read_csv(filename, encoding='CP949', index_col=0, header=0)
pericana_table.sido.unique()

#필요없는 값 '0'제거
print(pericana_table[pericana_table['sido']=='0'])
#sido가 0인것은 index가 1166였음.
#pericana_table = pericana_table.drop(pericana_table.index[1166])
pericana_table[pericana_table['sido']=='0']

#필요없는 값 '테스트'찾기.
print(pericana_table[pericana_table['sido']=='테스트'])

pericana_table = pericana_table.drop(pericana_table.index[798])
print(pericana_table[pericana_table['sido']=='테스트'])

print(pericana_table[pericana_table['sido']==' '])
pericana_table = pericana_table[pericana_table['sido'] != ' ']
pericana_table.sido.unique()
