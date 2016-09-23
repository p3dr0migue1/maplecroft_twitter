import os


class Config:
    DEBUG = False
    TESTING = False
    BASE_DIR = os.getcwd()
    STATIC_DIR = os.path.join(BASE_DIR, 'static')
    GEO_DATA_FILE = os.path.join(STATIC_DIR, 'js/geo_data.json')
    COUNTRIES_COORDINATES = os.path.join(BASE_DIR, 'countries_coordinates.csv')
    CONSUMER_KEY = '8GVD3x56AxU7GBpSfYVIeVcBi'
    CONSUMER_SECRET = 'qUTOEmLt9Y7bmMBWRjhRelLU60EF8TTeJPkDLfWaaOaTWA7XoE'
    ACCESS_TOKEN = '778311435143278592-ZjJgETFDHlcW64j4o6hpjAhgq5duPqm'
    ACCESS_SECRET = 'Su4CXcAORbkDLzMTaokM1qLkC67xm4kxV8gcAtZ8OLygG'


class DevelopmentConfig(Config):
    DEBUG = True
    ACCOUNT_NAME = 'pedrocurado85'


class ProductionConfig(Config):
    DEBUG = True
    ACCOUNT_NAME = 'MaplecroftRisk'


config = {
    'default': DevelopmentConfig,
    'production': ProductionConfig
}
