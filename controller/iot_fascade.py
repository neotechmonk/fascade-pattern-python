

from iot.devices import SmartSpeakerDevice
from iot.service import IOTService


class IOTFascade():
    def __init__(self, service : IOTService):
        self.service = service        
        # create the smart speaker
        self.smart_speaker = SmartSpeakerDevice()
        self.speaker_id = service.register_device(self.smart_speaker)