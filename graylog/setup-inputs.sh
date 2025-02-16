#!/bin/bash

# Wait for Graylog API to become available
until curl -s -o /dev/null "http://127.0.0.1:9000/api/system/lbstatus"; do
  echo "Waiting for Graylog API..."
  sleep 5
done

# Create Beats Input via API
curl -X POST "http://127.0.0.1:9000/api/system/inputs" \
     -u admin:password \
     -H "Content-Type: application/json" \
     -H "X-Requested-By: graylog" \
     -d '{
       "title": "Beats Input",
       "type": "org.graylog.plugins.beats.BeatsInput",
       "configuration": {
         "bind_address": "0.0.0.0",
         "port": 5044,
         "recv_buffer_size": 1048576
       },
       "global": true
     }'

echo "Beats Input has been created!"
