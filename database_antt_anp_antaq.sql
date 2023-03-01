	/****** object:  schema [anp]    script date: 23/02/2023 15:03:59 ******/
create schema [anp]
go
/****** object:  schema [antaq]    script date: 23/02/2023 15:03:59 ******/
create schema [antaq]
go
/****** object:  schema [antq]    script date: 23/02/2023 15:03:59 ******/
create schema [antq]
go
/****** object:  schema [antt]    script date: 23/02/2023 15:03:59 ******/
create schema [antt]
go
/****** object:  table [anp].[liquidos_entregas_distribuidor_atual]    script date: 23/02/2023 15:03:59 ******/
set ansi_nulls on
go
set quoted_identifier on
go
create table [anp].[liquidos_entregas_distribuidor_atual](
	[id] [int] identity(1,1) not null,
	[ano] [int] null,
	[mes] [int] null,
	[distribuidor] [varchar](100) null,
	[codproduto] [varchar](100) null,
	[nomeproduto] [varchar](100) null,
	[regiao] [varchar](100) null,
	[qtdproduto] [float] null,
primary key clustered
(
	[id] asc
)with (pad_index = off, statistics_norecompute = off, ignore_dup_key = off, allow_row_locks = on, allow_page_locks = on) on [primary]
) on [primary]
go
/****** object:  table [anp].[liquidos_entregas_fornecedor_atual]    script date: 23/02/2023 15:03:59 ******/
set ansi_nulls on
go
set quoted_identifier on
go
create table [anp].[liquidos_entregas_fornecedor_atual](
	[id] [int] identity(1,1) not null,
	[ano] [int] null,
	[mes] [int] null,
	[fornecedor] [varchar](100) null,
	[codproduto] [varchar](100) null,
	[nomeproduto] [varchar](100) null,
	[regiao] [varchar](100) null,
	[qtdproduto] [float] null,
primary key clustered
(
	[id] asc
)with (pad_index = off, statistics_norecompute = off, ignore_dup_key = off, allow_row_locks = on, allow_page_locks = on) on [primary]
) on [primary]
go
/****** object:  table [anp].[liquidos_entregas_historico]    script date: 23/02/2023 15:03:59 ******/
set ansi_nulls on
go
set quoted_identifier on
go
create table [anp].[liquidos_entregas_historico](
	[id] [int] identity(1,1) not null,
	[ano] [int] null,
	[mes] [int] null,
	[fornecedor] [varchar](150) null,
	[distribuidor] [varchar](150) null,
	[codproduto] [varchar](150) null,
	[nomeproduto] [varchar](150) null,
	[regiaoorigem] [varchar](150) null,
	[uforigem] [varchar](150) null,
	[localidadedestino] [varchar](150) null,
	[regiaodestinatario] [varchar](150) null,
	[ufdestino] [varchar](150) null,
	[qtdproduto] [float] null,
primary key clustered
(
	[id] asc
)with (pad_index = off, statistics_norecompute = off, ignore_dup_key = off, allow_row_locks = on, allow_page_locks = on) on [primary]
) on [primary]
go
/****** object:  table [anp].[liquidos_vendas_atual]    script date: 23/02/2023 15:03:59 ******/
set ansi_nulls on
go
set quoted_identifier on
go
create table [anp].[liquidos_vendas_atual](
	[id] [int] identity(1,1) not null,
	[ano] [int] null,
	[mes] [int] null,
	[agenteregulado] [varchar](150) null,
	[codproduto] [varchar](150) null,
	[nomeproduto] [varchar](150) null,
	[regiaoorigem] [varchar](150) null,
	[regiaodestinatario] [varchar](150) null,
	[mercadodestinatario] [varchar](150) null,
	[qtdproduto] [float] null,
primary key clustered
(
	[id] asc
)with (pad_index = off, statistics_norecompute = off, ignore_dup_key = off, allow_row_locks = on, allow_page_locks = on) on [primary]
) on [primary]
go
/****** object:  table [anp].[liquidos_vendas_historico]    script date: 23/02/2023 15:03:59 ******/
set ansi_nulls on
go
set quoted_identifier on
go
create table [anp].[liquidos_vendas_historico](
	[ano] [bigint] null,
	[mes] [bigint] null,
	[agenteregulado] [varchar](max) null,
	[codproduto] [bigint] null,
	[nomeproduto] [varchar](max) null,
	[regiaoorigem] [varchar](max) null,
	[uforigem] [varchar](max) null,
	[regiaodestinatario] [varchar](max) null,
	[ufdestino] [varchar](max) null,
	[mercadodestinatario] [varchar](max) null,
	[qtdproduto] [float] null
) on [primary] textimage_on [primary]
go
/****** object:  table [anp].[liquidos_vendas_hitorico]    script date: 23/02/2023 15:03:59 ******/
set ansi_nulls on
go
set quoted_identifier on
go
create table [anp].[liquidos_vendas_hitorico](
	[id] [int] identity(1,1) not null,
	[ano] [int] null,
	[mes] [int] null,
	[agenteregulado] [varchar](150) null,
	[codproduto] [varchar](150) null,
	[nomeproduto] [varchar](150) null,
	[regiaoorigem] [varchar](150) null,
	[uforigem] [varchar](150) null,
	[regiaodestinatario] [varchar](150) null,
	[ufdestino] [varchar](150) null,
	[mercadodestinatario] [varchar](150) null,
	[qtdproduto] [float] null,
primary key clustered
(
	[id] asc
)with (pad_index = off, statistics_norecompute = off, ignore_dup_key = off, allow_row_locks = on, allow_page_locks = on) on [primary]
) on [primary]
go
/****** object:  table [anp].[liquidos_vendas_uf_atual]    script date: 23/02/2023 15:03:59 ******/
set ansi_nulls on
go
set quoted_identifier on
go
create table [anp].[liquidos_vendas_uf_atual](
	[id] [int] identity(1,1) not null,
	[ano] [bigint] null,
	[mes] [bigint] null,
	[codproduto] [bigint] null,
	[nomeproduto] [varchar](150) null,
	[ufdeorigem] [varchar](150) null,
	[regiaoorigem] [varchar](150) null,
	[ufdedestino] [varchar](150) null,
	[regiaodestinatario] [varchar](150) null,
	[mercadodestinatario] [varchar](150) null,
	[qtdproduto] [float] null,
primary key clustered
(
	[id] asc
)with (pad_index = off, statistics_norecompute = off, ignore_dup_key = off, allow_row_locks = on, allow_page_locks = on) on [primary]
) on [primary]
go
/****** object:  table [antaq].[acordosbilaterais]    script date: 23/02/2023 15:03:59 ******/
set ansi_nulls on
go
set quoted_identifier on
go
create table [antaq].[acordos_bilaterais](
	[id] [int] identity(1,1) not null,
	[nacionalidadeembarcacao] [varchar](100) null,
	[anoacordobilateral] [varchar](100) null,
	[totalacordobilateral] [int] null,
	[acordotiponavegacao] [varchar](100) null,
	[pais] [varchar](100) null,
	[flagembarquedesembarque] [int] null,
	[ano] [date] null,
primary key clustered
(
	[id] asc
)with (pad_index = off, statistics_norecompute = off, ignore_dup_key = off, allow_row_locks = on, allow_page_locks = on) on [primary]
) on [primary]
go
/****** object:  table [antaq].[atracacao]    script date: 23/02/2023 15:03:59 ******/
set ansi_nulls on
go
set quoted_identifier on
go
create table [antaq].[atracacao](
	[id] [int] identity(1,1) not null,
	[idatracacao] [bigint] null,
	[cdtup] [varchar](100) null,
	[idberco] [varchar](100) null,
	[berco] [varchar](100) null,
	[portoatracação] [varchar](100) null,
	[apelidoinstalaçãoportuaria] [varchar](100) null,
	[complexoportuario] [varchar](100) null,
	[tipodaautoridadeportuária] [varchar](100) null,
	[dataatracacao] [datetime] null,
	[datachegada] [datetime] null,
	[datadesatracacao] [datetime] null,
	[datainiciooperacao] [datetime] null,
	[dataterminooperacao] [datetime] null,
	[ano] [varchar](10) null,
	[mes] [varchar](100) null,
	[tipodeoperacao] [varchar](100) null,
	[tipodenavegacaodaatracacao] [varchar](100) null,
	[nacionalidadedoarmador] [bigint] null,
	[flagmcoperacaoatracacao] [bigint] null,
	[terminal] [varchar](100) null,
	[município] [varchar](100) null,
	[uf] [varchar](30) null,
	[sguf] [varchar](10) null,
	[regiãogeografica] [varchar](30) null,
	[ndacapitania] [varchar](100) null,
	[ndoimo] [bigint] null,

primary key clustered
(
	[id] asc
)with (pad_index = off, statistics_norecompute = off, ignore_dup_key = off, allow_row_locks = on, allow_page_locks = on) on [primary]
) on [primary]
go
/****** object:  table [antaq].[carga]    script date: 23/02/2023 15:03:59 ******/
set ansi_nulls on
go
set quoted_identifier on
go
create table [antaq].[carga](
	[id] [int] identity(1,1) not null,
	[idcarga] [int] null,
	[idatracacao] [int] null,
	[origem] [varchar](100) null,
	[destino] [varchar](100) null,
	[cdmercadoria] [varchar](100) null,
	[tipooperaçãodacarga] [varchar](100) null,
	[cargageralacondicionamento] [varchar](100) null,
	[conteinerestado] [varchar](100) null,
	[tiponavegação] [varchar](100) null,
	[flagautorizacao] [varchar](2) null,
	[flagcabotagem] [int] null,
	[flagcabotagemmovimentacao] [int] null,
	[flagconteinertamanho] [varchar](100) null,
	[flaglongocurso] [int] null,
	[flagmcoperacaocarga] [int] null,
	[flagoffshore] [int] null,
	[flagtransporteviainterioir] [int] null,
	[percursotransporteemviasinteriores] [varchar](100) null,
	[percursotransporteinteriores] [varchar](100) null,
	[stnaturezacarga] [varchar](100) null,
	[stsh2] [varchar](100) null,
	[stsh4] [varchar](100) null,
	[naturezadacarga] [varchar](100) null,
	[sentido] [varchar](100) null,
	[teu] [int] null,
	[qtcarga] [int] null,
	[vlpesocargabruta] [float] null,
	[ano] [date] null,
primary key clustered
(
	[id] asc
)with (pad_index = off, statistics_norecompute = off, ignore_dup_key = off, allow_row_locks = on, allow_page_locks = on) on [primary]
) on [primary]
go
/****** object:  table [antaq].[carga_conteinerizada]    script date: 23/02/2023 15:03:59 ******/
set ansi_nulls on
go
set quoted_identifier on
go
create table [antaq].[carga_conteinerizada](
	[id] [int] identity(1,1) not null,
	[idcarga] [int] null,
	[cdmercadoriaconteinerizada] [varchar](100) null,
	[vlpesocargaconteinerizada] [float] null,
	[ano] [date] null,
primary key clustered
(
	[id] asc
)with (pad_index = off, statistics_norecompute = off, ignore_dup_key = off, allow_row_locks = on, allow_page_locks = on) on [primary]
) on [primary]
go
/****** object:  table [antaq].[carga_hidrovia]    script date: 23/02/2023 15:03:59 ******/
set ansi_nulls on
go
set quoted_identifier on
go
create table [antaq].[carga_hidrovia](
	[id] [int] identity(1,1) not null,
	[idcarga] [int] null,
	[hidrovia] [varchar](30) null,
	[valormovimentado] [int] null,
	[ano] [date] null,
primary key clustered
(
	[id] asc
)with (pad_index = off, statistics_norecompute = off, ignore_dup_key = off, allow_row_locks = on, allow_page_locks = on) on [primary]
) on [primary]
go
/****** object:  table [antaq].[carga_regiao]    script date: 23/02/2023 15:03:59 ******/
set ansi_nulls on
go
set quoted_identifier on
go
create table [antaq].[carga_regiao](
	[id] [int] identity(1,1) not null,
	[idcarga] [int] null,
	[regiaohidrografica] [varchar](100) null,
	[valormovimentado] [int] null,
	[ano] [date] null,
primary key clustered
(
	[id] asc
)with (pad_index = off, statistics_norecompute = off, ignore_dup_key = off, allow_row_locks = on, allow_page_locks = on) on [primary]
) on [primary]
go
/****** object:  table [antaq].[carga_rio]    script date: 23/02/2023 15:03:59 ******/
set ansi_nulls on
go
set quoted_identifier on
go
create table [antaq].[carga_rio](
	[id] [int] identity(1,1) not null,
	[idcarga] [int] null,
	[rio] [varchar](100) null,
	[valormovimentado] [int] null,
	[ano] [date] null,
primary key clustered
(
	[id] asc
)with (pad_index = off, statistics_norecompute = off, ignore_dup_key = off, allow_row_locks = on, allow_page_locks = on) on [primary]
) on [primary]
go
/****** object:  table [antaq].[legendas]    script date: 23/02/2023 15:03:59 ******/
set ansi_nulls on
go
set quoted_identifier on
go
create table [antaq].[legendas](
	[id] [int] identity(1,1) not null,
	[cdtup] [varchar](100) null,
	[nomedestino] [varchar](100) null,
	[cdbigramadestino] [varchar](100) null,
	[cdtrigramadestino] [varchar](100) null,
	[cdtupdestino] [varchar](100) null,
	[riodestino] [varchar](100) null,
	[regiaohidrograficadestino] [varchar](100) null,
	[ufdestino] [varchar](100) null,
	[cidadedestino] [varchar](100) null,
	[paisdestino] [varchar](100) null,
	[continentedestino] [varchar](100) null,
	[blocoeconomicodestino] [varchar](100) null,
primary key clustered
(
	[id] asc
)with (pad_index = off, statistics_norecompute = off, ignore_dup_key = off, allow_row_locks = on, allow_page_locks = on) on [primary]
) on [primary]
go
/****** object:  table [antaq].[taxaocupacao]    script date: 23/02/2023 15:03:59 ******/
set ansi_nulls on
go
set quoted_identifier on
go
create table [antaq].[taxa_ocupacao](
	[id] [int] identity(1,1) not null,
	[idberco] [varchar](30) null,
	[diataxaocupacao] [varchar](30) null,
	[mestaxaocupacao] [varchar](30) null,
	[anotaxaocupacao] [varchar](30) null,
	[tempoemminutosdias] [int] null,
	[ano] [date] null,
primary key clustered
(
	[id] asc
)with (pad_index = off, statistics_norecompute = off, ignore_dup_key = off, allow_row_locks = on, allow_page_locks = on) on [primary]
) on [primary]
go
/****** object:  table [antaq].[temposatracacao]    script date: 23/02/2023 15:03:59 ******/
set ansi_nulls on
go
set quoted_identifier on
go
create table [antaq].[temposatracacao](
	[id] [int] identity(1,1) not null,
	[idatracacao] [numeric](20, 0) null,
	[tesperaatracacao] [numeric](20, 0) null,
	[tesperainicioop] [numeric](20, 0) null,
	[toperacao] [numeric](20, 0) null,
	[tesperadesatracacao] [numeric](20, 0) null,
	[tatracado] [numeric](20, 0) null,
	[testadia] [numeric](20, 0) null,
	[ano] [date] null,
primary key clustered
(
	[id] asc
)with (pad_index = off, statistics_norecompute = off, ignore_dup_key = off, allow_row_locks = on, allow_page_locks = on) on [primary]
) on [primary]
go
/****** object:  table [antt].[producao_origem_destino]    script date: 23/02/2023 15:03:59 ******/
set ansi_nulls on
go
set quoted_identifier on
go
create table [antt].[producao_origem_destino](
	[id] [int] identity(1,1) not null,
	[mesano] [date] null,
	[ferrovia] [varchar](100) null,
	[mercadoriaantt] [varchar](100) null,
	[estacaoorigem] [varchar](100) null,
	[uforigem] [varchar](100) null,
	[estacaodestino] [varchar](100) null,
	[ufdestino] [varchar](100) null,
	[tu] [numeric](30, 0) null,
	[tku] [numeric](30, 0) null,
primary key clustered
(
	[id] asc
)with (pad_index = off, statistics_norecompute = off, ignore_dup_key = off, allow_row_locks = on, allow_page_locks = on) on [primary]
) on [primary]
go
