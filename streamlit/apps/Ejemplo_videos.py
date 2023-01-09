import streamlit as st

def app():
    st.title('Ejemplo en vídeos')
    video_file = open('./VIDEOS_RESULTADO/result_IMG_9553_Trim.mp4', 'rb')
    video_bytes = video_file.read()

    st.video(video_bytes)


    video_file = open('./VIDEOS_RESULTADO/result_IMG_9556_Trim_2.mp4', 'rb')
    video_bytes = video_file.read()

    st.video(video_bytes)

    video_file = open('./VIDEOS_RESULTADO/result_IMG_9556_Trim.mp4', 'rb')
    video_bytes = video_file.read()

    st.video(video_bytes)

    video_file = open('./VIDEOS_RESULTADO/result_traffic-sign-to-test_Trim.mp4', 'rb')
    video_bytes = video_file.read()

    st.video(video_bytes)

        
