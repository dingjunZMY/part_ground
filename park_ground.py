import time

from park_records import ParkRecords
class ParkGround():
    def __init__(self,parkground_address,parkground_name,parkground_type,park_balance=20):
        self.parkground_address=parkground_address
        self.Parkground_name=parkground_name
        self.Parkground_type=parkground_type
        self.car_list=[]
    #车辆进入停车场前判断停车场是否已满
    def car_isfull(self,car_list):
        if len(car_list)<20:
            return True
        else:
            return False 
    
    

    

