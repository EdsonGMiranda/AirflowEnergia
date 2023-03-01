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
    'pipeline_carga_tabelas_anp_liquids_v2',
    default_args=default_args,
    #    schedule_interval=timedelta(hours=10)
    schedule_interval=None
)


def extract_liquidos_distribuidor_atual(**kwargs):
    # lendo o arquivo de legendas
    dados = pd.read_csv('//opt//airflow//dags//Liquidos_Entregas_Distribuidor_Atual.csv', sep=';',
                        encoding='latin1')

    # criando o dataframe
    df = pd.DataFrame(dados)

    # # transformando em Json para passar em Xcomm
    dados = df.to_json(orient="records")
    #data = json.loads(df)
    return dados


def transform_liquidos_distribuidor_atual(**kwargs):
    data = kwargs['ti'].xcom_pull(task_ids='extract_liquidos_distribuidor_atual')
    df = pd.read_json(data)
    # transformação dos nomes das colunas
    df.rename(columns={'Ano': 'ano',
                       'Mês': 'mes',
                       'Distribuidor': 'distribuidor',
                       'Código do Produto': 'codproduto',
                       'Nome do Produto': 'nomeproduto',
                       'Região': 'regiao',
                       'Quantidade de Produto (mil m³)': 'qtdproduto'}, inplace=True)

    # trocando o , por . em campo float
    df['qtdproduto'] = df['qtdproduto'].str.replace(',', '.')
    df['qtdproduto'] = df['qtdproduto'].astype(float)
    # print(df.dtypes)
    # Store data in XCom
    data = df.to_json(orient="records")

    return data


def load_liquidos_distribuidor_atual(**kwargs):
    data = kwargs['ti'].xcom_pull(task_ids='transform_liquidos_distribuidor_atual')
    df = pd.read_json(data)
    # parametros de banco de dados
    server = '10.60.2.110\DENERGIA'
    database = 'FGV_ENERGIA_DE'
    username = 'FGV_ENERGIA_DE'
    passwd = Variable.get("passwd")
    password = passwd

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

    # Lendo uma consulta SQL usando pandas
    # query = "SELECT * FROM [antaq].[AcordosBilaterais]"
    # result = pd.read_sql(query,engine)
    # print(result)

    # Criando uma nova tabela e/ou anexe os valores do quadro de dados a esta tabela existente

    df.to_sql('liquidos_entregas_distribuidor_atual', schema='anp', con=engine, if_exists='append',
              index=False, chunksize=1000)

    # fechando conexão
    conn.close()


start_task = DummyOperator(task_id='start_task', dag=dag)


extract_liquidos_distribuidor_atual = PythonOperator(
    task_id='extract_liquidos_distribuidor_atual',
    python_callable=extract_liquidos_distribuidor_atual,
    provide_context=True,
    dag=dag
)


transform_liquidos_distribuidor_atual = PythonOperator(
    task_id='transform_liquidos_distribuidor_atual',
    python_callable=transform_liquidos_distribuidor_atual,
    provide_context=True,
    dag=dag
)


load_liquidos_distribuidor_atual = PythonOperator(
    task_id='load_liquidos_distribuidor_atual',
    python_callable=load_liquidos_distribuidor_atual,
    provide_context=True,
    dag=dag
)


# novo
def extract_liquidos_entregas_fornecedor_atual(**kwargs):
    # lendo o arquivo de legendas
    dados = pd.read_csv('//opt//airflow//dags//Liquidos_Entregas_Fornecedor_Atual.csv', sep=';',
                        encoding='latin1')

    # criando o dataframe
    df = pd.DataFrame(dados)

    # # transformando em Json para passar em Xcomm
    dados = df.to_json(orient="records")
    #data = json.loads(df)
    return dados


