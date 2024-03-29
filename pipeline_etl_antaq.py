import csv
import os
import re
from datetime import datetime, timedelta

import pyodbc
from airflow import DAG
from airflow.models import Variable
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator

default_args = {
    'owner': 'aiflow',
    'start_date': datetime(2022, 1, 1),
    'depends_on_past': False,
    'retries': 0 ,
    'retry_delay': timedelta(minutes=5)
}


dag = DAG(
    '1_pipeline_carga_tabelas_antaq_silver_v1',
    default_args=default_args,
#    schedule_interval=timedelta(hours=10)
    schedule_interval=None
)

def dataformat(str=""):
    return f'CONVERT(datetime, \'{str}\', 103)'

def moeda(n=0):
    return f'{n}'.replace('.', '')


def formatar(n=0):
    return f'{n}'.replace(',', '.')


def formatnull(n):
    if n == '':
        n = 'NULL'
    return f'{n}'

def remove_caractere(string, caractere):
    nova_string = string.replace(caractere, '')
    return nova_string

directory_raw = Variable.get("diretorio_raw")

start_task = DummyOperator(task_id='start_task', dag=dag)

def read_csv_and_insert_atracacao(**kwargs):
    passwd_2 = Variable.get("passwd_2")
    # Connect to the SQL Server
    #server = 'SQLDC1VDH0003\DENERGIA'
    server = '10.60.2.110\DENERGIA'
    database = 'FGV_ENERGIA_SILVER'
    username = 'FGV_ENERGIA_SILVER'
    password = passwd_2
    mascara = '^2...Atracacao.txt$'
    cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 18 for SQL Server};SERVER=' + server + ',4513;DATABASE=' + database + ';ENCRYPT=NO;TrustServerCertificate=yes;UID=' + username + ';PWD=' + password)
    cursor = cnxn.cursor()

    # read path and mask of file
    path = directory_raw
    dir_list = os.listdir(path)
    # print the list
    list_arq = list()
    for pos, i in enumerate(dir_list):
        if re.search(mascara, i):
            list_arq.append(i)

    for para_arq in list_arq:
        with open(path+para_arq, mode='r',
                  encoding='utf8') as arq:
            leitor = csv.reader(arq, delimiter=';')
            linha = 0
            for pos, coluna in enumerate(leitor):
                if linha == 0:
                    print(f'Colunas: {" ".join(coluna)}')
                    print(f'{len(coluna)}')
                    linha += 1
                else:
                    count = cursor.execute(
                        f"""INSERT INTO [antaq].[atracacao] ([idatracacao],[cdtup],[idberco],[berco],[portoatracacao],[apelidoinstalacaoportuaria],[complexoportuario],[tipodaautoridadeportuária],[dataatracacao],[datachegada],[datadesatracacao],[datainiciooperacao],[dataterminooperacao],[ano],[mes],[tipodeoperacao],[tipodenavegacaodaatracacao],[nacionalidadedoarmador],[flagmcoperacaoatracacao],[terminal],[municipio],[uf],[sguf],[regiaogeografica],[ndacapitania],[ndoimo]) values({coluna[0]},
                    \'{coluna[1]}\',
                    \'{coluna[2]}\',
                    \'{coluna[3]}\',
                    \'{remove_caractere(coluna[4],"'")}\',
                    \'{coluna[5]}\',
                    \'{coluna[6]}\',
                    \'{coluna[7]}\',
                    {dataformat(coluna[8])},
                    {dataformat(coluna[9])},
                    {dataformat(coluna[10])},
                    {dataformat(coluna[11])},
                    {dataformat(coluna[12])},
                    {formatnull(coluna[13])},
                    \'{coluna[14]}\',
                    \'{coluna[15]}\',
                    \'{coluna[16]}\',
                    {formatnull(coluna[17])},
                    {formatnull(coluna[18])},
                    \'{remove_caractere(coluna[19],"'")}\',
                    \'{coluna[20]}\',
                    \'{coluna[21]}\',
                    \'{coluna[22]}\',
                    \'{coluna[23]}\',
                    \'{formatnull(coluna[24])}\',
                    {formatnull(coluna[25])})""").rowcount
                    cursor.commit()
                    linha+=1

        print('Rows inserted: ' + str(linha))
        print(f'Imput {linha} no banco')


atracacao = PythonOperator(
    task_id='read_csv_and_insert_atracacao',
    python_callable=read_csv_and_insert_atracacao,
    provide_context=True,
    dag=dag
)


