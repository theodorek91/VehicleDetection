from collections import defaultdict

class Detection(object):
    def __init__(self, Object_Number, Car_intial_Position, Initial_Frame_No):
        # Car Number must be initial car.
        self.Car_Number = Car_Number
        # Position Value must be in terms of [[x1,y1],[x2,y2]]
        self.Initial_position = Car_initial_Position
        self.detected = True
        self.location_dict = defaultdict[list]
        self.Intial_Frame = Initial_Frame_No
        self.Type = "Not_detected_yet"
        self.Local_Frame = 1

    def set_attributes(self, Current_position, Frame_no):
        self.current_position = Current_position
        self.Current_Frame_No = Frame_no
        self.location_dict['position'].append(self.current_position)
        self.location_dict['Frame_No'].append(self.Current_Frame_No)
    
    def calculate_midpoint(self):
        if self.Current_Frame_No > self.Intial_Frame +2 :
            self.current_midpoint = [(self.current_position[0][0]+self.current_position[1][0])/2),
                                        (self.current_position[0][1]+self.current_position[1][1])/2)
            self.location_dict['midpoint'].append(self.current_midpoint)
        else:
            #print('requires more frames to calculate midpoint')
            pass
        return self.current_midpoint

    def set_detection_type(self):
        if self.Current_Frame_No = self.Intial_Frame+3:
            self.detection_type = "Car"
        else:
            self.detection_type = "Not_Car"

    def increment_local_frame(self):
        self.Local_Frame +=1

    def 
            

    
    