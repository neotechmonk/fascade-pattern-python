


import logging

from iot_fascade import IOTFascade


def power_speaker(on : bool , iot : IOTFascade) -> None:
    logging.info(f"Powering speaker {on}")
    iot.power_speaker(on) 
    logging.info("Message sent to speker")

def get_status( iot : IOTFascade) -> None:
    logging.info(f"Display status for IOT devices.")
    status = iot.get_status()
    logging.info(f"Status: {status}")
    return status

