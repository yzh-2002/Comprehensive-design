class TrafficSignal:
    def __init__(self,roads,config={}):
        # 初始化道路
        self.roads =roads
        # 设置默认配置
        self.set_default_config()
        # 更新配置
        for attr,val in config.items():
            setattr(self,attr,val)
        # 计算属性
        self.init_properties()

    def set_default_config(self):
        self.cycle =[(False,True),(True,False)] #
        self.slow_distance =50 #减速区域
        self.slow_factor =0.4 #减速系数？？
        self.stop_distance =15 #停车区域

        self.current_cycle_index =0

        self.last_t =0

    def init_properties(self):
        for i in range(len(self.roads)):
            for road in self.roads[i]:
                road.set_traffic_signal(self,i)

    @property
    def current_cycle(self):
        return self.cycle[self.current_cycle_index]

    def update(self,sim):
        cycle_length =30
        k =(sim.t // cycle_length) % 2 # //在python中是整除的意思
        self.current_cycle_index =int(k)
