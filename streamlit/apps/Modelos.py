import streamlit as st
from keras.models import load_model
import pandas as pd
def app():
    st.title('Modelos empleados')
    st.markdown("""
        Se probaron tres redes neuronales. Dos de ellos consisten en una misma red neuronal construida
         desde cero a diferencia
        que uno emplea el conjunto train aumentado y el otro no
        """)


    code ="""def model_cnn(n_classes):
    model = Sequential()   
    model.add(Conv2D(filters=32, kernel_size=(5,5), activation='relu', input_shape=(IMG_HEIGHT,IMG_WIDTH,channels)))
    model.add(Conv2D(filters=32, kernel_size=(5,5), activation='relu'))
    model.add(MaxPool2D(pool_size=(2, 2)))
    model.add(Dropout(rate=0.25))
    model.add(Conv2D(filters=64, kernel_size=(3,3), activation='relu'))
    model.add(Conv2D(filters=64, kernel_size=(3,3), activation='relu'))
    model.add(MaxPool2D(pool_size=(2, 2)))
    model.add(Dropout(rate=0.25))
    model.add(Flatten())
    model.add(Dense(256, activation='relu'))
    model.add(Dropout(rate=0.5))
    model.add(Dense(128, activation='relu'))
    model.add(Dropout(rate=0.5))
    model.add(Dense(n_classes, activation='softmax'))

    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model """

    st.code(code, language="python")

    st.markdown("""
        El tercer modelo emplea la red neuronal ya pre-entrenada para clasificación de objetos MobileNetV3Small 
        """)
    
    code = """def mobilenet(n_classes):
    print(IMG_HEIGHT,IMG_WIDTH,channels)
    base_model = MobileNetV3Small(weights="imagenet", input_shape=(IMG_HEIGHT,IMG_WIDTH,channels),  include_top=False)

    x= base_model.output
    x= keras.layers.GlobalAveragePooling2D()(x)
    x= keras.layers.Dense(512, activation ='relu')(x)
    x= keras.layers.Dense(256, activation ='relu')(x)
    x= keras.layers.Dense(128, activation ='relu')(x)
    preds = keras.layers.Dense(n_classes, activation ='softmax')(x)

    model = keras.Model(inputs=base_model.input, outputs=preds)

    



    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model """
    
    st.code(code, language="python")

    st.header("Resultados")
    df_result = pd.DataFrame(index=["Train", "Test"], columns = ["CNN", "CNN_AUG", "MOBILENETSMALL"])
    df_result["CNN"] = [98.9, 97.6]
    df_result["CNN_AUG"] = [97.15, 97.38 ]
    df_result["MOBILENETSMALL"] = [97.84, 87.09 ]

    st.table(df_result)
    