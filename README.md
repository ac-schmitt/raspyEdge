Raspberry Py IoT Edge Application
=================================

This projects shows how to connect a Raspberry Pi with AWS IoT.

Everything is done with no platform SDKs whatsoever. This is for my own educational purposes and probably never complete. If you are thinking about doing this in production, please check with the AWS SDKs.

## 2016-08-23

Usage for AWS IoT Shadow Publisher:

python3 awsIotPublishShadow -k <keyPath> -c <certPath> -t <thingName>

Example:
python3 awsIotPublishShadow -k abcde12345-private.pem.key -c abcde12345-certificate.pem.crt -t myThingName

It eventually comes ready equiped with support for the following sensors:

- Internal sensors from the Raspberry Hardware
- Texas Instruments Sensor Tag