def read_csv_and_insert_acordosbilaterais(**kwargs):
    passwd_2 = Variable.get("passwd_2")
    # Connect to the SQL Server
    #server = 'SQLDC1VDH0003\DENERGIA'
    server = '10.60.2.110\DENERGIA'
    database = 'FGV_ENERGIA_SILVER'
    username = 'FGV_ENERGIA_SILVER'
    password = passwd_2
    mascara = '^2...AcordosBilaterais.txt$'
    cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 18 for SQL Server};SERVER=' + server + ',4513;DATABASE=' + database + ';ENCRYPT=NO;TrustServerCertificate=yes;UID=' + username + ';PWD=' + password)
    cursor = cnxn.cursor()

    # read path and mask of file
    path = directory_raw
    dir_list = os.listdir(path)
    # print the list
    list_arq = list()
    for pos, i in enumerate(dir_list):
        if re.search(mascara, i):
            list_arq.append(i)

    for para_arq in list_arq:
        with open(path+para_arq, mode='r', encoding='utf8') as arq:
            leitor = csv.reader(arq, delimiter=';')
            linha = 0
            for pos, coluna in enumerate(leitor):
                if linha == 0:
                    print(f'Colunas: {" ".join(coluna)}')
                    print(f'{len(coluna)}')
                    linha += 1
                else:
                    count = cursor.execute(
                        f"""INSERT INTO [antaq].[acordos_bilaterais] ([nacionalidadeembarcacao],[anoacordobilateral],[totalacordobilateral],[acordotiponavegacao],[pais],[flagembarquedesembarque],[ano]) values(\'{coluna[0]}\',
                    \'{coluna[1]}\',
                    {formatar(coluna[2])},
                    \'{coluna[3]}\',
                    \'{coluna[4]}\',
                    {formatar(coluna[5])},
                    \'{'01-01-2022'}\')""").rowcount
                    cnxn.commit()
                    linha += 1

        print('Rows inserted: ' + str(linha))
        print(f'Imput {linha} no banco')


acordosbilaterais = PythonOperator(
    task_id='read_csv_and_insert_acordosbilaterais',
    python_callable=read_csv_and_insert_acordosbilaterais,
    provide_context=True,
    dag=dag
)


def read_csv_and_insert_carga(**kwargs):
    passwd_2 = Variable.get("passwd_2")
    # Connect to the SQL Server
    #server = 'SQLDC1VDH0003\DENERGIA'
    server = '10.60.2.110\DENERGIA'
    database = 'FGV_ENERGIA_SILVER'
    username = 'FGV_ENERGIA_SILVER'
    password = passwd_2
    mascara = '^2...Carga.txt$'
    cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 18 for SQL Server};SERVER=' + server + ',4513;DATABASE=' + database + ';ENCRYPT=NO;TrustServerCertificate=yes;UID=' + username + ';PWD=' + password)
    cursor = cnxn.cursor()

    # read path and mask of file
    path = directory_raw
    dir_list = os.listdir(path)
    # print the list
    list_arq = list()
    for pos, i in enumerate(dir_list):
        if re.search(mascara, i):
            list_arq.append(i)

    for para_arq in list_arq:
        with open(path+para_arq, mode='r', encoding='utf8') as arq:
            leitor = csv.reader(arq, delimiter=';')
            linha = 0
            for pos, coluna in enumerate(leitor):
                if linha == 0:
                    print(f'Colunas: {" ".join(coluna)}')
                    print(f'{len(coluna)}')
                    linha += 1
                else:
                    count = cursor.execute(
                        f"""INSERT INTO [antaq].[CARGA] ([IDCarga],[IDAtracacao],[Origem],[Destino],[CDMercadoria],[TipoOperaçãodaCarga],[CargaGeralAcondicionamento],[ConteinerEstado],[TipoNavegação],[FlagAutorizacao],[FlagCabotagem],[FlagCabotagemMovimentacao],[FlagConteinerTamanho],[FlagLongoCurso],[FlagMCOperacaoCarga],[FlagOffshore],[FlagTransporteViaInterioir],[PercursoTransporteemviasInteriores],[PercursoTransporteInteriores],[STNaturezaCarga],[STSH2],[STSH4],[NaturezadaCarga],[Sentido],[TEU],[QTCarga],[VLPesoCargaBruta],[ANO]) VALUES({coluna[0]},
                    {coluna[1]},
                    \'{coluna[2]}\',
                    \'{coluna[3]}\',
                    \'{coluna[4]}\',
                    \'{coluna[5]}\',
                    \'{coluna[6]}\',
                    \'{coluna[7]}\',
                    \'{coluna[8]}\',
                    \'{coluna[9]}\',
                    {formatnull(coluna[10])},
                    {formatnull(coluna[11])},
                    \'{coluna[12]}\',
                    \'{coluna[13]}\',
                    {formatnull(coluna[14])},
                    {formatnull(coluna[15])},
                    {formatnull(coluna[16])},
                    \'{coluna[17]}\',
                    \'{coluna[18]}\',
                    \'{coluna[19]}\',
                    \'{coluna[20]}\',
                    \'{coluna[21]}\',
                    \'{coluna[22]}\',
                    \'{coluna[23]}\',
                    {formatar(coluna[24])},
                    {formatar(coluna[25])},
                    {formatar(coluna[26])},
                    \'{"01-01-2022"}\')""").rowcount
                    cnxn.commit()
                    linha += 1

        print('Rows inserted: ' + str(count))
        print(f'Imput {linha} no banco')

