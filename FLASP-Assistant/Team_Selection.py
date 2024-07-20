# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import Label, Button, OptionMenu, StringVar

class TeamSelectionWindow:
    def __init__(self, left_team, right_team):
        self.window = tk.Toplevel()
        self.window.title("Выбор составов")

        self.display_team(left_team, side="left")
        self.display_team(right_team, side="right")

        Button(self.window, text="Начать матч").pack()

        self.window.mainloop()

    def display_team(self, team, side):
        frame = tk.Frame(self.window)
        frame.pack(side=side, fill="both", expand=True)

        Label(frame, text=team.name).pack()

        positions = ["ФРВ", "ЦАП", "ЦОП", "ЦЗ", "ВРТ"]
        for position in positions:
            row = tk.Frame(frame)
            row.pack(fill="x", expand=True)

            Label(row, text=position).pack(side="left")

            player_var = StringVar()
            player_var.set("Выберите игрока")  # default value
            OptionMenu(row, player_var, *[player.name for player in team.players]).pack(side="right")
