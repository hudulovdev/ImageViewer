import tkinter as tk
from PIL import ImageTk, Image
import os

class ImageViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Viewer")

        self.image_label = tk.Label(self.root)
        self.image_label.pack()

        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=10)

        self.prev_button = tk.Button(self.button_frame, text="Previous", command=self.show_prev_image)
        self.prev_button.grid(row=0, column=0, padx=10)

        self.next_button = tk.Button(self.button_frame, text="Next", command=self.show_next_image)
        self.next_button.grid(row=0, column=1, padx=10)

        self.image_files = self.load_image_files()
        self.current_image_index = 0
        self.show_current_image()

    def load_image_files(self):
        image_files = []
        for file in os.listdir("."):  # Assuming images are in the current directory
            if file.lower().endswith((".jpg", ".jpeg", ".png", ".gif")):
                image_files.append(file)
        return image_files

    def show_current_image(self):
        image_path = self.image_files[self.current_image_index]
        image = Image.open(image_path)
        image = image.resize((400, 400))  # Adjust the size as needed
        photo = ImageTk.PhotoImage(image)
        self.image_label.config(image=photo)
        self.image_label.image = photo

    def show_prev_image(self):
        self.current_image_index -= 1
        if self.current_image_index < 0:
            self.current_image_index = len(self.image_files) - 1
        self.show_current_image()

    def show_next_image(self):
        self.current_image_index += 1
        if self.current_image_index >= len(self.image_files):
            self.current_image_index = 0
        self.show_current_image()

if __name__ == '__main__':
    root = tk.Tk()
    image_viewer = ImageViewer(root)
    root.mainloop()
