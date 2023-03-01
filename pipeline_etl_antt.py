from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime, timedelta
from airflow.models import Variable
import pandas as pd
import pyodbc
from urllib.parse import quote_plus
import sqlalchemy as sal
from sqlalchemy import create_engine, inspect
import os, re, json

default_args = {
    'owner': 'aiflow',
    'start_date': datetime(2023, 1, 1),
    'depends_on_past': False,
    'retries': 0,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    '1_pipeline_carga_tabelas_antt_v1',
    default_args=default_args,
    #    schedule_interval=timedelta(hours=10)
    schedule_interval=None
)

def load_producao_origem_destino(**kwargs):
    # lendo o arquivo de legendas
    mascara ='producao_origem_destino_2....csv$'


    # read path and mask of file
    path = '//opt//airflow//dags//'
    dir_list = os.listdir(path)
    # print the list
    list_arq = list()
    for pos, i in enumerate(dir_list):
        if re.search(mascara, i):
            list_arq.append(i)

    for para_arq in list_arq:
        dados = pd.read_csv(path+para_arq, sep=';',
                            encoding='latin1')

        # criando o dataframe
        df = pd.DataFrame(dados)

        df.rename(columns={'Mes_Ano': 'mesano',
                           'Ferrovia': 'ferrovia',
                           'Mercadoria_ANTT': 'mercadoriaantt',
                           'Estacao_Origem': 'estacaoorigem',
                           'UF_Origem': 'uforigem',
                           'Estacao_Destino': 'estacaodestino',
                           'UF_Destino': 'ufdestino',
                           'TU': 'tu',
                           'TKU': 'tku'}, inplace=True)
        # adcionando campo data
        df['mesano'] = pd.to_datetime(df['mesano'])
        df['tu'] = df['tu'].str.replace('.', '').astype(float)
        df['tku'] = df['tku'].str.replace('.', '').astype(float)
        df['tu'] = pd.to_numeric(df['tu'])
        df['tku'] = pd.to_numeric(df['tku'])

        server = '10.60.2.110\DENERGIA'
        database = 'FGV_ENERGIA_SILVER'
        username = 'FGV_ENERGIA_SILVER'
        passwd_2 = Variable.get("passwd_2")
        password = passwd_2

        # transformando para formato odbc
        parametros = (
                'DRIVER={ODBC Driver 18 for SQL Server};SERVER=' + server + ';PORT=4513;DATABASE=' + database + ';ENCRYPT=no;TrustServerCertificate=yes;UID=' + username + ';PWD=' + password)

        # passando a string de conexão para formato url
        url_db = quote_plus(parametros)

        # Estabelecendo conexão com o banco de dados
        engine = sal.create_engine('mssql+pyodbc:///?odbc_connect=%s' % url_db)

        # Estabelecendo a conexão com o banco de dados usando o mecanismo como interface
        conn = engine.connect()
        inspector = inspect(engine)

        # Criando uma nova tabela e/ou anexe os valores do quadro de dados a esta tabela existente

        df.to_sql('producao_origem_destino', schema='antt', con=engine, if_exists='append',
                  index=False, chunksize=1000)

        # fechando conexão
        conn.close()


start_task = DummyOperator(task_id='start_task', dag=dag)

producao_origem_destino = PythonOperator(
    task_id='load_producao_origem_destino',
    python_callable=load_producao_origem_destino,
    provide_context=True,
    dag=dag
)

end_task = DummyOperator(task_id='end_task', dag=dag)

start_task >> producao_origem_destino >> end_task