carga = PythonOperator(
    task_id='read_csv_and_insert_carga',
    python_callable=read_csv_and_insert_carga,
    provide_context=True,
    dag=dag
)


def read_csv_and_insert_carga_hidrovia(**kwargs):
    passwd_2 = Variable.get("passwd_2")
    # Connect to the SQL Server
    #server = 'SQLDC1VDH0003\DENERGIA'
    server = '10.60.2.110\DENERGIA'
    database = 'FGV_ENERGIA_SILVER'
    username = 'FGV_ENERGIA_SILVER'
    password = passwd_2
    mascara = '^2...Carga_Hidrovia.txt$'
    cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 18 for SQL Server};SERVER=' + server + ',4513;DATABASE=' + database + ';ENCRYPT=NO;TrustServerCertificate=yes;UID=' + username + ';PWD=' + password)
    cursor = cnxn.cursor()

    # read path and mask of file
    path = directory_raw
    dir_list = os.listdir(path)
    # print the list
    list_arq = list()
    for pos, i in enumerate(dir_list):
        if re.search(mascara, i):
            list_arq.append(i)

    for para_arq in list_arq:
        with open(path+para_arq, mode='r', encoding='utf8') as arq:
            leitor = csv.reader(arq, delimiter=';')
            linha = 0
            for pos, coluna in enumerate(leitor):
                if linha == 0:
                    print(f'Colunas: {" ".join(coluna)}')
                    print(f'{len(coluna)}')
                    linha += 1
                else:
                    count = cursor.execute(
                        f"""INSERT INTO [antaq].[Carga_Hidrovia] ([IDCarga],[Hidrovia],[ValorMovimentado],[ANO])  values({coluna[0]},
                    \'{coluna[1]}\',
                    {formatar(coluna[2])},
                    \'{'01-01-2022'}\')""").rowcount
                    cnxn.commit()
                    linha += 1

        print('Rows inserted: ' + str(linha))
        print(f'Imput {linha} no banco')


carga_hidrovia = PythonOperator(
    task_id='read_csv_and_insert_carga_hidrovia',
    python_callable=read_csv_and_insert_carga_hidrovia,
    provide_context=True,
    dag=dag
)


def read_csv_and_insert_carga_regiao(**kwargs):
    passwd_2 = Variable.get("passwd_2")
    # Connect to the SQL Server
    #server = 'SQLDC1VDH0003\DENERGIA'
    server = '10.60.2.110\DENERGIA'
    database = 'FGV_ENERGIA_SILVER'
    username = 'FGV_ENERGIA_SILVER'
    password = passwd_2
    mascara = '^2...Carga_Regiao.txt$'
    cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 18 for SQL Server};SERVER=' + server + ',4513;DATABASE=' + database + ';ENCRYPT=NO;TrustServerCertificate=yes;UID=' + username + ';PWD=' + password)
    cursor = cnxn.cursor()

    # read path and mask of file
    path = directory_raw
    dir_list = os.listdir(path)
    # print the list
    list_arq = list()
    for pos, i in enumerate(dir_list):
        if re.search(mascara, i):
            list_arq.append(i)

    for para_arq in list_arq:
        with open(path+para_arq, mode='r', encoding='utf8') as arq:
            leitor = csv.reader(arq, delimiter=';')
            linha = 0
            for pos, coluna in enumerate(leitor):
                if linha == 0:
                    print(f'Colunas: {" ".join(coluna)}')
                    print(f'{len(coluna)}')
                    linha += 1
                else:
                    count = cursor.execute(
                        f"""INSERT INTO [antaq].[carga_regiao]([idcarga],[regiaohidrografica],[valormovimentado],[ano]) values({coluna[0]},
                    \'{coluna[1]}\',
                    {formatar(coluna[2])},
                    \'{'01-01-2022'}\')""").rowcount
                    cnxn.commit()
                    linha += 1

        print('Rows inserted: ' + str(linha))
        print(f'Imput {linha} no banco')


