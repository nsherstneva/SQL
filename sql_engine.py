
# %%
from sqlalchemy import create_engine
import urllib
import pyodbc
import pandas as pd

df1 = pd.DataFrame({'PersonID': [2,3,4],
                    'LastName' : ['Sonia', 'Priya', 'me'],
                    'FirstName':['re','mu', 'ku']})
#print('Load df', df)

def created_server():
    quoted = urllib.parse.quote_plus("DRIVER={SQL Server};SERVER=DESKTOP-R3MHCGP\SQLEXPRESS;DATABASE=Pandas_test")
    engine = create_engine('mssql+pyodbc:///?odbc_connect={}'.format(quoted))
    print('Created engine ', engine)
    df1.to_sql('iowa', schema='dbo', con = engine,index=False, if_exists='replace')
    print('Done ')