def transform_liquidos_entregas_fornecedor_atual(**kwargs):
    data = kwargs['ti'].xcom_pull(task_ids='extract_liquidos_entregas_fornecedor_atual')
    df = pd.read_json(data)
    # transformação dos nomes das colunas
    df.rename(columns={'Ano': 'ano',
                       'Mês': 'mes',
                       'Fornecedor': 'fornecedor',
                       'Código do Produto': 'codproduto',
                       'Nome do Produto': 'nomeproduto',
                       'Região': 'regiao',
                       'Quantidade de Produto (mil m³)': 'qtdproduto'}, inplace=True)

    # trocando o , por . em campo float
    df['qtdproduto'] = df['qtdproduto'].str.replace(',', '.')
    df['qtdproduto'] = df['qtdproduto'].astype(float)
    # print(df.dtypes)
    # Store data in XCom
    data = df.to_json(orient="records")

    return data


def load_liquidos_entregas_fornecedor_atual(**kwargs):
    data = kwargs['ti'].xcom_pull(task_ids='transform_liquidos_entregas_fornecedor_atual')
    df = pd.read_json(data)
    # parametros de banco de dados
    server = '10.60.2.110\DENERGIA'
    database = 'FGV_ENERGIA_DE'
    username = 'FGV_ENERGIA_DE'
    passwd = Variable.get("passwd")
    password = passwd

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

    # Lendo uma consulta SQL usando pandas
    # query = "SELECT * FROM [antaq].[AcordosBilaterais]"
    # result = pd.read_sql(query,engine)
    # print(result)

    # Criando uma nova tabela e/ou anexe os valores do quadro de dados a esta tabela existente

    df.to_sql('liquidos_entregas_fornecedor_atual', schema='anp', con=engine, if_exists='append',
              index=False, chunksize=1000)

    # fechando conexão
    conn.close()


extract_liquidos_entregas_fornecedor_atual = PythonOperator(
    task_id='extract_liquidos_entregas_fornecedor_atual',
    python_callable=extract_liquidos_entregas_fornecedor_atual,
    provide_context=True,
    dag=dag
)


transform_liquidos_entregas_fornecedor_atual = PythonOperator(
    task_id='transform_liquidos_entregas_fornecedor_atual',
    python_callable=transform_liquidos_entregas_fornecedor_atual,
    provide_context=True,
    dag=dag
)


load_liquidos_entregas_fornecedor_atual = PythonOperator(
    task_id='load_liquidos_entregas_fornecedor_atual',
    python_callable=load_liquidos_entregas_fornecedor_atual,
    provide_context=True,
    dag=dag
)

def extract_liquidos_entregas_historico(**kwargs):
    # lendo o arquivo de legendas
    dados = pd.read_csv('//opt//airflow//dags//Liquidos_Entregas_Historico.csv', sep=';',
                        encoding='latin1')

    # criando o dataframe
    df = pd.DataFrame(dados)

    # # transformando em Json para passar em Xcomm
    dados = df.to_json(orient="records")
    #data = json.loads(df)
    return dados


def transform_liquidos_entregas_historico(**kwargs):
    data = kwargs['ti'].xcom_pull(task_ids='extract_liquidos_entregas_historico')
    df = pd.read_json(data)
    # transformação dos nomes das colunas
    df.rename(columns={'Ano': 'ano',
                   'Mês': 'mes',
                   'Fornecedor Destino': 'fornecedor',
                   'Distribuidor Origem': 'distribuidor',
                   'Código do Produto': 'codproduto',
                   'Nome do Produto': 'nomeproduto',
                   'Região Origem': 'regiaoorigem',
                   'UF Origem': 'uforigem',
                   'Localidade Destino': 'localidadedestino',
                   'Região Destinatário': 'regiaodestinatario',
                   'UF Destino': 'ufdestino',
                   'Quantidade de Produto (mil m³)': 'qtdproduto'}, inplace=True)

    # trocando o , por . em campo float
    df['qtdproduto'] = df['qtdproduto'].str.replace(',', '.')
    df['qtdproduto'] = df['qtdproduto'].astype(float)
    # print(df.dtypes)
    # Store data in XCom
    data = df.to_json(orient="records")

    return data


