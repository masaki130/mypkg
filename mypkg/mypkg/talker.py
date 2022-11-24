#!/usr/bin/python3
#SPDX-FileCopyrightText:2022 Masaki Mitani
#SPDX-License Identifier;BSD-3-Clause

import rclpy
from rclpy.node import Node
from person_msgs.srv import Query

#rclpy.init()
#node = Node("talker")
#pub = node.create_publisher(Person, "person", 10)
#n = 0

def cb(request, response):
    if request.name == "三谷将貴":
        response.age = 21
    else:
        response.age = 255
    return response

    #global n
    #msg = Person()
    #msg.name = "三谷将貴"
    #msg.age = n
    #pub.publish(msg)
    #n += 1

rclpy.init()
node = Node("talker")
srv = node.create_service(Query, "query", cb)
rclpy.spin(node)
