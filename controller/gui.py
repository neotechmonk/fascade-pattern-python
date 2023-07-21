import logging
import tkinter as tk
from typing import Callable

from iot.devices import SmartSpeakerDevice
from iot.service import IOTService
from message.helper import Message as Msg
from network.connection import Connection

OFF_TEXT = "Speaker OFF"
ON_TEXT = "Speaker ON"
STATUS_UPDATE_TEXT = "Status Update"


class SmartApp(tk.Tk):
    def __init__(self, power_speaker_fn : Callable[[bool], None ], power_status_fn : Callable[[], str]) -> None:
        super().__init__()
        self.title("Smart App")
        self.geometry("400x250+300+300")
        self.speaker_on = False
        self.power_speaker_fn = power_speaker_fn
        self.power_status_fn = power_status_fn

        # create a IOT service
        self.service = IOTService()

        # create the smart speaker
        smart_speaker = SmartSpeakerDevice()
        self.speaker_id = self.service.register_device(smart_speaker)

        self.create_ui()

    def create_ui(self) -> None:
        self.toggle_button = tk.Button(
            self, text=OFF_TEXT, width=10, command=self.toggle
        )
        self.get_status_button = tk.Button(
            self, text=STATUS_UPDATE_TEXT, width=10, command=self.display_status
        )
        self.status_label = tk.Label(self, text="")
        self.toggle_button.pack()
        self.get_status_button.pack()
        self.status_label.pack()