carga_regiao = PythonOperator(
    task_id='read_csv_and_insert_carga_regiao',
    python_callable=read_csv_and_insert_carga_regiao,
    provide_context=True,
    dag=dag
)


def read_csv_and_insert_carga_rio(**kwargs):
    passwd_2 = Variable.get("passwd_2")
    # Connect to the SQL Server
    #server = 'SQLDC1VDH0003\DENERGIA'
    server = '10.60.2.110\DENERGIA'
    database = 'FGV_ENERGIA_SILVER'
    username = 'FGV_ENERGIA_SILVER'
    password = passwd_2
    mascara = '^2...Carga_Rio.txt$'
    cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 18 for SQL Server};SERVER=' + server + ',4513;DATABASE=' + database + ';ENCRYPT=NO;TrustServerCertificate=yes;UID=' + username + ';PWD=' + password)
    cursor = cnxn.cursor()

    # read path and mask of file
    path = directory_raw
    dir_list = os.listdir(path)
    # print the list
    list_arq = list()
    for pos, i in enumerate(dir_list):
        if re.search(mascara, i):
            list_arq.append(i)

    for para_arq in list_arq:
        with open(path+para_arq, mode='r', encoding='utf8') as arq:
            leitor = csv.reader(arq, delimiter=';')
            linha = 0
            for pos, coluna in enumerate(leitor):
                if linha == 0:
                    print(f'Colunas: {" ".join(coluna)}')
                    print(f'{len(coluna)}')
                    linha += 1
                else:
                    count = cursor.execute(
                        f"""INSERT INTO [antaq].[Carga_Rio] ([IDCarga],[Rio],[ValorMovimentado],[ANO]) values({coluna[0]},
                    \'{coluna[1]}\',
                    {formatar(coluna[2])},
                    \'{'01-01-2022'}\')""").rowcount
                    cnxn.commit()
                    linha += 1

        print('Rows inserted: ' + str(linha))
        print(f'Imput {linha} no banco')


carga_rio = PythonOperator(
    task_id='read_csv_and_insert_carga_rio',
    python_callable=read_csv_and_insert_carga_rio,
    provide_context=True,
    dag=dag
)


def read_csv_and_insert_carga_conteinerizada(**kwargs):
    passwd_2 = Variable.get("passwd_2")
    # Connect to the SQL Server
    #server = 'SQLDC1VDH0003\DENERGIA'
    server = '10.60.2.110\DENERGIA'
    database = 'FGV_ENERGIA_SILVER'
    username = 'FGV_ENERGIA_SILVER'
    password = passwd_2
    mascara = '^2...Carga_Conteinerizada.txt$'
    cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 18 for SQL Server};SERVER=' + server + ',4513;DATABASE=' + database + ';ENCRYPT=NO;TrustServerCertificate=yes;UID=' + username + ';PWD=' + password)
    cursor = cnxn.cursor()

    # read path and mask of file
    path = directory_raw
    dir_list = os.listdir(path)
    # print the list
    list_arq = list()
    for pos, i in enumerate(dir_list):
        if re.search(mascara, i):
            list_arq.append(i)

    for para_arq in list_arq:
        with open(path+para_arq, mode='r',
                  encoding='utf8') as arq:
            leitor = csv.reader(arq, delimiter=';')
            linha = 0
            for pos, coluna in enumerate(leitor):
                if linha == 0:
                    print(f'Colunas: {" ".join(coluna)}')
                    print(f'{len(coluna)}')
                    linha += 1
                else:
                    count = cursor.execute(
                        f"""INSERT INTO [antaq].[CARGA_CONTEINERIZADA] ([IDCarga],[CDMercadoriaConteinerizada],[VLPesoCargaConteinerizada],[ANO])  values({coluna[0]},
                    \'{coluna[1]}\',
                    {formatar(coluna[2])},
                    \'{'01-01-2022'}\')""").rowcount
                    cnxn.commit()
                    linha += 1

        print('Rows inserted: ' + str(count))
        print(f'Imput {linha} no banco')


carga_conteinerizada = PythonOperator(
    task_id='read_csv_and_insert_carga_conteinerizada',
    python_callable=read_csv_and_insert_carga_conteinerizada,
    provide_context=True,
    dag=dag
)


