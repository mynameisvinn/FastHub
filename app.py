from cola import main as cola_main
from dota import main as dota_main


from hub import transform
import uuid


st.title("FastHub")

datasets = ['CoLA', 'Dota', '1mdb', 'mnist']

selected_datasets = st.multiselect("Select a dataset ", datasets)
selected_tag = st.multiselect("Tag: ", ['mynameisvinn', 'activeloop'])



res = None

if selected_datasets:
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
        url = 'https://drive.google.com/uc?id=1fwiTNqRRen09E-O9VSpcMV2e6_d4GGVK'
        schema = {
            'sentence': Text(shape=(None, ), max_shape=(500, )),
            'labels': Primitive(dtype="int64")
        }
        res = dota_main(url)

    else:
        pass


if selected_datasets:
    st.write("Code snippet ")

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
        CMD = ['python', 'fetch.py', '-user mynameisvinn']  # placeholder
        """.format(tag)
    st.code(body, language='bash')