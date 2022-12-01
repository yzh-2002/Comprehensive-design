import numpy as np

class Vehicle:
    def __init__(self,config={}):
        # 设置默认配置
        self.set_default_config()

        # 更新配置
        for attr,val in config.items():
            setattr(self,attr,val)

        # 计算车辆信息
        self.init_properties()

    def set_default_config(self):
        self.l =4 #车身长度
        self.s0 =4 #
        self.T =1 #驾驶员反应时间
        self.v_max =16.6 #最大车速
        self.a_max =1.44 #最大加速度
        self.b_max =4.61 #舒适减速度

        self.path =[]
        self.current_road_index =0

        self.x =0 #车辆坐标两个维度：所在车道+所在车道的坐标x
        self.v =self.v_max # 初始满速？
        self.a =0
        self.stopped =False

    def init_properties(self):
        # 开根号，计算IDM模型所需
        self.sqrt_ab =2*np.sqrt(self.a_max*self.b_max)
        self._v_max =self.v_max


    def update(self,lead,dt):
        """
        @param lead:Vehicle 前一辆车辆
        @param dt:
        """
        # 更新位置和速度
        if self.v + self.a*dt<0:
            self.x -=1/2*self.v*self.v/self.a #v^2/2a
            slef.v =0;
        else:
            self.v +=self.a*dt
            self.x +=self.v*dt +self.a*dt*dt/2  #vt+1/2at^2

        # 更新加速度
        alpha =0 #安全距离与实际前车距离的比值，越小越安全，无前者则为0
        if lead:
            delta_x =lead.x -self.x -lead.l #距离前车尾部的距离
            delta_v =self.v -lead.v #与前车速度差

            alpha =(self.s0+max(0,self.T*self.v+delta_v*self.v/self.sqrt_ab))/delta_x

        self.a =self.a_max * (1-(self.v/self.v_max)**4 -alpha**2) #参考IDM模型

        # 进入红绿灯口停车距离的减速度
        if self.stopped:
            self.a =-self.b_max*self.v/self.v_max

    def stop(self):
        self.stopped =True

    def unstop(self):
        self.stopped =False

    # 更新最大速度？
    def slow(self,v):
        self.v_max =v

    def unslow(self):
        self.v_max =self._v_max