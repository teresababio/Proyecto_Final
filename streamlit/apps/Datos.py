import streamlit as st
import pandas as pd
from auxiliar.sennal import classes, lst_count


def app():
    st.title('Datos')
    st.markdown("""El conjunto de señales a estudiar ha sido obtenido de la base de datos 
    [Kaggle](https://www.kaggle.com/datasets/meowmeowmeowmeowmeow/gtsrb-german-traffic-sign),
    que contiene 43 tipos de señales de tráfico distintas alemanas. A continuación, se podrán ver cada una de las
    señales de estudio""")

    
    df = pd.DataFrame(columns = ["label", "name"])
    df["name"] = classes.values()
    df["label"] = classes.keys()
    df["value_counts"] = lst_count
    df = df.set_index("label")
    st.table(df)
    st.markdown("""
    Como el número de fotos por cada label no es similar, 
    se procedió a aplicar Data Augmentation al conjunto de entrenamiento.""")

    code = """           p = Augmentor.Pipeline(os.path.join(cur_path,'Train',str(label)))
            p.rotate(probability=0.7, max_left_rotation=10, max_right_rotation=10)
            p.zoom(probability=0.5, min_factor=1.1, max_factor=1.4)
            p.skew(probability=0.6)
            p.sample(limit - value)  """
    
    st.code(code, language="python")



