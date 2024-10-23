import streamlit as st

def main():
    st.title("Audio Replacement in video")
    st.write("Upload a video file to replace its audio with AI-generated voice.")

    video_file = st.file_uploader("Choose a video file...", type=["mp4" , "mov" , "avi"])
    if video_file is not None:
        st.video(video_file)

if __name__ == "__main__":
    main()