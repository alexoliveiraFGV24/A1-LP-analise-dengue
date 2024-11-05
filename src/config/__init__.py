"""Módulo contendo funções e variáveis importantes de configuração"""
import os


def DATASET_LOCAL() -> str:
    """Retorna o caminho absoluto da pasta 'Data'

    Returns:
        str: Caminho dos datasets
    """
    return os.path.join(os.getcwd(), 'data')


def DATASETS() -> list[str]:
    """Função que lista todos os datasets na pasta data

    Returns:
        list[str]: Lista de arquivos
    """
    return os.listdir(DATASET_LOCAL())


def FILES_FOLDER() -> str:
    """Função que retorna o caminho da pasta 'File'

    Returns:
        str: Caminho da pasta 'Files'
    """
    return os.path.join(os.getcwd(), 'files')


def OUTPUT_FOLDER() -> str:
    """Função que retorna o caminho para a pasta 'Output'

    Returns:
        str: Caminho da pasta 'Output'
    """
    return os.path.join(os.getcwd(), 'output')


REQUIRED_COLUMNS = [  # As colunas requeridas para todas as funções do código
    'DT_INVEST', 'FEBRE', 'DOR_RETRO', 'LEUCOPENIA', 'PETEQUIA_N', 'DT_VIRAL', 
    'RESUL_NS1', 'ACIDO_PEPT', 'DT_PCR', 'AUTO_IMUNE', 'CEFALEIA', 'ARTRITE', 
    'DT_ENCERRA', 'DT_SIN_PRI', 'MIALGIA', 'CONJUNTVIT', 'DT_NS1', 'DIABETES', 
    'DT_SORO', 'RESUL_PCR_', 'DT_CHIK_S1', 'DT_INTERNA', 'HEPATOPAT', 'EXANTEMA', 
    'SG_UF_NOT', 'ARTRALGIA', 'CLASSI_FIN', 'RENAL', 'HOSPITALIZ', 'VOMITO', 
    'RESUL_VI_N', 'DT_NOTIFIC', 'DT_OBITO', 'DT_DIGITA', 'DOR_COSTAS', 'LACO', 
    'DT_CHIK_S2', 'NAUSEA', 'HIPERTENSA', 'DT_ALRM', 'DT_GRAV', 'DT_PRNT', 
    'EVOLUCAO', 'HEMATOLOG', 'RESUL_SORO', 'SIGLA_UF', 'SG_UF_NOT', 'ID_OCUPA_N', 'SOROTIPO',
    'HISTOPA_N', 'IMUNOH_N',
]

CHUNKS_SIZE = 5 * 10**4  # Chunks usados quando ler todo o dataset

MAX_SET_SIZE = 3  # Tamanho máximo de síntomas a considerar
