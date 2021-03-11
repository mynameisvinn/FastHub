import urllib.request
import tarfile
import hub
from tqdm import tqdm
import argparse
import json
from glob import glob
import gdown

from Fast import Dataset
    

class Retrieve(Dataset):
    def __init__(self):
        self.sink = "sink"
        self.directory = "unzipped"
    
    
    def fetch(self, url):
    	return gdown.download(url, self.directory, quiet=False) 
    

    def unpack(self, tarfile_file_name):
        open_tarfile = tarfile.open(tarfile_file_name)
        open_tarfile.extractall(path=self.directory)
        open_tarfile.close()
        
    
    def push(self, schema: dict, files, url: str):
        self.schema = schema
        
        size = len(files)
        if size == 0:
            raise ValueError("Empty Directory")
        print(">> {size} records".format(size))
        
        ds = hub.Dataset(url, shape=(size,), schema=schema, mode="w")
        
        for i, file in tqdm(enumerate(files)):
            with open(file) as json_file:
                data = json.load(json_file)
                ds['data', i] = data
        ds.commit()


def main(url):
    print(">> downloading")
    R = Retrieve()
    # R.fetch(url)
    return True