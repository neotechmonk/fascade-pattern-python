
import logging
from functools import partial

from gui import SmartApp
from iot.service import IOTService
from iot_controller import get_status, power_speaker
from iot_fascade import IOTFascade


def main():
    logging.basicConfig(level=logging.INFO)

    # create a IOT service
    service = IOTService()

    # create the fascade 
    iot_speaker = IOTFascade(service)

    power_speaker_fn = partial(power_speaker, iot=iot_speaker)
    get_status_fn= partial(get_status, iot=iot_speaker) 

    app = SmartApp(power_speaker_fn, get_status_fn)
    app.mainloop()


if __name__ == "__main__":
    main()