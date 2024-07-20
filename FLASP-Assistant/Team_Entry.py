# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import Entry, Label, Button, Frame
from Team_Selection import TeamSelectionWindow

class Player:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Team:
    def __init__(self, name, players):
        self.name = name
        self.players = players

class TeamFrame(Frame):
    def __init__(self, parent, team_name):
        super().__init__(parent)

        self.entries = []

        Label(self, text=team_name).grid(row=0, column=0)
        self.team_name_entry = Entry(self)
        self.team_name_entry.grid(row=0, column=1)

        Label(self, text="Фамилия").grid(row=1, column=0)
        Label(self, text="Айди").grid(row=1, column=1)

        for i in range(2, 12):
            name_entry = Entry(self)
            name_entry.grid(row=i, column=0)
            id_entry = Entry(self)
            id_entry.grid(row=i, column=1)
            self.entries.append((name_entry, id_entry))

    def get_team(self):
        name = self.team_name_entry.get()
        players = [Player(name_entry.get(), id_entry.get()) for name_entry, id_entry in self.entries]
        return Team(name, players)

def start_match(left_frame, right_frame):
    left_team = left_frame.get_team()
    right_team = right_frame.get_team()
    TeamSelectionWindow(left_team, right_team)

def create_match_window():
    window = tk.Tk()
    window.title("Матч")

    left_frame = TeamFrame(window, "Команда хозяев")
    right_frame = TeamFrame(window, "Команда гостей")

    left_frame.pack(side="left", fill="both", expand=True)
    right_frame.pack(side="right", fill="both", expand=True)

    Button(window, text="К выбору составов", command=lambda: start_match(left_frame, right_frame)).pack()

    window.mainloop()

create_match_window()

