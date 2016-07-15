#!/usr/bin/python
# Copyright 2016 Alexander Schmitt

import paho.mqtt.client as paho
import ssl
import config
from time import sleep
from datetime import datetime

connflag = False


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
    mqttc = paho.Client(client_id=config.aws_iot_clientid())
    mqttc.on_connect = on_connect
    mqttc.on_message = on_message
    mqttc.on_log = on_log

    mqttc.tls_set(caPath, certfile=certPath, keyfile=keyPath,
                  cert_reqs=ssl.CERT_REQUIRED,
                  tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)

    mqttc.connect(awshost, awsport, keepalive=60)

    mqttc.loop_start()

    while True:
        if connflag is True:
            heartbeat = datetime.utcnow().isoformat()
            JSONPayload = '{"state":{"desired":{"heartbeat":"' + \
                str(heartbeat) + '"}}}'
            print(JSONPayload)
            mqttc.publish("$aws/things/" + thingname +
                          "/shadow/update", JSONPayload, qos=1)
            print("msg sent: heartbeat " + str(heartbeat))
        else:
            print("waiting for connection...")
        sleep(config.aws_iot_heartbeat_rate())


connect("raspedge", "faafc87544-private.pem.key",
        "faafc87544-certificate.pem.crt")
