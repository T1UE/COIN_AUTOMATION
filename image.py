from PIL import Image, ImageTk
import tkinter as tk

image = Image.open("homepage.png")

root = tk.Tk()
root.title("Coordinate Finder")

photo = ImageTk.PhotoImage(image)

canvas = tk.Canvas(
    root,
    width=image.width,
    height=image.height,
    scrollregion=(0, 0, image.width, image.height)
)

canvas.pack()

canvas.create_image(0, 0, anchor="nw", image=photo)

def mouse_move(event):
    x = int(canvas.canvasx(event.x))
    y = int(canvas.canvasy(event.y))
    root.title(f"X: {x}   Y: {y}")

canvas.bind("<Motion>", mouse_move)

root.mainloop()

# from PIL import Image

# img = Image.open("homepage.png")
# print("Screenshot size:", img.size)