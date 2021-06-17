#! /bin/bash

cd {{ microservice_destpath }}

nohup java -jar {{ microservice_fullname }} & 

sleep 6

num=`ps -ef | grep {{ microservice_fullname }} | grep -v "grep" | wc -l`

if [[ "${num}" == "0" ]];then
  exit 1
else
  exit 0
fi