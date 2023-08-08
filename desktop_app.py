import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Load the trained model
model = load_model('pet_expressions_model_DenseNet50.h5')
emotion_classes = ['angry', 'happy', 'sad', 'some typa way']

def preprocess_image(image_path):
    img = image.load_img(image_path, target_size=(224, 224))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img /= 255.0
    return img

def classify_emotion():
    file_path = filedialog.askopenfilename()
    if file_path:
        img = preprocess_image(file_path)
        result = model.predict(img)
        predicted_class = emotion_classes[np.argmax(result)]
        show_results_screen(file_path, predicted_class)

def show_results_screen(image_path, emotion):
    results_window = tk.Toplevel()
    results_window.title("Results")

    img = Image.open(image_path)
    img.thumbnail((400, 400))  # Resize image for display
    img = ImageTk.PhotoImage(img)

    image_label = tk.Label(results_window, image=img)
    image_label.image = img
    image_label.pack(pady=10)

    emotion_label = tk.Label(results_window, text=f"Predicted Emotion: {emotion}", font=("Helvetica", 14, "bold"))
    emotion_label.pack()

app = tk.Tk()
app.title("Pet Emotion Predictor")

# Color palette
bg_color = "#F4F4F4"

# Configure color scheme
app.configure(bg=bg_color)
frame = tk.Frame(app, borderwidth=5, relief=tk.SUNKEN, bg=bg_color)  # Inverted border style
frame.pack(padx=40, pady=40)  # Increase padding for a larger starting screen

title_label = tk.Label(frame, text="Pet Emotion Predictor", font=("Helvetica", 20, "bold"), bg=bg_color)
title_label.pack(pady=20)

browse_button = tk.Button(frame, text="Browse Image", command=classify_emotion, bg="red", fg='white', font=("Helvetica", 14))
browse_button.pack()

app.mainloop()






