# Comprehensive-design
单交叉口实时交通流采集与预测系统的设计与实现

## app

> electron应用（electron+react）

## ml

> 机器学习部分

## test/simulation

> 交通仿真部分

核心代码位于trafficSimulator文件夹下：

1. window.py
2. vehicle.py
3. road.py
4. traffic_signal.py
5. vehicle_generator.py
6. simulation.py
7. curve.py

### 依赖管理（python）

1. 项目依赖第三方库于requirements.txt中
2. 新项目安装依赖 `pip install -r requirements.txt`
3. 添加新依赖更新依赖配置文件 `pip freeze > requirements.txt`