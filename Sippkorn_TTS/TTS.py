import pygame
from gtts import gTTS
import time

# ฟังก์ชันสร้างไฟล์เสียง
def tts(text):
    tts = gTTS(text=text, lang='th') # เปลี่ยนภาษาไทย th เป็นอังกฤษ๋ en ได้
    filename = "tts_test.mp3" 
    tts.save(filename) # บันทึกแล้วได้ไฟล์ .mp3 สามารถใช้ได้เลย
    print(f"บันทึกไฟล์เสียง: {text}")
    return filename

# ฟังก์ชันเล่นไฟล์เสียง
def speak(file):
    print(f"กำลังเล่นไฟล์เสียง: {file}")
    #ส่วนของการเล่นโหลดไฟล์เสียง
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    
    # รอจนกว่าเสียงจะเล่นจบ
    while pygame.mixer.music.get_busy():
        time.sleep(0.01) 
    pygame.mixer.music.unload()
        
# ============================ การใช้งาน ==================================

# ขั้นตอนที่ 1 สร้างเสียงและเก็บชื่อไฟล์
voice = tts("การทดสอบเปลี่ยนข้อความเป็นเสียง")

# ขั้นตอนที่ 2ใส่ให้โปรแกรมเล่นเสียง
speak(voice)
 
