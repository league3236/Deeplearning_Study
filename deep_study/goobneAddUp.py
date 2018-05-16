import pandas as pd # 판다스 사용
filename ='goobne.csv'

goobne_table = pd.read_csv(filename, encoding='CP949', index_col=0, header=0)
print(goobne_table.sido.unique())

print(goobne_table[goobne_table['sido']=='0'])
print(goobne_table[goobne_table['sido']==''])
print(goobne_table[goobne_table['sido']==' '])

goobne_table = goobne_table.drop([473,509,700,839,898])

print(goobne_table[goobne_table['sido']==' '])
print(goobne_table.sido.unique())

sido_table = pd.read_csv('district.csv', encoding='CP949', index_col=0, header=0)
print(sido_table)

m = goobne_table.merge(sido_table, on=['sido', 'gungu'], how='outer', suffixes=['', '_'], indicator=True)

m_result = m.query('_merge=="left_only" ')
print(m_result)

print(m_result[['sido','gungu']])

gungu_alias = """청주시흥덕구:청주시  여주군:여주시   청주시서원구:청주시  용인시기흥구:용인시   
고양시일산서구:고양시  부천시오정구:부천시  천안시동남구:천안시  부강면:세종시  연서면:세종시  
창원시진해구:창원시  나리로:세종시  갈매로:세종시  성남시수정구:성남시   청주시상당구:청주시  
전의면:세종시  조치원읍:세종시  전주시완산구:전주시  창원시마산합포구:창원시   당진군:당진시 
안산시단원구:안산시  부천시소사구:부천시  안산시상록구:안산시  수원시장안구:수원시 
고양시일산동구:고양시  천안시서북구:천안시  안양시동안구:안양시  부천시원미구:부천시  
전주시덕진구:전주시  포항시북구:포항시  창원시마산회원구:창원시   창원시성산구:창원시  
안양시만안구:안양시  포항시남구:포항시   수원시권선구:수원시   고양시덕양구:고양시 
청원군:청주시   용인시수지구:용인시   수원시영릉구:수원시   청주시청원구:청주시   성남시분당구:성남시
용인시처인구:용인시   수원시팔달구:수원시   누리로:세종시   도움3로:세종시   보듬3로:세종시   성남시중원구:성남시
수원시영통구:수원시   마산회원구:마산시 창원시의창구:창원시
                """

gungu_dict = dict()
for aliasset in gungu_alias.split():
    s = aliasset.split(':')
    gungu_dict.update({s[0]: s[1]})

goobne_table.gungu = goobne_table.gungu.apply(lambda v: gungu_dict.get(v,v))
m = goobne_table.merge(sido_table, on= ['sido', 'gungu'], how='outer', suffixes=['', '_'], indicator=True)
m_result = m.query('_merge =="left_only"')
print("여기서 수정해야함")
print(m_result[['sido','gungu']])

goobne_table.to_csv('goobne_modify.csv', encoding="euc-kr", mode='a', header=False)