def load_liquidos_entregas_historico(**kwargs):
    data = kwargs['ti'].xcom_pull(task_ids='transform_liquidos_entregas_historico')
    df = pd.read_json(data)
    # parametros de banco de dados
    server = '10.60.2.110\DENERGIA'
    database = 'FGV_ENERGIA_DE'
    username = 'FGV_ENERGIA_DE'
    passwd = Variable.get("passwd")
    password = passwd

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

    # Lendo uma consulta SQL usando pandas
    # query = "SELECT * FROM [antaq].[AcordosBilaterais]"
    # result = pd.read_sql(query,engine)
    # print(result)

    # Criando uma nova tabela e/ou anexe os valores do quadro de dados a esta tabela existente

    df.to_sql('liquidos_entregas_historico', schema='anp', con=engine, if_exists='append',
              index=False, chunksize=1000)

    # fechando conexão
    conn.close()


extract_liquidos_entregas_historico = PythonOperator(
    task_id='extract_liquidos_entregas_historico',
    python_callable=extract_liquidos_entregas_historico,
    provide_context=True,
    dag=dag
)


transform_liquidos_entregas_historico = PythonOperator(
    task_id='transform_liquidos_entregas_historico',
    python_callable=transform_liquidos_entregas_historico,
    provide_context=True,
    dag=dag
)


load_liquidos_entregas_historico = PythonOperator(
    task_id='load_liquidos_entregas_historico',
    python_callable=load_liquidos_entregas_historico,
    provide_context=True,
    dag=dag
)


def extract_liquidos_vendas_atual(**kwargs):
    # lendo o arquivo de legendas
    dados = pd.read_csv('//opt//airflow//dags//Liquidos_Vendas_Atual.csv', sep=';',
                        encoding='latin1')

    # criando o dataframe
    df = pd.DataFrame(dados)

    # # transformando em Json para passar em Xcomm
    dados = df.to_json(orient="records")
    #data = json.loads(df)
    return dados


def transform_liquidos_vendas_atual(**kwargs):
    data = kwargs['ti'].xcom_pull(task_ids='extract_liquidos_vendas_atual')
    df = pd.read_json(data)
    # transformação dos nomes das colunas
    df.rename(columns={'Ano': 'ano',
                   'Mês': 'mes',
                   'Agente Regulado':'agenteregulado',
                   'Código do Produto': 'codproduto',
                   'Nome do Produto': 'nomeproduto',
                   'Região Origem': 'regiaoorigem',
                   'Região Destinatário': 'regiaodestinatario',
                   'Mercado Destinatário': 'mercadodestinatario',
                   'Quantidade de Produto (mil m³)': 'qtdproduto'}, inplace=True)

    # trocando o , por . em campo float
    df['qtdproduto'] = df['qtdproduto'].str.replace(',', '.')
    df['qtdproduto'] = df['qtdproduto'].astype(float)
    # print(df.dtypes)
    # Store data in XCom
    data = df.to_json(orient="records")

    return data


def load_liquidos_vendas_atual(**kwargs):
    data = kwargs['ti'].xcom_pull(task_ids='transform_liquidos_vendas_atual')
    df = pd.read_json(data)
    # parametros de banco de dados
    server = '10.60.2.110\DENERGIA'
    database = 'FGV_ENERGIA_DE'
    username = 'FGV_ENERGIA_DE'
    passwd = Variable.get("passwd")
    password = passwd

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

    # Lendo uma consulta SQL usando pandas
    # query = "SELECT * FROM [antaq].[AcordosBilaterais]"
    # result = pd.read_sql(query,engine)
    # print(result)

    # Criando uma nova tabela e/ou anexe os valores do quadro de dados a esta tabela existente

    df.to_sql('liquidos_vendas_atual', schema='anp', con=engine, if_exists='append',
              index=False, chunksize=1000)

    # fechando conexão
    conn.close()


