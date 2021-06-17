#! /bin/bash

cd "{{ microservice_destpath }}"

num=`ps -ef | grep {{ microservice_fullname }} | grep -v "grep" | wc -l`

filename=`date +"%Y%m%d_%H%M%S"`

if [[ "${num}" == "0" ]];then
  mv {{ microservice_fullname}} ./bak/{{ microservice_fullname }}_${filename}
  exit 0
else
  ps -ef | grep {{ microservice_fullname }} | grep -v "grep" | awk '{print $2}' | xargs -i kill {}
  mv {{ microservice_fullname}} ./bak/{{ microservice_fullname }}_${filename}
fi
