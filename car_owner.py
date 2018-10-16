import time
from car import Car
from park_ground import ParkGround
from park_records import ParkRecords
from park_place import ParkPlace
class CarOwner():
    togroundtime=0
    toplacetime=0
    exitroundtime=0
    exitplacetime=0
    def __init__(self,owner_name,owner_phone,owner_no):
        self.owner_name=owner_name
        self.owner_phone=owner_phone
        self.owner_no=owner_no
    #车主开车进入停车场
    def drive_topark(self,car,parkground):
        choice=parkground.car_isfull(parkground.car_list)
        if choice==True:
            CarOwner.togroundtime=time.ctime()
            print('车主{} 电话号为{} 开着车号为{} 车型为{} 颜色为{} 品牌为{} 进入{} 时间为{}'.format(self.owner_name,self.owner_phone,car.car_number,car.car_model,car.car_color,car.car_brand,parkground.Parkground_name,CarOwner.togroundtime))
            ParkRecords.parkrecords.append(['车编号：1','车牌号：{}'.format(car.car_number) ,'进入停车场时间：{}'.format(CarOwner.togroundtime),'','',''])  
        else:
            print('车位已满，请等候！')
     #车主把车停到车位
    def drive_toparkplace(self,parkplace):
            CarOwner.toplacetime=time.ctime()
            print('{}开车进入{}车位,时间为{}'.format(self.owner_name,parkplace.parkplace_name,CarOwner.toplacetime))
            ParkRecords.parkrecords[0][3]='停到车位时间:{}'.format(CarOwner.toplacetime)
    #车主购物完驾车离开车位
    def drive_exitplace(self):
            CarOwner.exitplacetime=time.ctime
            ParkRecords.parkrecords[0][4]='离开车位时间:{}'.format(CarOwner.exitplacetime)
            print('车主{}开车离开车位'.format(self.owner_name))
    #车主驾车到达出口
    def drive_reachpart(self):
            print('车主{}到达出口，生成订单，缴纳停车费'.format(self.owner_name))
    #车主交完费驶离出口
    def drive_exitpart(self,car):
            CarOwner.exitroundtime=time.ctime
            ParkRecords.parkrecords[0][5]='离开停车场时间:{}'.format(CarOwner.exitroundtime)
            print('车主{}离开停车场，车号为{}'.format(self.owner_name,car.car_number))
            print('--------------停车记录--------------')
            for i in range(len(ParkRecords.parkrecords)):
                for j in range(len(ParkRecords.parkrecords[0])):
                    print(ParkRecords.parkrecords[i][j],end='\n'+'----------------------------'+'\n')


            
    
        



    
        
