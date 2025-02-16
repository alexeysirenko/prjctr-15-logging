# prjctr-15-logging

Set up Graylog and ELK stasks to collect slow MySQL logs. Compare MySQL performance with different `long_query_time` values

### Setup a cluster

```
docker compose up -d
```

### Insert 1 million users

```
docker exec -it app python populate_db.py
```

### Create inputs for Graylog

```
chmod 775 graylog/setup-inputs.sh
./graylog/setup-inputs.sh
```

### Run tests

```
docker exec -it app siege -c10 -t30s "http://127.0.0.1:5000/search?name=test"
```

### Test results:

| long_query_time | transactions | longest_transaction |
| :-------------- | :----------: | :-----------------: |
| 0               |     295      |        1.62         |
| 1               |     315      |        1.42         |
| 10              |     328      |        1.37         |
