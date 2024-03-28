from abc import ABCMeta, abstractclassmethod
import pandas as pd
import numpy as np
from typing import Union
import os
import requests
from bs4 import BeautifulSoup
import pickle
import pymongo

"""
Extraction, Transformation, Load
주기적으로 내부 및 외부 데이터베이스로부터 정보를 추출하고 
정해진 규약에 따라 정보를 변환한 후 DW에 정보를 적재하는 프로세스
"""


class Extraction(metaclass=ABCMeta):
    @abstractclassmethod
    def __init__(self) -> None:
        pass

    @abstractclassmethod
    def get_data(self, data: Union[dict, pd.DataFrame, str]) -> None:
        pass

    @abstractclassmethod
    def statistics(self) -> pd.DataFrame:
        pass


class Extract_europe(Extraction):
    def __init__(self, url):
        self.path = './europe_extraction'
        self.url = url

    def get_data(self):
        os.system(f"wget -P {self.path} {self.url}")

    def statistics(self):
        """
        데이터 통계
        """
        return


class Extract_asia(Extraction):
    def __init__(self, url):
        self.path = './asia_extraction'
        self.file = 'asia_original_collection.pickle'
        self.url = url

    def get_data(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            data = response.json()
            with open(f'{self.path}/{self.file}', 'wb') as fw:
                pickle.dump(data, fw)
        else:
            print('Error:', response.status_code)

    def statistics(self):
        """
        데이터 통계
        """
        return


class Extract_usa(Extraction):
    def __init__(self, url):
        self.path = './usa_extraction'
        self.data = pd.DataFrame()
        self.url = url

    def get_data(self):
        response = requests.get(self.url)
        html_data = response.text
        soup = BeautifulSoup(html_data, 'html.parser')

    def statistics(self):
        """
        데이터 통계
        """
        return


class Transformation(metaclass=ABCMeta):
    @abstractclassmethod
    def __init__(self) -> None:
        pass

    @abstractclassmethod
    def pre_statistics(self):
        """
        transformation 이전의 통계 값
        """
        pass

    @abstractclassmethod
    def filtering(self):
        """
        데이터 클렌징
        """
        pass

    @abstractclassmethod
    def transform(self):
        """
        데이터 형식 변환 
        """
        pass

    @abstractclassmethod
    def standardization(self):
        """
        데이터 표준화
        """
        pass

    @abstractclassmethod
    def post_statistics(self):
        """
        데이터 transformation 이후 통계 값
        """
        pass

    @abstractclassmethod
    def save(self):
        pass


class Transform_europe(Transformation):
    def __init__(self):
        pass

    def pre_statistics(self):
        pass

    def filtering(self):
        pass

    def transform(self):
        pass

    def standardization(self):
        pass

    def post_statistics(self):
        pass

    def save(self):
        pass


class Transform_asia(Transformation):
    def __init__(self):
        pass

    def pre_statistics(self):
        pass

    def filtering(self):
        pass

    def transform(self):
        pass

    def standardization(self):
        pass

    def post_statistics(self):
        pass

    def save(self):
        pass


class Transform_usa(Transformation):
    def __init__(self):
        pass

    def pre_statistics(self):
        pass

    def filtering(self):
        pass

    def transform(self):
        pass

    def standardization(self):
        pass

    def post_statistics(self):
        pass

    def save(self):
        pass


class Load_data:
    def __init__(self, data) -> None:
        self.data = data
        self._MONGO_URI = os.environ.get('MONGO_URI')
        self._MONGO_DB = os.environ.get('MONGO_DB')

    def load(self):
        client = pymongo.MongoClient(self._MONGO_URI)
        db = client[self._MONGO_DB]
        collection = db.mycollection
        result = collection.insert_one(self.data)


class Etl:
    def __init__(self) -> None:
        self.europe_extraction = Extract_europe('url1')
        self.asia_extraction = Extract_asia('url2')
        self.usa_extraction = Extract_usa('url3')
        self.europe_transformation = Transform_europe()
        self.asia_transformation = Transform_asia()
        self.usa_transformation = Transform_usa()

    def extraction(self):
        for continent in (
                self.europe_extraction, self.asia_extraction, self.usa_extraction):
            continent.get_data()
            continent.statistics()

    def transformation(self):
        for continent in (self.europe_transformation, self.asia_transformation,
                          self.usa_transformation):
            continent.pre_statistics()
            continent.filtering()
            continent.transform()
            continent.standardization()
            continent.post_statistics()
            continent.save()

    def load(self):
        data_load = Load_data()
        data_load.load()


if __name__ == '__main__':
    etl = Etl()
    etl.extraction()
    etl.transformation()
    etl.load()
