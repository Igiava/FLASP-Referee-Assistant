## -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import Label, Button, OptionMenu, StringVar
from Assistant_Window import AssistantWindow

class TeamSelectionWindow:
    def __init__(self, left_team, right_team):
        self.window = tk.Toplevel()
        self.window.title("Выбор составов")

        self.left_team = left_team
        self.right_team = right_team

        self.left_team_positions = {}
        self.right_team_positions = {}

        self.display_team(left_team, side="left", positions_dict=self.left_team_positions)
        self.display_team(right_team, side="right", positions_dict=self.right_team_positions)

        Label(self.window, text="Команда, начинающая матч:").pack()
        self.starting_team_var = StringVar()
        self.starting_team_var.set(left_team.name)  # default value
        OptionMenu(self.window, self.starting_team_var, left_team.name, right_team.name).pack()

        Button(self.window, text="Начать матч", command=self.start_match).pack()

        self.window.mainloop()

    def display_team(self, team, side, positions_dict):
        frame = tk.Frame(self.window)
        frame.pack(side=side, fill="both", expand=True)

        Label(frame, text=team.name).pack()

        positions = ["ФРВ", "ЦАП", "ЦОП", "ЦЗ", "ВРТ"]
        for position in positions:
            row = tk.Frame(frame)
            row.pack(fill="x", expand=True)

            Label(row, text=position).pack(side="left")

            player_var = StringVar()
            player_var.set(team.players[0].name)  # default value
            OptionMenu(row, player_var, *[player.name for player in team.players]).pack(side="right")
            positions_dict[position] = player_var

    def start_match(self):
        AssistantWindow(self.left_team, self.right_team, self.left_team_positions, self.right_team_positions, self.starting_team_var.get())