def read_csv_and_insert_taxa_ocupacao(**kwargs):
    passwd_2 = Variable.get("passwd_2")
    # Connect to the SQL Server
    #server = 'SQLDC1VDH0003\DENERGIA'
    server = '10.60.2.110\DENERGIA'
    database = 'FGV_ENERGIA_SILVER'
    username = 'FGV_ENERGIA_SILVER'
    password = passwd_2
    mascara = '^2...TaxaOcupacao.txt$'
    cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 18 for SQL Server};SERVER=' + server + ',4513;DATABASE=' + database + ';ENCRYPT=NO;TrustServerCertificate=yes;UID=' + username + ';PWD=' + password)
    cursor = cnxn.cursor()

    # read path and mask of file
    path = directory_raw
    dir_list = os.listdir(path)
    # print the list
    list_arq = list()
    for pos, i in enumerate(dir_list):
        if re.search(mascara, i):
            list_arq.append(i)

    for para_arq in list_arq:
        with open(path+para_arq, mode='r', encoding='utf8') as arq:
            leitor = csv.reader(arq, delimiter=';')
            linha = 0
            for pos, coluna in enumerate(leitor):
                if linha == 0:
                    print(f'Colunas: {" ".join(coluna)}')
                    print(f'{len(coluna)}')
                    linha += 1
                else:
                    count = cursor.execute(
                        f"""INSERT INTO [antaq].[taxa_ocupacao]([idberco],[diataxaocupacao],[mestaxaocupacao],[anotaxaocupacao],[tempoemminutosdias],[ano]) values(\'{coluna[0]}\',
                    \'{coluna[1]}\',
                    \'{coluna[2]}\',
                    \'{coluna[3]}\',
                    {formatnull(coluna[4])},
                    \'{'01-01-2022'}\')""").rowcount
                    cnxn.commit()
                    linha += 1

        print('Rows inserted: ' + str(linha))
        print(f'Imput {linha} no banco')


taxa_ocupacao = PythonOperator(
    task_id='read_csv_and_insert_taxa_ocupacao',
    python_callable=read_csv_and_insert_taxa_ocupacao,
    provide_context=True,
    dag=dag
)


def read_csv_and_insert_tempos_atracacao(**kwargs):
    passwd_2 = Variable.get("passwd_2")
    # Connect to the SQL Server
    #server = 'SQLDC1VDH0003\DENERGIA'
    server = '10.60.2.110\DENERGIA'
    database = 'FGV_ENERGIA_SILVER'
    username = 'FGV_ENERGIA_SILVER'
    password = passwd_2
    mascara = '^2...TemposAtracacao.txt$'
    cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 18 for SQL Server};SERVER=' + server + ',4513;DATABASE=' + database + ';ENCRYPT=NO;TrustServerCertificate=yes;UID=' + username + ';PWD=' + password)
    cursor = cnxn.cursor()

    # read path and mask of file
    path = directory_raw
    dir_list = os.listdir(path)
    # print the list
    list_arq = list()
    for pos, i in enumerate(dir_list):
        if re.search(mascara, i):
            list_arq.append(i)

    for para_arq in list_arq:
        with open(path+para_arq, mode='r', encoding='utf8') as arq:
            leitor = csv.reader(arq, delimiter=';')
            linha = 0
            for pos, coluna in enumerate(leitor):
                if linha == 0:
                    print(f'Colunas: {" ".join(coluna)}')
                    print(f'{len(coluna)}')
                    linha += 1
                else:
                    count = cursor.execute(
                        f"""INSERT INTO [antaq].[TemposAtracacao] ([IDAtracacao] ,[TEsperaAtracacao] ,[TEsperaInicioOp],[TOperacao],[TEsperaDesatracacao],[TAtracado],[TEstadia],[ANO]) values({coluna[0]},
                    {formatar(coluna[1])},
                    {formatar(coluna[2])},
                    {formatar(coluna[3])},
                    {formatar(coluna[4])},
                    {formatar(coluna[5])},
                    {formatar(coluna[6])},
                    \'{'01-01-2022'}\')""").rowcount
                    cnxn.commit()
                    linha += 1

        print('Rows inserted: ' + str(linha))
        print(f'Imput {linha} no banco')


tempos_atracacao = PythonOperator(
    task_id='read_csv_and_insert_tempos_atracacao',
    python_callable=read_csv_and_insert_tempos_atracacao,
    provide_context=True,
    dag=dag
)

end_task = DummyOperator(task_id='end_task', dag=dag)



start_task >> atracacao >> end_task
start_task >> acordosbilaterais >> end_task
start_task >> carga >> end_task
start_task >> carga_hidrovia >> end_task
start_task >> carga_regiao >> end_task
start_task >> carga_rio >> end_task
start_task >> carga_conteinerizada >> end_task
start_task >> taxa_ocupacao >> end_task
start_task >> tempos_atracacao >> end_task
