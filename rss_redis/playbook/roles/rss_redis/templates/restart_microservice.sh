#! /bin/bash

cd "{{ microservice_destpath }}"

num=`ps -ef | grep {{ microservice_fullname }} | grep -v "grep" | wc -l`

filename=`date +"%Y%m%d_%H%M%S"`

if [[ "${num}" == "0" ]];then
else
  ps -ef | grep {{ microservice_fullname }} | grep -v "grep" | awk '{print $2}' | xargs -i kill {}
fi

echo "service shutdown"

cd {{ microservice_destpath }}

nohup java -jar {{ microservice_fullname }} & 

sleep 6

num=`ps -ef | grep {{ microservice_fullname }} | grep -v "grep" | wc -l`

if [[ "${num}" == "0" ]];then
  exit 1
  echo "service start"
else
  exit 0
fi
