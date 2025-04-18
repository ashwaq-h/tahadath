import streamlit as st
import os

# عنوان الصفحة
st.title("مترجم النص إلى لغة الإشارة")

# إدخال النص
text = st.text_input("اكتب الكلمة:")

# عند الضغط على زر الترجمة
if st.button("ترجم"):
    if text:
        video_path = f"videos/{text}.mp4"
        if os.path.exists(video_path):
            st.success(f"ترجمة الكلمة: {text}")
            st.video(video_path)
        else:
            st.error("لم يتم العثور على فيديو لهذه الكلمة.")
    else:
        st.warning("يرجى إدخال كلمة أولاً.")