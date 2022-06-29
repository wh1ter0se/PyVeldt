from itertools import permutations as permute
from typing import List, Tuple

class Strip():

    def __init__(self, label:str, lengths:List[int], 
                 type:str='WS2811', leds_per_m:int=30, color_order:str='RGB') -> None:
        '''Multi-channel addressable LED strip.
        
           Arguments:
           - label: Identifiable name for this strip.
           - lengths: A list of discrete segment lengths (to be used
               when multiple strips are wired in series on the same data line)
           - type: The type of addressable LED controller.
           - leds_per_m: The amount of *addressable* controllers per meter of 
                the strip. NOTE: In some strips (especially WS2811), there may
                only be 1 addressable controller for every 3 LEDs.
           - color_order: A string containg the order of the R, G, B (and 
                optionally W) channels.'''
            
        self.label = label
        self.leds_per_m = leds_per_m

        self.type = type.upper().strip()
        if self.type not in ['WS2811', 'WS2812B']:
            raise ValueError(f'Invalid type: {self.type}')

        self.color_order = color_order.upper().strip()
        if self.color_order not in [*[''.join(x) for x in permute('RGB')], 
                                    *[''.join(x) for x in permute('RGBW')]]:
            raise ValueError(f'Invalid color_order: {self.color_order}')
        self.has_W_channel = 'W' in self.color_order
        self.num_channels = len(self.color_order)
        
        self.segments = {}
        for index, length in enumerate(lengths,1):
            segment_label = f'{label}-{index}' # index starts at 1
            self.segments[segment_label] = Segment(strip=self, 
                                               label=segment_label, 
                                               length=length, 
                                               offset=sum(lengths[:index-1]))

        self.pixels = [(0,)*self.num_channels for x in range(self.length())]
        self.enabled = True


    def get_segment(self, segment_label:str): # -> Segment
        ''''''
        for key, value in self.segments.items():
            if key == segment_label: return value


    def get_segments(self) -> list: # -> List[Segment]
        ''''''
        return list(self.segments.values())


    def length(self) -> int:
        ''''''
        return sum(seg.length for seg in self.segments.values())

        



class Segment():

    def __init__(self, strip:Strip, label:str, length:int, offset:int) -> None:
        ''''''
        self.label = label
        
        self.strip = strip
        self.length = length
        self.offset = offset

        #self._pixels = [(0,)*self.strip.num_channels for x in range(self.length)]


    def pixels(self) -> List[Tuple[int,int,int]]:
        ''''''
        return self.strip.pixels[self.offset:(self.offset+self.length)]
