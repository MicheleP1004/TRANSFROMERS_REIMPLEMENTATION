from datasets import load_dataset
import os

# This script load a dataset from HuggingFace Hub and save it in the DATA directory as csv

DATASET_PATH = "iwslt2017"
DATASET_NAME = "iwslt2017-de-en"

dataset_train = load_dataset(DATASET_PATH,DATASET_NAME,trust_remote_code=True,split="train")
dataset_val = load_dataset(DATASET_PATH,DATASET_NAME,trust_remote_code=True,split="validation")
dataset_test = load_dataset(DATASET_PATH,DATASET_NAME,trust_remote_code=True,split="test")


dataset_train.to_csv(path_or_buf="./DATA/"+DATASET_NAME+"/train_data.csv")
dataset_val.to_csv(path_or_buf="./DATA/"+DATASET_NAME+"/val_data.csv",)
dataset_test.to_csv(path_or_buf="./DATA/"+DATASET_NAME+"/test_data.csv",)