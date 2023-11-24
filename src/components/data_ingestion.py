import os 
import sys 
from src.exception import CustomException
from src.logger import logging
import pandas as pd


# training  and test spliting 
from sklearn.model_selection import train_test_split
from dataclasses import dataclass



# inputs where to save train , test data 
# input for data_ingestion component 
@dataclass #directly define class variable
class DataIngestionConfig:

    # here the trained data will be stored at specified file location 
    train_data_path: str=os.path.join("artifact","train.csv")

# for saving test data 
    test_data_path: str=os.path.join("artifact","test.csv")

# for saving raw data 
    raw_data_path: str=os.path.join("artifact","raw.csv")
    

class DataIngestion:
    def __init__(self):

        self.ingestion_config = DataIngestionConfig()

    #  to read from database

    def start_data_ingestion(self):
        logging.info("Entered the data ingestion method")

        try:
# reading the data             
            df = pd.read_csv("notebook\data.csv")
            logging.info("Succesfully read data as DF")

# creating a dir for train data if already exist dont make new 
            
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index= False,header=True)

            logging.info("Train Test initiated")
# training and testing data
            train_set , test_set = train_test_split(df,test_size=0.2,random_state=45)

# saving train data to artifact train data 

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header = True)

# saving test data to test_data_path in artifact
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header = True)

            logging.info("Ingestion Done")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            ) 

        except Exception as e:

            raise CustomException(e,sys)

if __name__ == "__main__":
    obj = DataIngestion()
    obj.start_data_ingestion()