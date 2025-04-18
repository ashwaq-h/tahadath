if st.button("ترجم"):
    if text:
        video_path = f"videos/{text}.mp4"
        st.write("يحاول تشغيل الملف:", video_path)  # <-- أضفنا هذا السطر هنا

        if os.path.exists(video_path):
            video_file = open(video_path, 'rb')
            video_bytes = video_file.read()
            st.video(video_bytes)
        else:
            st.error("لم يتم العثور على فيديو لهذه الكلمة.")
    else:
        st.warning("يرجى إدخال كلمة أولاً.")
