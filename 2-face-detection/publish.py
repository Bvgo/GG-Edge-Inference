import sys
import greengrasssdk

class Publisher:
    def __init__(self, admin, main):
        self.admin = admin
        self.main = main

        if not sys.stdout.isatty():
            GGC = greengrasssdk.client('iot-data')
            def debug(topic=self.admin, payload=""):
                GGC.publish(topic=topic, payload=payload)
            self.publish = debug
        else:
            def debug(topic=self.admin, payload=""):
                print(topic, payload)
            self.publish = debug