extract_liquidos_vendas_atual = PythonOperator(
    task_id='extract_liquidos_vendas_atual',
    python_callable=extract_liquidos_vendas_atual,
    provide_context=True,
    dag=dag
)


transform_liquidos_vendas_atual = PythonOperator(
    task_id='transform_liquidos_vendas_atual',
    python_callable=transform_liquidos_vendas_atual,
    provide_context=True,
    dag=dag
)


load_liquidos_vendas_atual = PythonOperator(
    task_id='load_liquidos_vendas_atual',
    python_callable=load_liquidos_vendas_atual,
    provide_context=True,
    dag=dag
)


def extract_liquidos_venda_historico(**kwargs):
    return 'passou aqui'


def transform_liquidos_venda_historico(**kwargs):
    return 'passou aqui 2'


def load_liquidos_venda_historico(**kwargs):
    # lendo o arquivo de legendas
    dados = pd.read_csv('//opt//airflow//dags//Liquidos_Vendas_Historico.csv', sep=';',
                        encoding='latin1')
    # criando o dataframe
    df = pd.DataFrame(dados)
    # transformação dos nomes das colunas
    df.rename(columns={'Ano': 'ano',
                       'Mês': 'mes',
                       'Agente Regulado': 'agenteregulado',
                       'Código do Produto': 'codproduto',
                       'Nome do Produto': 'nomeproduto',
                       'Região Origem': 'regiaoorigem',
                       'UF Origem': 'uforigem',
                       'Região Destinatário': 'regiaodestinatario',
                       'UF Destino': 'ufdestino',
                       'Mercado Destinatário': 'mercadodestinatario',
                       'Quantidade de Produto (mil m³)': 'qtdproduto'}, inplace=True)

    # trocando o , por . em campo float
    df['qtdproduto'] = df['qtdproduto'].str.replace(',', '.')
    df['qtdproduto'] = df['qtdproduto'].astype(float)
    # print(df.dtypes)
    # parametros de banco de dados
    server = '10.60.2.110\DENERGIA'
    database = 'FGV_ENERGIA_DE'
    username = 'FGV_ENERGIA_DE'
    passwd = Variable.get("passwd")
    password = passwd

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

    # Lendo uma consulta SQL usando pandas
    # query = "SELECT * FROM [antaq].[AcordosBilaterais]"
    # result = pd.read_sql(query,engine)
    # print(result)

    # Criando uma nova tabela e/ou anexe os valores do quadro de dados a esta tabela existente

    df.to_sql('liquidos_vendas_historico', schema='anp', con=engine, if_exists='append',
              index=False, chunksize=1000)

    # fechando conexão
    conn.close()


extract_liquidos_venda_historico = PythonOperator(
    task_id='extract_liquidos_venda_historico',
    python_callable=extract_liquidos_venda_historico,
    provide_context=True,
    dag=dag
)


transform_liquidos_venda_historico = PythonOperator(
    task_id='transform_liquidos_venda_historico',
    python_callable=transform_liquidos_venda_historico,
    provide_context=True,
    dag=dag
)


load_liquidos_venda_historico = PythonOperator(
    task_id='load_liquidos_venda_historico',
    python_callable=load_liquidos_venda_historico,
    provide_context=True,
    dag=dag
)


def extract_liquidos_vendas_uf_atual(**kwargs):
    # lendo o arquivo de legendas
    dados = pd.read_csv('//opt//airflow//dags//Liquidos_Vendas_UF_Atual.csv', sep=';',
                        encoding='latin1')

    # criando o dataframe
    df = pd.DataFrame(dados)

    # # transformando em Json para passar em Xcomm
    dados = df.to_json(orient="records")
    #data = json.loads(df)
    return dados


