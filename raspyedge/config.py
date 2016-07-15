# Copyright 2016 Alexander Schmitt

_aws_iot_endpoint = "data.iot.eu-west-1.amazonaws.com"
_aws_iot_port = 8883
_aws_iot_clientid = "raspyedge"
_aws_iot_thingname = "raspyedge"
_aws_iot_capath = \
    "VeriSign-Class 3-Public-Primary-Certification-Authority-G5.pem"
_aws_iot_certpath = ""
_aws_iot_keypath = ""
_aws_iot_heartbeat_rate = 1


def aws_iot_endpoint():
    return _aws_iot_endpoint


def aws_iot_port():
    return _aws_iot_port


def aws_iot_clientid():
    return _aws_iot_clientid


def aws_iot_thingname():
    return _aws_iot_thingname


def aws_iot_capath():
    return _aws_iot_capath


def aws_iot_certpath():
    return _aws_iot_certpath


def aws_iot_keypath():
    return _aws_iot_keypath


def aws_iot_heartbeat_rate():
    return _aws_iot_heartbeat_rate
