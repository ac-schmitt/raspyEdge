#!/usr/bin/python
# Copyright 2016 Alexander Schmitt

import paho.mqtt.client as paho
import ssl
import sys
import getopt
import config
from time import sleep
from datetime import datetime

pahoclient = paho.Client(client_id=config.aws_iot_clientid())


def on_connect(client, userdata, flags, rc):
    print("Connected!: " + str(rc))


def on_publish(client, userdata, mid):
    print("msg sent: " + str(userdata) + ", " + str(mid))


def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))


def on_log(client, userdata, level, buf):
    print("paho log: " + str(buf))


def connect(keyPath,
            certPath=config.aws_iot_certpath(),
            awshost=config.aws_iot_endpoint(),
            awsport=config.aws_iot_port(),
            caPath=config.aws_iot_capath()):
    pahoclient.on_connect = on_connect
    pahoclient.on_message = on_message
    pahoclient.on_publish = on_publish
    pahoclient.on_log = on_log

    pahoclient.tls_set(caPath, certfile=certPath, keyfile=keyPath,
                       cert_reqs=ssl.CERT_REQUIRED,
                       tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)
    pahoclient.connect(awshost, awsport, keepalive=60)
    pahoclient.loop_start()


def publish(thingname=config.aws_iot_thingname()):
    while True:
        heartbeat = datetime.utcnow().isoformat()
        JSONPayload = '{"state":{"desired":{"heartbeat":"' + \
            str(heartbeat) + '"}}}'
        pahoclient.publish("$aws/things/" + thingname +
                           "/shadow/update", JSONPayload, qos=1)
        sleep(config.aws_iot_heartbeat_rate())


def main(argv):
    keyPath = config.aws_iot_keypath()
    certPath = config.aws_iot_certpath()
    thingName = config.aws_iot_thingname()

    try:
        opts, args = getopt.getopt(argv, "k:c:t:")
    except getopt.GetoptError:
        print("<script> -k <keyPath> -c <certPath> -t <thingName>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-k":
            keyPath = arg
        elif opt == "-c":
            certPath = arg
        elif opt == "-t":
            thingName = arg

    connect(keyPath, certPath)
    publish(thingName)

if __name__ == "__main__":
    main(sys.argv[1:])
