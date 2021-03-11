from cola import main as cola_main
from dota import main as dota_main

import time
from hub import transform
import uuid
import streamlit as st

st.title("FastHub")

datasets = ['CoLA', 'Dota', '1mdb', 'mnist']

selected_datasets = st.multiselect("Select a dataset ", datasets)
selected_tag = st.multiselect("Tag: ", ['mynameisvinn', 'activeloop'])

if selected_datasets and selected_tag:
    dataset = selected_datasets[0]
    handle = selected_tag[0]
    random = uuid.uuid1()
    tag = f"{handle}/{dataset}-{random}"

    if selected_datasets[0] == 'CoLA':

        # url = 'https://nyu-mll.github.io/CoLA/cola_public_1.1.zip'
        # schema = {
            # 'sentence': Text(shape=(None, ), max_shape=(500, )),
            # 'labels': Primitive(dtype="int64")
        # }

        # res = cola_main(url, tag, schema)
        pass
    
    if selected_datasets[0] == 'Dota':
        pass

    else:
        pass



if selected_datasets and selected_tag:

    with st.spinner('Pushing'):
        time.sleep(2)

    st.write("Code snippet ")

    body = f"""
        import hub            
        
        ds = hub.load('{tag}')
        X = ds['sentence'].compute()
        y = ds['labels'].compute()
        """.format(tag)
    
    st.code(body, language='python')

    st.write("Dockerfile")
    body = f"""
        pip install hub            
        CMD = ['python', 'fetch.py', '-user {handle}']  # placeholder
        """.format(handle)
    st.code(body, language='bash')

    st.write("Easy Viz")
    body = f"""
    https://app.activeloop.ai/dataset/{handle}/{dataset}-{random}
    """.format(handle, dataset, random)
    st.code(body, language='bash')
