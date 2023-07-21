

from iot.devices import SmartSpeakerDevice
from iot.service import IOTService
from message.helper import Message as Msg
from network.connection import Connection


class IOTFascade():
    def __init__(self, service : IOTService):
        self.service = service        
        # create the smart speaker
        self.smart_speaker = SmartSpeakerDevice()
        self.speaker_id = service.register_device(self.smart_speaker)


    def power_speaker(self, on : bool ) -> None:

        msg =  'switch_on' if on else 'switch_off'
      
        # create a connection to the smart speaker
        speaker_ip, speaker_port = self.service.get_device(
            self.speaker_id
        ).connection_info()
        speaker_connection = Connection(speaker_ip, speaker_port)

        # construct a message
        message = Msg(
            "SERVER",  self.speaker_id, msg
        )

        # send the message
        speaker_connection.connect()
        speaker_connection.send(message.b64)
        speaker_connection.disconnect()

    def get_status(self) -> None:
        self.status = ""
        for device_id, device in self.service.devices().items():
            self.status += f"{device_id}: {device.status_update()}"
        return self.status
