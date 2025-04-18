import pygame
import time

# تهيئة pygame لتشغيل الفيديو
pygame.init()
screen = pygame.display.set_mode((640, 480))

# دالة لتشغيل فيديو بلغة الإشارة
def play_sign_video(video_path):
    movie = pygame.movie.Movie(video_path)
    movie.set_display(screen)
    movie.play()
    while movie.get_busy():
        pygame.time.Clock().tick(60)

# إدخال نص من المستخدم
text = input("اكتب الكلمة التي تريد ترجمتها إلى لغة الإشارة: ")

# التحقق من الكلمة وتشغيل الفيديو المناسب
if "مرحبا" in text:
    play_sign_video("marhaban.mp4")

elif "شكرا" in text:
    play_sign_video("shukran.mp4")

else:
    print("ما لقيت فيديو مناسب لهالكلمة.")