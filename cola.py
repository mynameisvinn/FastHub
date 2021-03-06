"""Download handler for CoLA dataset"""
from hub import transform
from hub.schema import Primitive, Text


import zipfile
from tqdm import tqdm
import requests
import pandas as pd
import numpy as np



from Fast import Dataset
    

class Retrieve(Dataset):
    def __init__(self, url: str, tag: str, schema: dict):
        self.temp = "temp"
        self.url = url
        self.tag = tag
        self.schema = schema
    
    
    def fetch(self):
        r = requests.get(self.url)  
        with open(self.temp, 'wb') as f:
            f.write(r.content)
    

    def unpack(self):
        with zipfile.ZipFile(self.temp, 'r') as z:
            z.extractall()

        
    def push(self):
        # read data into memory
        df = pd.read_csv(
                "./cola_public/raw/in_domain_train.tsv",
                sep="\t",
                header=None,
                usecols=[1, 3],
                names=["label", "sentence"],
            )
            
        sentences = list(df.sentence.values)
        labels = list(df.label.values)
        data = list(zip(sentences, labels))
        
        @transform(schema=self.schema)
        def load_transform(sample):
            return {
                "sentence": sample[0],
                "labels": sample[1]
            }

        ds = load_transform(data)
        return ds.store(self.tag)



def main(url, tag, schema):
    R = Retrieve(url, tag, schema)
    R.fetch()
    R.unpack()
    ds = R.push()
    if ds:
        return True
