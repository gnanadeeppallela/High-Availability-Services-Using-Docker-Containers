#!/bin/sh


# Change the parameters according to the configuration of wamp server, the port number should be same as the server
ip="127.0.0.1"
port="8096"
realm="realm1"
path=$HOME/Desktop/ecep_client-master/

echo "END NODE CREATED"

# Do not edit the below line
python -m ecep_endNode.ecep_wampClient.deviceRegister $ip $port $realm $path
