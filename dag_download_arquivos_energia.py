from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime, timedelta
from airflow.models import Variable
import urllib3 as ur
from bs4 import BeautifulSoup
import requests
import zipfile
import os

default_args = {
    'owner': 'aiflow',
    'start_date': datetime(2023, 1, 1),
    'depends_on_past': False,
    'retries': 0,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    '1_download_arquivos_energia',
    default_args=default_args,
    #    schedule_interval=timedelta(hours=10)
    schedule_interval=None
)

def baixa_arquivos_antaq(**kwargs):
    anos_interesse =[Variable.get("anos_p_download")]
    nome_arquivo = ['Atracacao', 'Carga', 'CargaConteinerizada', 'CargaRegiao_Hidrovia_Rio', 'TemposAtracacao', 'AcordosBilaterais', 'TaxaOcupacao']

    directory_external = Variable.get("diretório_dowload")

    if not os.path.exists(directory_external):
        os.makedirs(directory_external)


    if not os.path.exists(directory_external):
        os.makedirs(directory_external)

    for arquivo in nome_arquivo:
        for ano in anos_interesse:
            url_atracacao = f'http://web.antaq.gov.br/Sistemas/ArquivosAnuario/Arquivos/{ano}{arquivo}.zip'
            zipurl = url_atracacao
            resp = requests.get(zipurl)
            zname = f"{directory_external}{ano}{arquivo}.zip"
            zfile = open(zname, 'wb')
            zfile.write(resp.content)
            zfile.close()

    directory_raw = Variable.get("diretorio_raw")

    if not os.path.exists(directory_raw):
        os.makedirs(directory_raw)


    for ano in anos_interesse:
        for arquivo in nome_arquivo:
            #print(zipfile.is_zipfile(f"{directory_external}{ano}{arquivo}.zip"))
            with zipfile.ZipFile(f"{directory_external}{ano}{arquivo}.zip", 'r') as zip_ref:
                zip_ref.extractall(f"{directory_raw}")

start_task = DummyOperator(task_id='start_task', dag=dag)

baixa_arquivos_antaq = PythonOperator(
    task_id='baixa_arquivos_antaq',
    python_callable=baixa_arquivos_antaq,
    provide_context=True,
    dag=dag
)

def baixa_arquivos_antt(**kwargs):
    ano_interresse = [Variable.get("anos_p_download")]

    url = 'https://dados.antt.gov.br/dataset/sistema-de-acompanhamento-do-desempenho-operacional-das-concessionarias-siade'
    conexao = ur.PoolManager()
    retorno = conexao.request('GET', url)


    pagina = BeautifulSoup(retorno.data, "html.parser")


    dado = []
    for link in pagina.find_all('a', class_='resource-url-analytics'):
            dado.append(link.get('href'))


    lista = []
    for ano in ano_interresse:
        for dados in dado:
            if dados[150:] == f"{ano}.csv":
                lista.append(dados)


    directory_external = Variable.get("diretório_dowload")
    #directory_external = 'C:\\FGVENERGIA\\ANTT\\DOWNLOAD\\'

    if not os.path.exists(directory_external):
        os.makedirs(directory_external)

    for ano in ano_interresse:
        for link_antt in lista:
                url_atracacao = f'{link_antt}'
                print(url_atracacao)
                zipurl = url_atracacao
                resp = requests.get(zipurl)
                zname = f"{directory_external}{link_antt[126:]}"
                print(zname)
                zfile = open(zname, 'wb')
                zfile.write(resp.content)
                zfile.close()

    directory_raw = Variable.get("diretório_raw")
    #directory_raw = 'C:\\FGVENERGIA\\ANTT\\DOWNLOAD\\RAW\\'

    if not os.path.exists(directory_raw):
        os.makedirs(directory_raw)

    #Zipando os arquivos para ficar no PATH
    for link_antt in lista:
        with zipfile.ZipFile(f"{directory_external}{link_antt[126:]}.zip", 'w') as myzip:
            myzip.write(f"{directory_external}{link_antt[126:]}", f"{link_antt[126:]}")
            myzip.close()
            os.remove(f"{directory_external}{link_antt[126:]}")

    #Descompactando na RAW
    for link_antt in lista:
        with zipfile.ZipFile(f"{directory_external}{link_antt[126:]}.zip", 'r') as zip_ref:
            zip_ref.extractall(f"{directory_raw}")
            zip_ref.close()

baixa_arquivos_antt = PythonOperator(
    task_id='baixa_arquivos_antt',
    python_callable=baixa_arquivos_antt,
    provide_context=True,
    dag=dag
)


def baixa_arquivos_anp(**kwargs):

    nome_arquivo = ['liquidos-metadado']

    directory_external = Variable.get("diretório_dowload")

    if not os.path.exists(directory_external):
        os.makedirs(directory_external)


    if not os.path.exists(directory_external):
        os.makedirs(directory_external)

    for arquivo in nome_arquivo:
        url_atracacao = f'https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/mdpg/{arquivo}.zip'
        zipurl = url_atracacao
        resp = requests.get(zipurl)
        zname = f"{directory_external}{arquivo}.zip"
        zfile = open(zname, 'wb')
        zfile.write(resp.content)
        zfile.close()

    directory_raw = Variable.get("diretorio_raw")

    if not os.path.exists(directory_raw):
        os.makedirs(directory_raw)


  
    for arquivo in nome_arquivo:
        #print(zipfile.is_zipfile(f"{directory_external}{ano}{arquivo}.zip"))
        with zipfile.ZipFile(f"{directory_external}{ano}{arquivo}.zip", 'r') as zip_ref:
            zip_ref.extractall(f"{directory_raw}")
            
baixa_arquivos_anp = PythonOperator(
    task_id='baixa_arquivos_anp',
    python_callable=baixa_arquivos_anp,
    provide_context=True,
    dag=dag
)

end_task = DummyOperator(task_id='end_task', dag=dag)

start_task >> baixa_arquivos_antaq >> end_task
start_task >> baixa_arquivos_antt >> end_task
start_task >> baixa_arquivos_anp >> end_task
