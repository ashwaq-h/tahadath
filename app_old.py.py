
import streamlit as st
import speech_recognition as sr
import os

# عنوان الصفحة
st.title("Speech to Sign Language Translator")

# زر التسجيل
if st.button("اضغط وتكلم"):
    st.write("استمع الآن... تكلّم")

    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio, language="ar-SA")
            st.success(f"الكلمة التي قلتها: {text}")

            video_path = f"videos/{text}.mp4"
            if os.path.exists(video_path):
                st.video(video_path)
            else:
                st.error("لم يتم العثور على فيديو لهذه الكلمة.")
        
        except sr.UnknownValueError:
            st.error("لم يتم التعرف على الكلام. حاول مرة أخرى.")
        except sr.RequestError:
            st.error("حدثت مشكلة في الاتصال بخدمة التعرف على الصوت. تأكد من اتصال الإنترنت.")
    
    except Exception as e:
        st.error(f"حدث خطأ أثناء محاولة الوصول للمايكروفون: {e}")