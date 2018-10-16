from car import Car
from car_owner import CarOwner
from park_ground import ParkGround
from park_place import ParkPlace
def main():
    car=Car('辽AR17C0','小轿车','红色','本田')
    carowner=CarOwner('Tom','15840246978','001')
    parkground=ParkGround('远航中路','万隆停车场','地下')
    parkplace=ParkPlace('中区001')
    carowner.drive_topark(car,parkground)
    carowner.drive_toparkplace(parkplace)
    carowner.drive_reachpart()
    carowner.drive_exitpart(car)
if __name__ == '__main__':
    main()
    
