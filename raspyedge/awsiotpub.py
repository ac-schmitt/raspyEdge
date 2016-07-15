#!/usr/bin/python

# this source is part of my Hackster.io project:
# https://www.hackster.io/mariocannistra/radio-astronomy-with-rtl-sdr-raspberrypi-and-amazon-aws-iot-45b617

# use this program to test the AWS IoT certificates received by the author
# to participate to the spectrogram sharing initiative on AWS cloud

# this program will publish test mqtt messages using the AWS IoT hub
# to test this program you have to run first its companion awsiotsub.py
# that will subscribe and show all the messages sent by this program

import paho.mqtt.client as paho
# import os
# import socket
import ssl
import config
from time import sleep
from datetime import datetime
# from random import uniform

connflag = False
shadow = {"desired": {}, "reported": {}}


def on_connect(client, userdata, flags, rc):
    global connflag
    connflag = True
    print("Connection returned result: " + str(rc))


def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))


def on_log(client, userdata, level, buf):
    print("paho log: " + str(buf))


def connect(thingname,
            keyPath,
            certPath=config.aws_iot_certpath(),
            awshost=config.aws_iot_endpoint(),
            awsport=config.aws_iot_port(),
            caPath=config.aws_iot_capath()):
    mqttc = paho.Client()
    mqttc.on_connect = on_connect
    mqttc.on_message = on_message
    mqttc.on_log = on_log

#    clientId = config.aws_iot_clientid
#    thingName = config.aws_iot_thingname

    mqttc.tls_set(caPath, certfile=certPath, keyfile=keyPath,
                  cert_reqs=ssl.CERT_REQUIRED,
                  tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)

    mqttc.connect(awshost, awsport, keepalive=60)

    mqttc.loop_start()

    while True:
        sleep(config.aws_iot_heartbeat_rate())
        if connflag is True:
            heartbeat = datetime.now().time()
            JSONPayload = '{"state":{"desired":{"heartbeat":"' + \
                str(heartbeat) + '"}}}'
            print(JSONPayload)
            mqttc.publish("$aws/things/" + thingname +
                          "/shadow/update", JSONPayload, qos=1)
            print("msg sent: heartbeat " + str(heartbeat))
        else:
            print("waiting for connection...")


connect("raspedge", "faafc87544-private.pem.key",
        "faafc87544-certificate.pem.crt")
