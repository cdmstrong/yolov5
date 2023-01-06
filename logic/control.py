# 用来控制 停车场的类
from enum import Enum
import numpy as np
import time
from PyQt5 import QtCore, QtGui, QtWidgets
import cv2 as cv
import random
import datetime
class resource_type(Enum):
    camera = 1,
    video = 2
d1 = datetime.datetime.now()

class Car() :
    def __init__(self, license) -> None:
        # self.id = np.randomInt(10)
        self.enter_time = datetime.datetime.now()
        self.leave_time = self.enter_time  + datetime.timedelta(hours=random.randint(1, 20))
        self.given = False
        self.license = license

class ParkingLot() :
    def __init__(self) -> None:
        self.max = 100
        self.pass_all = False
        self.forbiden = False
        self.white_acc = False
        self.black_err = False
        self.free_time = 1
        self.price_hour = 5
        self.income = 0
        self.resources = resource_type.video
        self.car_list = []
    def set_passErr(self, state):
        self.pass_all = state
    def set_passAll(self, state):
        self.pass_all = state
        print(self.pass_all)
    def set_black(self, state):
        self.black_err = state
    def set_white(self, state):
        self.white_acc = state
    def add_car(self, car: Car):
        self.car_list.append(car)
        print(self.max )
        self.max = self.max - 1
        return self.max, len(self.car_list)
    def leave_car(self, car: str):
        j = 0
        stopCar = None
        for i in range(len(self.car_list)):
            if self.car_list[j].license == car:
                stopCar = self.car_list[j]
                self.car_list.pop(j)
            else:
                j += 1
        if(stopCar):
            seconds = (stopCar.leave_time - stopCar.enter_time).seconds/3600
            giveTime = seconds - self.free_time
            self.income += 0 if giveTime < 0 else giveTime * self.price_hour
            # self.car_list.remove(car)
            print(f"停车时长{seconds}, 免费时长{self.free_time}")
            self.max += 1
            return self.max, len(self.car_list), giveTime * self.price_hour
        
    def selectFile(self, ui):
            print('button_image_open')
            name_list = []
            try:
                img_name, _ = QtWidgets.QFileDialog.getOpenFileName(None, "选择文件",'./', filter="*.jpg;;*.png;;All Files(*)")
            except OSError as reason:
                print('文件出错啦')
                QtWidgets.QMessageBox.warning(ui, 'Warning', '文件出错', buttons=QtWidgets.QMessageBox.Ok)
            else:
                if not img_name:
                   QtWidgets.QMessageBox.warning(ui,"Warning", '文件出错', buttons=QtWidgets.QMessageBox.Ok)
                   self.log('文件出错')
                else:
                    img = cv.imread(img_name)
                    # info_show = self.recognize.skim_video(img)
                    date = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) # 当前时间
                    file_extaction = img_name.split('.')[-1]
                    new_fileName = date + '.' + file_extaction
                    # file_path = self.output_folder + 'img_output/' + new_fileName
                    # cv.imwrite(file_path, img)
                    # self.show_img(info_show, img)
                    print(img_name)
                    
    def setFree_time(self, value):
        self.free_time = value.value()
        
        
    def setPrice(self, price):
        self.price_hour = price.value()
    def find_car(self, license: str):
        item = [x for x in self.car_list if x.license == license]
        if item:
            return item
    def pay_car(self, license: str):
        item = self.find_car(license)
        item.given = True
        print('open the parking')
    
        
    