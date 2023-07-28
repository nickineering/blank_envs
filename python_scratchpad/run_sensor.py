"""
## Overview ##

You’re designing software for a mission-critical device which contains multiple sensors, each controlled by an independent program.
Each of these sensor programs is able to generate messages describing its state. It is key that the device be able to report this information 
to a centralised cloud-based monitoring system, so that faults and downtime can be minimised. To accomplish this you’ve been tasked with 
designing software that will enable each of these programs to report their state to the cloud monitoring system. This file contains the template 
to use to emulate a sensor program. The device is running a Linux environment. You may consider using any python libraries and Linux utilities. 

## Objective ##

Your task is to design the __send_state__ function and any additional software needed to achieve the desired functionality, respecting the 
constraints below. The resulting work is expected to be runnable and demonstrate the desired functionality.

## Constraints ##

1. Use the following request bin to send the state data to: https://requestbin.com/r/en6msadu8lecg

2. Unit tests should be present for the send_state function.

3. The sensor data processing function is mission-critical and time sensitive: calls to the __send_state__ function should be non-blocking with 
minimal performance impact regardless of connectivity issues.

4. The device should be able to run in offline mode, in which case any connectivity requests will fail. In this case the desired behavior is 
that the state events should be buffered until the device comes online, at which point these events would be sent. Consider edge cases for when 
the device runs offline for extended periods of time.

5. BONUS: Consider that the device can be turned off and turned on at any time during its normal use. Implement an approach that allows the device 
to not lose buffered events in case of a poweroff.
"""

import time
import uuid
import random


class Sensor:
    def __init__(self):
        self.sensor_id = str(uuid.uuid4())
        print(f"Created sensor: {self.sensor_id}")

    def _event_type(self):
        event_types = ["nominal", "info", "warning", "error", "critical"]
        return random.choices(event_types, cum_weights=[60, 24, 10, 5, 1], k=1)[0]

    def do_work(self):
        time.sleep(random.uniform(0.1, 1.5))

    @property
    def state(self):
        return {
            "id": self.sensor_id,
            "event": {
                "type": self._event_type(),
                "readings": [random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)],
            },
            "timestamp": int(time.time()),
        }


def send_state(state):
    # TODO: Implement me
    print(state)
    pass


def main():
    sensor = Sensor()

    while True:
        sensor.do_work()
        send_state(sensor.state)


if __name__ == "__main__":
    main()
