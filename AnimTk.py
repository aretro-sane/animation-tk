import tkinter as tk

import numpy as np
import seaborn as sns
from matplotlib.figure import Figure
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

sns.set_theme(palette="viridis")

rng = np.random.default_rng()

fig = Figure(figsize=(20, 20), dpi=100)
ax = fig.add_subplot(111, xlim=(-11, 11), ylim=(-1, 21))
ax.set_title("Plot Positions")
ax.set_xlabel("X-Axis")
ax.set_ylabel("Y-Axis")
obj, = ax.plot([], [], 'o', lw=3)

def init():
    obj.set_data([], [])
    return obj,

def animate(i):
    n_obj = rng.integers(21)
    x = rng.uniform(-10, 10, n_obj)
    y = rng.uniform(0, 20, n_obj)
    obj.set_data(x, y)
    return obj,

class AnimTkApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Animation with Tkinter")
        self.geometry("1000x1000")
        
        canvas = FigureCanvasTkAgg(fig, self)
        canvas.draw()
        toolbar = NavigationToolbar2Tk(canvas, self, pack_toolbar=False)
        toolbar.update()
        
        toolbar.pack(side=tk.BOTTOM, fill=tk.X)
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

if __name__ == "__main__":
    app = AnimTkApp()
    anim = FuncAnimation(fig, animate, init_func=init, interval=2000, blit=True)
    app.mainloop()
