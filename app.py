from cola import main as cola_main
from dota import main as dota_main

import streamlit as st
from hub import transform
from hub.schema import Primitive, Text

import uuid
import zipfile
from tqdm import tqdm
import requests
import pandas as pd
import numpy as np

st.title("FastHub")

selected_datasets = st.multiselect("Select a dataset ", ['CoLA', 'Dota'])
selected_tag = st.multiselect("Tag: ", ['mynameisvinn', 'activeloop'])



res = None

if selected_datasets:
    dataset = selected_datasets[0]
    random = uuid.uuid1()
    tag = f"mynameisvinn/{dataset}-{random}"

    if selected_datasets[0] == 'CoLA':
        url = 'https://nyu-mll.github.io/CoLA/cola_public_1.1.zip'
        schema = {
            'sentence': Text(shape=(None, ), max_shape=(500, )),
            'labels': Primitive(dtype="int64")
        }

        res = cola_main(url, tag, schema)
    
    if selected_datasets[0] == 'Dota':
        url = 'https://drive.google.com/uc?id=1fwiTNqRRen09E-O9VSpcMV2e6_d4GGVK'
        schema = {
            'sentence': Text(shape=(None, ), max_shape=(500, )),
            'labels': Primitive(dtype="int64")
        }
        res = dota_main(url)


if selected_datasets:
    st.write("Code snippet! ")

    body = f"""
        import hub            
        
        ds = hub.load('{tag}')
        ds['sentence'].compute()  # fetch all sentences
        ds['labels'].compute()  # fetch all labels
        """.format(tag)
    
    st.code(body, language='python')

    st.write("Dockerfile")
    body = f"""
        pip install hub            
        CMD = ['python', 'fetch.py', '-user mynameisvinn']
        """.format(tag)
    st.code(body, language='bash')