def transform_liquidos_vendas_uf_atual(**kwargs):
    data = kwargs['ti'].xcom_pull(task_ids='extract_liquidos_vendas_uf_atual')
    df = pd.read_json(data)
    # transformação dos nomes das colunas
    df.rename(columns={'Ano': 'ano',
                   'Mês': 'mes',
                   'Código do Produto': 'codproduto',
                   'Nome do Produto': 'nomeproduto',
                   'UF de Origem': 'uforigem',
                   'Região Origem': 'regiaoorigem',
                   'UF de Destino': 'ufdestino',
                   'Região Destinatário': 'regiaodestinatario',
                   'Mercado Destinatário': 'mercadodestinatario',
                   'Quantidade de Produto (mil m³)': 'qtdproduto'}, inplace=True)

    # trocando o , por . em campo float
    df['qtdproduto'] = df['qtdproduto'].str.replace(',', '.')
    df['qtdproduto'] = df['qtdproduto'].astype(float)
    # print(df.dtypes)
    # Store data in XCom
    data = df.to_json(orient="records")

    return data


def load_liquidos_vendas_uf_atual(**kwargs):
    data = kwargs['ti'].xcom_pull(task_ids='transform_liquidos_vendas_uf_atual')
    df = pd.read_json(data)
    # parametros de banco de dados
    server = '10.60.2.110\DENERGIA'
    database = 'FGV_ENERGIA_DE'
    username = 'FGV_ENERGIA_DE'
    passwd = Variable.get("passwd")
    password = passwd

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

    # Lendo uma consulta SQL usando pandas
    # query = "SELECT * FROM [antaq].[AcordosBilaterais]"
    # result = pd.read_sql(query,engine)
    # print(result)

    # Criando uma nova tabela e/ou anexe os valores do quadro de dados a esta tabela existente

    df.to_sql('liquidos_vendas_uf_atual', schema='anp', con=engine, if_exists='append',
              index=False, chunksize=1000)

    # fechando conexão
    conn.close()


extract_liquidos_vendas_uf_atual = PythonOperator(
    task_id='extract_liquidos_vendas_uf_atual',
    python_callable=extract_liquidos_vendas_uf_atual,
    provide_context=True,
    dag=dag
)


transform_liquidos_vendas_uf_atual = PythonOperator(
    task_id='transform_liquidos_vendas_uf_atual',
    python_callable=transform_liquidos_vendas_uf_atual,
    provide_context=True,
    dag=dag
)


load_liquidos_vendas_uf_atual = PythonOperator(
    task_id='load_liquidos_vendas_uf_atual',
    python_callable=load_liquidos_vendas_uf_atual,
    provide_context=True,
    dag=dag
)



end_task = DummyOperator(task_id='end_task', dag=dag)


start_task >> extract_liquidos_distribuidor_atual >> transform_liquidos_distribuidor_atual >> load_liquidos_distribuidor_atual >> end_task

start_task >> extract_liquidos_entregas_fornecedor_atual >> transform_liquidos_entregas_fornecedor_atual >> load_liquidos_entregas_fornecedor_atual  >> end_task

start_task >> extract_liquidos_entregas_fornecedor_atual >> transform_liquidos_entregas_fornecedor_atual >> load_liquidos_entregas_fornecedor_atual  >> end_task

start_task >> extract_liquidos_entregas_historico >> transform_liquidos_entregas_historico >> load_liquidos_entregas_historico  >> end_task

start_task >> extract_liquidos_vendas_atual >> transform_liquidos_vendas_atual >> load_liquidos_vendas_atual  >> end_task

start_task >> extract_liquidos_venda_historico >> transform_liquidos_venda_historico >> load_liquidos_venda_historico  >> end_task

start_task >> extract_liquidos_vendas_uf_atual >> transform_liquidos_vendas_uf_atual >> load_liquidos_vendas_uf_atual  >> end_task
