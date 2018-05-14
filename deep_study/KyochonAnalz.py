import pandas as pd
sido_table = pd.read_csv('district.csv', encoding='CP949', index_col=0, header=0)
sido_table

gungu_alias= """ 고양시  부천시오정구:부천시  천안시동남구:천안시  부강면:세종시  연서면:세종시  
창원시진해구:창원시 청주시흥덕구:청주시  여주군:여주시   청주시서원구:청주시  용인시기흥구:용인시   
고양시일산서구:나리로:세종시  갈매로:세종시  성남시수정구:성남시   청주시상당구:청주시  
전의면:세종시  조치원읍:세종시  전주시완산구:전주시  창원시마산합포구:창원시   당진군:당진시 
안산시단원구:안산시  부천시소사구:부천시  안산시상록구:안산시  수원시장안구:수원시 
고양시일산동구:고양시  천안시서북구:천안시  안양시동안구:안양시  부천시원미구:부천시  
전주시덕진구:전주시  포항시북구:포항시  창원시마산회원구:창원시   창원시성산구:창원시  
안양시만안구:안양시  포항시남구:포항시   수원시권선구:수원시   고양시덕양구:고양시 
청원군:청주시   용인시수지구:용인시   수원시영릉구:수원시  용인시처인구:용인시 
수원시팔달구:수원시   수원시영통구:수원시   성남시중원구:성남시  성남시분당구:성남시  """




filename ='kyochon.csv'
kyochon_table = pd.read_csv(filename, encoding='CP949', index_col=0, header=0)
print(kyochon_table.sido.unique())

sido_alias= """ 서울:서울특별시   부산:부산광역시  부산시:부산광역시  
대구:대구광역시   대구시:대구광역시 인천:인천광역시  광주:광주광역시  
대전:대전광역시  울산:울산광역시   세종:세종특별자치시  세종시:세종특별자치시  경기:경기도  강원:강원도   충북:충청북도  충남:충청남도   전북:전라북도   
전남:전라남도     경북:경상북도    경남:경상남도   제주:제주특별자치도  """
sido_dict = dict(aliasset.split(':') for aliasset in sido_alias.split())
kyochon_table.sido = kyochon_table.sido.apply(lambda v: sido_dict.get(v,v))
print(kyochon_table.sido.unique())

m = kyochon_table.merge(sido_table, on=['sido', 'gungu'], how='outer', suffixes=['', '_'], indicator=True)
m_result = m.query('_merge=="left_only" ')
print(m_result[['sido','gungu']])

gungu_dict = dict(aliasset.split(':') for aliasset in gungu_alias.split())
kyochon_table.gungu = kyochon_table.gungu.apply(lambda v: gungu_dict.get(v,v))
m = kyochon_table.merge(sido_table, on= ['sido', 'gungu'], how='outer', suffixes=['', '_'], indicator=True)
m_result = m.query('_merge =="left_only"')
print(m_result[['sido', 'gungu']])
