# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import Label, Toplevel

class AssistantWindow:
    def __init__(self, left_team, right_team, left_team_positions, right_team_positions, starting_team):
        self.window = Toplevel()
        self.window.title("Помощник судьи")

        # Верхний левый виджет
        self.top_left_frame = tk.Frame(self.window)
        self.top_left_frame.grid(row=0, column=0, padx=10, pady=10)
        Label(self.top_left_frame, text="Оповещение игроков и действия").pack()

        # Верхний правый виджет
        self.top_right_frame = tk.Frame(self.window)
        self.top_right_frame.grid(row=0, column=1, padx=10, pady=10)
        Label(self.top_right_frame, text="Таймер матча, счет и замены").pack()

        # Нижний левый виджет
        self.bottom_left_frame = tk.Frame(self.window)
        self.bottom_left_frame.grid(row=1, column=0, padx=10, pady=10)
        Label(self.bottom_left_frame, text="Статусы действий команды хозяев").pack()

        # Нижний правый виджет
        self.bottom_right_frame = tk.Frame(self.window)
        self.bottom_right_frame.grid(row=1, column=1, padx=10, pady=10)
        Label(self.bottom_right_frame, text="Статусы действий команды гостей").pack()

        self.window.mainloop()

