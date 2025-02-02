from pydub.utils import mediainfo
import os

file_path = os.path.join("vibes-and-stuff/main_app", "Kendrick_Lamar_United_In_Grief.mp3")

info = mediainfo(file_path)
duration = float(info['duration'])

print(f"Длительность: {duration} секунд")
