from dotenv import load_dotenv
load_dotenv()
import os
import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
import google.generativeai as genai
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

prompt = """
            You are Youtobe video summarizer.
            You will be taking the transcript text and summarizing the entair video and 
            providing the important summary in points within 250 words.
            Please provide the summary of the text given here
            """
            
def generate_gemini_content(transcript_text, prompt):
    model=genai.GenerativeModel("gemini-pro")
    response=model.generate_content(prompt+transcript_text)
    return response.text

def extact_transcript_details(youtube_video_url):
    try:
        video_id=youtube_video_url.split("=")[1]
        transcript_text=YouTubeTranscriptApi.get_transcript(video_id)
        transcript = " "
        for i in transcript_text:
            transcript += "" + i["text"]
        return transcript
    
    except Exception as e:
        raise e
    
        
    

st.title("YouTube Transcript to Detailed Notes Conveter")

youtube_video_url=st.text_input("Enter the Youtube link")
if youtube_video_url:
    video_id=youtube_video_url.split("=")[1]
    st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg",use_column_width=True)
    
if st.button("Get Detailed Notes"):
    transcript_text=extact_transcript_details(youtube_video_url)
    
    if transcript_text:
        summary=generate_gemini_content(transcript_text,prompt)
        st.markdown("Detailed Notes")
        st.write(summary)
