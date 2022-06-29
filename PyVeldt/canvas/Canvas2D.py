from ..subsystems.LEDs.Strip import Segment
from ..utils.math import distance

class Canvas2D():
    def __init__(self, label:str) -> None:
        self.label = label

        self.layers = []
        self.canvas_segments = []
        

    class CanvasSegment():
        def __init__(self, segment:Segment, start_pos:tuple, vector:tuple):
            self.segment = segment
            self.length = self.segment.length
            self.start_pos = start_pos
            self.vector = vector


    class Layer():
        def __init__(self): 
            pass
    

    class FunctionLayer(Layer):

        def __init__(self, init_func:function=(lambda x,y:0,0,0)):
            ''''''
            self.func = init_func

        def set_func(self, func:function):
            self.func = func


    class ObjectLayer(Layer):
        def __init__(self):
            ''''''
            pass

        class Object():
            def __init__(self, center:tuple, init_velocity:tuple=(0,0)):
                ''''''
                self.center = center
                self.velocity = init_velocity

            def set_center(self, new_x, new_y):
                ''''''
                self.center = (new_x, new_y)
            
            def get_RGBA(self, abs_position:tuple) -> tuple: 
                ''''''
                raise NotImplementedError

        class Circle(Object):
            def __init__(self, center:tuple, radius:float, color, feather:float=0, init_velocity:tuple=(0,0)):
                ''''''
                super().__init__(center, init_velocity)
                self.radius = radius
                self.color = color
                self.feather = feather

            def get_RGBA(self, abs_position:tuple) -> tuple:
                ''''''
                dist = distance(abs_position, self.center)
                if dist <= self.radius: alpha = 1.0 # inside circle
                elif dist < self.radius + self.feather: # in feather region
                    alpha = 1.0 - ((dist - self.radius) / self.feather)
                else: alpha = 0.0 # outside circle
                return (self.color.RGB, alpha)