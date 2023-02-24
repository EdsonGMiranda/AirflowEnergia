/****** Object:  Schema [anp]    Script Date: 23/02/2023 15:03:59 ******/
CREATE SCHEMA [anp]
GO
/****** Object:  Schema [antaq]    Script Date: 23/02/2023 15:03:59 ******/
CREATE SCHEMA [antaq]
GO
/****** Object:  Schema [antq]    Script Date: 23/02/2023 15:03:59 ******/
CREATE SCHEMA [antq]
GO
/****** Object:  Schema [antt]    Script Date: 23/02/2023 15:03:59 ******/
CREATE SCHEMA [antt]
GO
/****** Object:  Table [anp].[liquidos_entregas_distribuidor_atual]    Script Date: 23/02/2023 15:03:59 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [anp].[liquidos_entregas_distribuidor_atual](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[ano] [int] NULL,
	[mes] [int] NULL,
	[distribuidor] [varchar](100) NULL,
	[codproduto] [varchar](100) NULL,
	[nomeproduto] [varchar](100) NULL,
	[regiao] [varchar](100) NULL,
	[qtdproduto] [float] NULL,
PRIMARY KEY CLUSTERED
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [anp].[liquidos_entregas_fornecedor_atual]    Script Date: 23/02/2023 15:03:59 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [anp].[liquidos_entregas_fornecedor_atual](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[ano] [int] NULL,
	[mes] [int] NULL,
	[fornecedor] [varchar](100) NULL,
	[codproduto] [varchar](100) NULL,
	[nomeproduto] [varchar](100) NULL,
	[regiao] [varchar](100) NULL,
	[qtdproduto] [float] NULL,
PRIMARY KEY CLUSTERED
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [anp].[liquidos_entregas_historico]    Script Date: 23/02/2023 15:03:59 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [anp].[liquidos_entregas_historico](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[ano] [int] NULL,
	[mes] [int] NULL,
	[fornecedor] [varchar](150) NULL,
	[distribuidor] [varchar](150) NULL,
	[codproduto] [varchar](150) NULL,
	[nomeproduto] [varchar](150) NULL,
	[regiaoorigem] [varchar](150) NULL,
	[uforigem] [varchar](150) NULL,
	[localidadedestino] [varchar](150) NULL,
	[regiaodestinatario] [varchar](150) NULL,
	[ufdestino] [varchar](150) NULL,
	[qtdproduto] [float] NULL,
PRIMARY KEY CLUSTERED
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [anp].[liquidos_vendas_atual]    Script Date: 23/02/2023 15:03:59 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [anp].[liquidos_vendas_atual](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[ano] [int] NULL,
	[mes] [int] NULL,
	[agenteregulado] [varchar](150) NULL,
	[codproduto] [varchar](150) NULL,
	[nomeproduto] [varchar](150) NULL,
	[regiaoorigem] [varchar](150) NULL,
	[regiaodestinatario] [varchar](150) NULL,
	[mercadodestinatario] [varchar](150) NULL,
	[qtdproduto] [float] NULL,
PRIMARY KEY CLUSTERED
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [anp].[liquidos_vendas_historico]    Script Date: 23/02/2023 15:03:59 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [anp].[liquidos_vendas_historico](
	[ano] [bigint] NULL,
	[mes] [bigint] NULL,
	[agenteregulado] [varchar](max) NULL,
	[codproduto] [bigint] NULL,
	[nomeproduto] [varchar](max) NULL,
	[regiaoorigem] [varchar](max) NULL,
	[uforigem] [varchar](max) NULL,
	[regiaodestinatario] [varchar](max) NULL,
	[ufdestino] [varchar](max) NULL,
	[mercadodestinatario] [varchar](max) NULL,
	[qtdproduto] [float] NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [anp].[liquidos_vendas_hitorico]    Script Date: 23/02/2023 15:03:59 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [anp].[liquidos_vendas_hitorico](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[ano] [int] NULL,
	[mes] [int] NULL,
	[agenteregulado] [varchar](150) NULL,
	[codproduto] [varchar](150) NULL,
	[nomeproduto] [varchar](150) NULL,
	[regiaoorigem] [varchar](150) NULL,
	[uforigem] [varchar](150) NULL,
	[regiaodestinatario] [varchar](150) NULL,
	[ufdestino] [varchar](150) NULL,
	[mercadodestinatario] [varchar](150) NULL,
	[qtdproduto] [float] NULL,
PRIMARY KEY CLUSTERED
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [anp].[liquidos_vendas_uf_atual]    Script Date: 23/02/2023 15:03:59 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [anp].[liquidos_vendas_uf_atual](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[ano] [bigint] NULL,
	[mes] [bigint] NULL,
	[codproduto] [bigint] NULL,
	[nomeproduto] [varchar](150) NULL,
	[ufdeorigem] [varchar](150) NULL,
	[regiaoorigem] [varchar](150) NULL,
	[ufdedestino] [varchar](150) NULL,
	[regiaodestinatario] [varchar](150) NULL,
	[mercadodestinatario] [varchar](150) NULL,
	[qtdproduto] [float] NULL,
PRIMARY KEY CLUSTERED
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [antaq].[AcordosBilaterais]    Script Date: 23/02/2023 15:03:59 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [antaq].[acordosbilaterais](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[nacionalidadeembarcacao] [varchar](100) NULL,
	[AnoAcordoBilateral] [varchar](100) NULL,
	[TotalAcordoBilateral] [int] NULL,
	[AcordoTipoNavegacao] [varchar](100) NULL,
	[País] [varchar](100) NULL,
	[FlagEmbarqueDesembarque] [int] NULL,
	[ANO] [date] NULL,
PRIMARY KEY CLUSTERED
(
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [antaq].[Atracacao]    Script Date: 23/02/2023 15:03:59 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [antaq].[Atracacao](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[IDAtracacao] [bigint] NULL,
	[CDTUP] [varchar](100) NULL,
	[IDBerco] [varchar](100) NULL,
	[Berco] [varchar](100) NULL,
	[PortoAtracação] [varchar](100) NULL,
	[ApelidoInstalaçãoPortuaria] [varchar](100) NULL,
	[ComplexoPortuario] [varchar](100) NULL,
	[TipodaAutoridadePortuária] [varchar](100) NULL,
	[DataAtracacao] [datetime] NULL,
	[DataChegada] [datetime] NULL,
	[DataDesatracacao] [datetime] NULL,
	[DataInicioOperacao] [datetime] NULL,
	[DataTerminoOperacao] [datetime] NULL,
	[Ano] [varchar](10) NULL,
	[Mes] [varchar](100) NULL,
	[TipodeOperacao] [varchar](100) NULL,
	[TipodeNavegacaodaAtracacao] [varchar](100) NULL,
	[NacionalidadedoArmador] [bigint] NULL,
	[FlagMCOperacaoAtracacao] [bigint] NULL,
	[Terminal] [varchar](100) NULL,
	[Município] [varchar](100) NULL,
	[UF] [varchar](30) NULL,
	[SGUF] [varchar](10) NULL,
	[RegiãoGeografica] [varchar](30) NULL,
	[NdaCapitania] [varchar](100) NULL,
	[NdoIMO] [bigint] NULL,
PRIMARY KEY CLUSTERED
(
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [antaq].[CARGA]    Script Date: 23/02/2023 15:03:59 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [antaq].[CARGA](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[IDCarga] [int] NULL,
	[IDAtracacao] [int] NULL,
	[Origem] [varchar](100) NULL,
	[Destino] [varchar](100) NULL,
	[CDMercadoria] [varchar](100) NULL,
	[TipoOperaçãodaCarga] [varchar](100) NULL,
	[CargaGeralAcondicionamento] [varchar](100) NULL,
	[ConteinerEstado] [varchar](100) NULL,
	[TipoNavegação] [varchar](100) NULL,
	[FlagAutorizacao] [varchar](2) NULL,
	[FlagCabotagem] [int] NULL,
	[FlagCabotagemMovimentacao] [int] NULL,
	[FlagConteinerTamanho] [varchar](100) NULL,
	[FlagLongoCurso] [int] NULL,
	[FlagMCOperacaoCarga] [int] NULL,
	[FlagOffshore] [int] NULL,
	[FlagTransporteViaInterioir] [int] NULL,
	[PercursoTransporteemviasInteriores] [varchar](100) NULL,
	[PercursoTransporteInteriores] [varchar](100) NULL,
	[STNaturezaCarga] [varchar](100) NULL,
	[STSH2] [varchar](100) NULL,
	[STSH4] [varchar](100) NULL,
	[NaturezadaCarga] [varchar](100) NULL,
	[Sentido] [varchar](100) NULL,
	[TEU] [int] NULL,
	[QTCarga] [int] NULL,
	[VLPesoCargaBruta] [float] NULL,
	[ANO] [date] NULL,
PRIMARY KEY CLUSTERED
(
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [antaq].[CARGA_CONTEINERIZADA]    Script Date: 23/02/2023 15:03:59 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [antaq].[CARGA_CONTEINERIZADA](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[IDCarga] [int] NULL,
	[CDMercadoriaConteinerizada] [varchar](100) NULL,
	[VLPesoCargaConteinerizada] [float] NULL,
	[ANO] [date] NULL,
PRIMARY KEY CLUSTERED
(
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [antaq].[Carga_Hidrovia]    Script Date: 23/02/2023 15:03:59 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [antaq].[Carga_Hidrovia](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[IDCarga] [int] NULL,
	[Hidrovia] [varchar](30) NULL,
	[ValorMovimentado] [int] NULL,
	[ANO] [date] NULL,
PRIMARY KEY CLUSTERED
(
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [antaq].[Carga_Regiao]    Script Date: 23/02/2023 15:03:59 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [antaq].[Carga_Regiao](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[IDCarga] [int] NULL,
	[RegiãoHidrográfica] [varchar](100) NULL,
	[ValorMovimentado] [int] NULL,
	[ANO] [date] NULL,
PRIMARY KEY CLUSTERED
(
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [antaq].[Carga_Rio]    Script Date: 23/02/2023 15:03:59 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [antaq].[Carga_Rio](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[IDCarga] [int] NULL,
	[Rio] [varchar](100) NULL,
	[ValorMovimentado] [int] NULL,
	[ANO] [date] NULL,
PRIMARY KEY CLUSTERED
(
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [antaq].[LEGENDAS]    Script Date: 23/02/2023 15:03:59 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [antaq].[LEGENDAS](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[CDTUP] [varchar](100) NULL,
	[NOMEDESTINO] [varchar](100) NULL,
	[CDBIGRAMADESTINO] [varchar](100) NULL,
	[CDTRIGRAMADESTINO] [varchar](100) NULL,
	[CDTUPDESTINO] [varchar](100) NULL,
	[RIODESTINO] [varchar](100) NULL,
	[REGIÃOHIDROGRÁFICADESTINO] [varchar](100) NULL,
	[UFDESTINO] [varchar](100) NULL,
	[CIDADEDESTINO] [varchar](100) NULL,
	[PAISDESTINO] [varchar](100) NULL,
	[CONTINENTEDESTINO] [varchar](100) NULL,
	[BLOCOECONOMICO_DESTINO] [varchar](100) NULL,
PRIMARY KEY CLUSTERED
(
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [antaq].[TaxaOcupacao]    Script Date: 23/02/2023 15:03:59 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [antaq].[TaxaOcupacao](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[IDBerco] [varchar](30) NULL,
	[DiaTaxaOcupacao] [varchar](30) NULL,
	[MêsTaxaOcupacao] [varchar](30) NULL,
	[AnoTaxaOcupacao] [varchar](30) NULL,
	[TempoEmMinutosdias] [int] NULL,
	[ANO] [date] NULL,
PRIMARY KEY CLUSTERED
(
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [antaq].[TemposAtracacao]    Script Date: 23/02/2023 15:03:59 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [antaq].[TemposAtracacao](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[IDAtracacao] [numeric](20, 0) NULL,
	[TEsperaAtracacao] [numeric](20, 0) NULL,
	[TEsperaInicioOp] [numeric](20, 0) NULL,
	[TOperacao] [numeric](20, 0) NULL,
	[TEsperaDesatracacao] [numeric](20, 0) NULL,
	[TAtracado] [numeric](20, 0) NULL,
	[TEstadia] [numeric](20, 0) NULL,
	[ANO] [date] NULL,
PRIMARY KEY CLUSTERED
(
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [antt].[producao_origem_destino]    Script Date: 23/02/2023 15:03:59 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [antt].[producao_origem_destino](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[mes_ano] [date] NULL,
	[ferrovia] [varchar](100) NULL,
	[mercadoria_antt] [varchar](100) NULL,
	[estacao_origem] [varchar](100) NULL,
	[uf_origem] [varchar](100) NULL,
	[estacao_destino] [varchar](100) NULL,
	[uf_destino] [varchar](100) NULL,
	[tu] [numeric](30, 0) NULL,
	[tku] [numeric](30, 0) NULL,
PRIMARY KEY CLUSTERED
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
