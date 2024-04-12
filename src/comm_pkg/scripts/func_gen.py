#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import pyvisa
import gpib_ctypes
from std_msgs.msg import String

    # 장치 연결 (연결 문자열은 실제 장치에 맞게 수정하세요)
    # instr = rm.open_resource('GPIB0::11::INSTR')
    # instr = rm.open_resource('USB0::0x0699::0x0356::C017460::INSTR')
    # ASRL/dev/ttyUSB0::INSTR

def func_gen():
    # node 설정
    rospy.init_node('func_gen', anonymous=True)
    rate = rospy.Rate(10)

    rm = pyvisa.ResourceManager()                # VISA 리소스 매니저 생성
    rm.list_resources()
    instr = rm.open_resource('USB0::0x0699::0x0356::C017460::INSTR')      # 장치 포트 Open

    voltage = 1

    instr.write('*IDN?')
    instr.write('FUNCTION DC')
    

    # response = instr.query('FUNCTION SIN')
    # print(response)

    # response = instr.query('SOURce1:VOLTage:LEVel:IMMediate:OFFSet 1')
    # print(response)

    # response = instr.query('OUTPUT ON')
    # print(response)
    

    # 통신 반복문 설정
    while not rospy.is_shutdown():
        instr.write('SOURce1:VOLTage:LEVel:IMMediate:OFFSet {}V'.format(1))
        instr.write('SOURce1:VOLTage:LEVel:IMMediate:OFFSet {}V'.format(0.5))

        rate.sleep()


if __name__ == '__main__':
    try:
        func_gen()
    except rospy.ROSInterruptException:
        pass

