# rpiFanAutoControl（树莓派风扇自动调速）

<!-- <p>
    <img src='https://www.soulfree.cn/wp-content/uploads/2020/09/1600448265-Snipaste_2020-09-19_00-56-18.png' width='300'/>
</p> -->

## 增加了静音模式，夜间时风扇更加安静
实测静音模式下 cpu稳定在 48 - 50 度 也还可以

### 20:00 - 2:00 为静音模式
可根据需求自行修改
``` python
n = time.asctime(time.localtime(time.time()))  # 当前时间
nowHour = int(time.strftime("%H", time.localtime()))  # 当前小时
if nowHour >= 20 or nowHour <= 2:
    mode = "mute"
else:
    mode = "normal"

```
温度℃ | 正常(频率) | 静音(频率)
- | - | -
50° | 100 | 30
48° | 90 | 30
45° | 70 | 30
40° | 40 | 30

## 注
pwm频率范围为 0.0-100.0 风扇转速依次增大

---

[Blog](https://www.soulfree.cn/index.php/2020/09/19/rpifanautocontrol)
