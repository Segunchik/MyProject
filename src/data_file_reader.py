import csv


import pandas as pd


from pandas import DataFrame

def csv_reader(path_file: str) -> list[dict]|str:
    '''
    Функция принимает на вход путь к файлу в формате csv и возвращает список словарей с его содержимым
    :param path_file: - путь к файлу *.csv
    :return: dict[]
    '''
    try:
#        with open(path_file, 'r', encoding='utf-8') as file:
        df: DataFrame  = pd.read_csv(path_file, delimiter=';')
        return df.to_dict(orient='records')
    except FileNotFoundError as err:
        return str(err)
    except ValueError as err:
        return str(err)


def excel_reader(path_file: str) -> list[dict]|str:
    '''
    Функция принимает на вход путь к файлу в формате EXCEL и возвращает список словарей с его содержимым
    :param path_file: - путь к файлу *.csv
    :return: dict[]
    '''

    try:
        df = pd.read_excel(path_file)
        return df.to_dict('records')
    except FileNotFoundError as err:
        return str(err)
    except ValueError as err:
        return str(err)





