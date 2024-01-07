from tkinter import *
import random
import time

from objects import Ball, Paddle

tk = Tk()
tk.title("Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

paddle = Paddle(canvas, 'green')
ball = Ball(canvas, paddle, 'red')
wait_flag = True

while True:
	if ball.hit_bottom == False:
		ball.draw()
		paddle.draw()
		tk.update_idletasks()
		tk.update()
	if wait_flag:
		time.sleep(1)
		wait_flag = False
	tk.update_idletasks()
	tk.update()
	time.sleep(0.01)