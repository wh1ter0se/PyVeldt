from ..subsystems.LEDStrip import Segment
from ..utils import math
from typing import Tuple

class Map2D():
    def __init__(self) -> None:
        self.segments = []

    class MapSegment():
        def __init__(self, segment:Segment, start_pos:Tuple(int,int), vector:Tuple(int,int)):
            self.segment = segment
            self.length = self.segment.length
            self.start_pos = start_pos
            self.vector = vector

class Canvas2D():
    def __init__(self, label:str) -> None:
        self.label = label

        self.layers = []
        self.canvas_segments = []

    class Layer():
        def __init__(self, label:str): 
            self.label  = label

    def add_layer(self, layer:Layer):
        self.layers.append(layer)


class FunctionLayer(Canvas2D.Layer):

    def __init__(self, label:str, init_func:function=(lambda x,y:0,0,0)):
        ''''''
        super().__init__(label)
        self.func = init_func

    def set_func(self, func:function):
        self.func = func


class ObjectLayer(Canvas2D.Layer):
    def __init__(self, label:str):
        ''''''
        super().__init__(label)
        pass

    class Object():
        def __init__(self, center:Tuple(int,int), init_velocity:Tuple(int,int)=(0,0)):
            ''''''
            self.center = center
            self.velocity = init_velocity

        def set_center(self, new_x, new_y):
            ''''''
            self.center = (new_x, new_y)
        
        def get_RGBA(self, abs_position:Tuple(int,int)) -> Tuple(int,int,int,float): 
            ''''''
            raise NotImplementedError

    class Circle(Object):
        def __init__(self, center:Tuple(int,int), radius:float, color, feather:float=0, init_velocity:Tuple(int,int)=(0,0)):
            ''''''
            super().__init__(center, init_velocity)
            self.radius = radius
            self.color = color
            self.feather = feather

        def get_RGBA(self, abs_position:tuple) -> Tuple(int,int,int,float):
            ''''''
            dist = math.distance(abs_position, self.center)
            if dist <= self.radius: alpha = 1.0 # inside circle
            elif dist < self.radius + self.feather: # in feather region
                alpha = 1.0 - ((dist - self.radius) / self.feather)
            else: alpha = 0.0 # outside circle
            return (self.color.RGB, alpha)