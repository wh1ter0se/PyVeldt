from serial import Serial

class MSGEQ7():

    def __init__(self, serial_port:str, stereo:bool=False) -> None:
        self.port = serial_port
        self.stereo = stereo
        self.ser = Serial(self.port,115200,timeout=1)

    def start(self):
        pass

    def stop(self):
        pass