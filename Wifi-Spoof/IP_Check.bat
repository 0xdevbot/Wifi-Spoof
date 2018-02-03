#!/bin/bash

Check="$(cat /proc/sys/net/ipv4/ip_forward)"

if [ $Check == "0" ] ; then
    echo "Setting IP forwarding"
    echo  "1" >>/proc/sys/net/ipv4/ip_forward
fi
