import time
import RPi.GPIO as GPIO

FAN_GPIO = 14  # 针脚 博客上边有针脚图
SLEEP_TIME = 60  # 每60秒检测温度并修改一次频率
mode = "mute"  # 模式

GPIO.setmode(GPIO.BCM)
GPIO.setup(FAN_GPIO, GPIO.OUT)
p = GPIO.PWM(FAN_GPIO, 331)
p.start(50)

# temp 温度
# normal 默认 pwm频率
# mute  静音
arr = [
    {
        "temp": 50,
        "normal": 100,
        "mute": 30
    },
    {
        "temp": 48,
        "normal": 90,
        "mute": 30
    },
    {
        "temp": 45,
        "normal": 70,
        "mute": 30
    },
    {
        "temp": 40,
        "normal": 40,
        "mute": 30
    }
]
# 注：pwm 范围为0 - 100 值越大转的越快 反之则越慢

while True:
    # 获取CPU温度
    tmpFile = open('/sys/class/thermal/thermal_zone0/temp')
    cpu_temp_raw = tmpFile.read()
    tmpFile.close()
    cpu_temp = round(float(cpu_temp_raw) / 1000, 1)
    t = cpu_temp

    # 取时间 修改模式 20:00 - 2:00 为静音模式
    n = time.asctime(time.localtime(time.time()))  # 当前时间
    nowHour = int(time.strftime("%H", time.localtime()))  # 当前小时

    if nowHour >= 20 or nowHour <= 2:
        mode = "mute"
    else:
        mode = "normal"

    for item in arr:
        if t >= item["temp"]:
            p.ChangeDutyCycle(item[mode])
            print(item[mode], t, mode, n)
            time.sleep(SLEEP_TIME)
            break
