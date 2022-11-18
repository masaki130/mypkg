#!/usr/bin/python3
#SPDX-FileCopyrightText:2022 Masaki Mitani
#SPDX-License Identifier;BSD-3-Clause

import rclpy
from rclpy.node import Node
form std_msgs.msg import Int16

def cb(msg):
    global node
    node.get_logger().info("Listen: %d" % msg.data)

rclpy.init()
node = Node("listener")
pub = node.create_subscription(Int16."countup", cb, 10)
rclpy.spin(node)
