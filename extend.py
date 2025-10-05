# =======================================================
# Sorting Visualizer with Percentage Labels on Each Bar
# =======================================================
# Author: Puku
# Description:
#   A sorting algorithm visualizer built using Tkinter.
#   Visualizes Bubble Sort, Selection Sort, and Insertion Sort.
#   Each bar shows its relative height percentage on top.
# =======================================================

import tkinter as tk
import random
import time


class SortingVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Sorting Visualizer with Percentages")
        self.root.geometry("850x500")
        self.root.config(bg="white")

        # Canvas to draw bars
        self.canvas = tk.Canvas(root, width=800, height=400, bg="white")
        self.canvas.pack(pady=20)

        # Generate random data
        self.data = [random.randint(10, 390) for _ in range(25)]
        self.draw_bars(self.data)

        # Buttons for controls
        frame = tk.Frame(root, bg="white")
        frame.pack(pady=10)

        tk.Button(frame, text="Bubble Sort", command=self.bubble_sort,
                  bg="#0078D7", fg="white", font=("Arial", 10, "bold"), width=12).pack(side="left", padx=5)

        tk.Button(frame, text="Selection Sort", command=self.selection_sort,
                  bg="#FF9800", fg="white", font=("Arial", 10, "bold"), width=12).pack(side="left", padx=5)

        tk.Button(frame, text="Insertion Sort", command=self.insertion_sort,
                  bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), width=12).pack(side="left", padx=5)

        tk.Button(frame, text="Shuffle", command=self.shuffle_data,
                  bg="#9C27B0", fg="white", font=("Arial", 10, "bold"), width=12).pack(side="left", padx=5)

        self.status_label = tk.Label(root, text="Status: Ready", font=("Arial", 12, "bold"), bg="white")
        self.status_label.pack(pady=5)

    # ---------------- Helper: Draw Bars ----------------
    def draw_bars(self, data, color="skyblue"):
        self.canvas.delete("all")
        c_width = 800
        c_height = 400
        x_width = c_width / len(data)
        max_value = max(data)

        for i, val in enumerate(data):
            x0 = i * x_width
            y0 = c_height - val
            x1 = (i + 1) * x_width
            y1 = c_height

            # Draw bar
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="black")

            # Compute height percentage
            percent = int((val / max_value) * 100)

            # Draw percentage above the bar
            self.canvas.create_text(
                (x0 + x1) / 2, y0 - 10,
                text=f"{percent}%",
                fill="black",
                font=("Arial", 10, "bold")
            )

        self.root.update_idletasks()

    # ---------------- Shuffle Data ----------------
    def shuffle_data(self):
        random.shuffle(self.data)
        self.draw_bars(self.data)
        self.status_label.config(text="Status: Shuffled")

    # ---------------- Bubble Sort ----------------
    def bubble_sort(self):
        data = self.data
        n = len(data)
        total_steps = n * (n - 1) / 2
        current_step = 0
        self.status_label.config(text="Status: Bubble Sorting...")

        for i in range(n):
            for j in range(0, n - i - 1):
                current_step += 1
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
                self.draw_bars(data, "tomato")
                time.sleep(0.05)
        self.draw_bars(data, "lightgreen")
        self.status_label.config(text="Status: Bubble Sort Completed ✅")

    # ---------------- Selection Sort ----------------
    def selection_sort(self):
        data = self.data
        n = len(data)
        self.status_label.config(text="Status: Selection Sorting...")

        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if data[j] < data[min_idx]:
                    min_idx = j
                self.draw_bars(data, "plum")
                time.sleep(0.05)
            data[i], data[min_idx] = data[min_idx], data[i]
        self.draw_bars(data, "lightgreen")
        self.status_label.config(text="Status: Selection Sort Completed ✅")

    # ---------------- Insertion Sort ----------------
    def insertion_sort(self):
        data = self.data
        n = len(data)
        self.status_label.config(text="Status: Insertion Sorting...")

        for i in range(1, n):
            key = data[i]
            j = i - 1
            while j >= 0 and data[j] > key:
                data[j + 1] = data[j]
                j -= 1
                self.draw_bars(data, "gold")
                time.sleep(0.05)
            data[j + 1] = key
        self.draw_bars(data, "lightgreen")
        self.status_label.config(text="Status: Insertion Sort Completed ✅")


# ---------------- Run GUI ----------------
if __name__ == "__main__":
    root = tk.Tk()
    app = SortingVisualizer(root)
    root.mainloop()
