# 计算距离模块（常用于计算距离矩阵）
from scipy.spatial import distance
# collections是python内建的集合模块，deque是双向列表
from collections import deque

class Road:
    def __init__(self,start,end):
        """
        @param start:Int[] 二维坐标，一维数组
        @param end:Int[] 二维坐标，一维数组
        """
        self.start =start
        self.end =end

        self.vehicles =deque() #road上的车辆队列
        self.init_properties()

    def init_properties(self):
        self.length =distance.euclidean(self.start,self.end) #计算一维数组（二维坐标）欧式距离（也即两点之间的直线长度）
        self.angle_sin =(self.end[1] -self.start[1])/self.length
        self.angle_cos =(self.end[0] -self.start[0])/self.length

        self.has_traffic_signal =False #是否有信号灯

    def set_traffic_signal(self,signal,group):
        """
        @param signal:
        @param group:
        """
        self.traffic_signal =signal
        self.traffic_signal_group =group
        self.has_traffic_signal =True

    @property #python内置的装饰器，可以直接road实例.traffic_signal_state调用该方法（无需加括号调用）
    def traffic_signal_state(self):
        if self.has_traffic_signal:
            i =self.traffic_signal_group
            return self.traffic_signal.current_cycle[i]
        return True

    def update(self,dt):
        n =len(self.vehicles)

        if n>0:
            # 更新第一辆车
            self.vehicles[0].update(None,dt) # lead为None

