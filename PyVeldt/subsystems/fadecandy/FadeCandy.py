from ..LEDs.Strip import Strip
from . import opc
from typing import List
import warnings


class FadeCandy():

    def __init__(self, channel:int=0) -> None:
        ''''''
        self.channel = channel
        self.client_port = 'localhost:7892'
        self.client = opc.Client(self.client_port)
        
        self.strips = [None for x in range(8)]
        self.pixels = [(0,0,0) for x in range(512)]


    def add_strip(self, port:int, strip:Strip) -> None:
        ''''''
        if port not in range(8):
            raise ValueError(f'Invalid port: {port}')
        if strip.length() > 64:
            raise ValueError(f"FadeCandy's maximum amount of pixels is 64")
        if strip.has_W_channel:
            raise ValueError('FadeCandy does not support a white channel')
        
        if self.strips[port] is not None:
            warnings.warn(f"Port {port}: Overwriting strip '{self.strips[port].label}' with strip '{strip.label}'")

        self.strips[port] = strip
        

    def update_pixels(self) -> None:
        ''''''
        for port, strip in enumerate(self.strips):
            offset = port * 64
            self.pixels[offset:(offset+strip.length())] = strip.pixels
        self.client.put_pixels(self.pixels)
