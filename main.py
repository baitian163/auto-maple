"""The central program that ties all the modules together."""

import time
import os
from src.modules.bot import Bot
from src.modules.capture import Capture
from src.modules.notifier import Notifier
from src.modules.listener import Listener
from src.modules.gui import GUI


# 禁用所有 GPU 设备，强制 TensorFlow 只看得到 CPU
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
# 禁用 TensorFlow 的日志输出（可选，减少终端噪音）
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


bot = Bot()
capture = Capture()
notifier = Notifier()
listener = Listener()

bot.start()
while not bot.ready:
    time.sleep(0.01)

capture.start()
while not capture.ready:
    time.sleep(0.01)

notifier.start()
while not notifier.ready:
    time.sleep(0.01)

listener.start()
while not listener.ready:
    time.sleep(0.01)

print('\n[~] Successfully initialized Auto Maple')

gui = GUI()
gui.start()
