from PIL import Image
import pytesseract
from moviepy.editor import VideoFileClip
import numpy as np
import cv2

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Path to the video file
video_path = 'meeting.mp4'

# Function to extract frames from the video and perform OCR
def extract_text_from_video(video_path, start_time, end_time, interval):
    """
    Extracts text from video frames using OCR.
    """
    # Load the video
    video = VideoFileClip(video_path).subclip(start_time, end_time)

    # Initialize variables
    texts = []
    timestamps = []

    # Iterate over frames
    for t in np.arange(start_time, end_time, interval):
        # Get the frame at time t
        frame = video.get_frame(t)
        frame_image = Image.fromarray(frame)

        # Perform OCR on the frame
        text = pytesseract.image_to_string(frame_image)

        # Store the text and timestamp if text is detected
        if text.strip():
            texts.append(text.strip())
            timestamps.append(t)

    return texts, timestamps

# Extract text from the first 3 minutes of the video, checking every 5 seconds
extracted_texts, timestamps = extract_text_from_video(video_path, 360, 370, 5)

# Display the first few extracted texts and their timestamps
extracted_texts[:5], timestamps[:5]
