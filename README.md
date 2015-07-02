# Introduction

Deploy app in marathon

# How to run.


``` bash
# Create a chronos.
./create_app.sh templates/chronos/chronos.json.tmpl

# Create a zk_web.
./create_app.sh templates/zk_web/zk_web.json.tmpl

# Create ambari hadoop cluster in mesos marathon.
CPUS=1 MEM=4096 ./create_app.sh templates/ambari/ambari_server.json.tmpl 
NUM_INSTANCES=3 CPUS=0.5 MEM=4096 AMBARI_SERVER=10.244.95.72 ./create_app.sh templates/ambari/ambari_agent.json.tmpl

# Create PredictionIO eventserver
NUM_INSTANCES=3 \
CPUS=0.3 MEM=2048 \
ES_NAME=$ES_NAME \
ES_HOST=$ES_HOST \
ES_T_PORT=$ES_T_PORT \
ZOOKEEPER_HOSTS=$ZOOKEEPER_HOSTS \
NAMENODE=$HDFS_NAMENODE \
./create_app.sh templates/predicitonio/predictionio_eventserver.json.tmpl
```

For ambari cluster. [See here for introduction](https://github.com/wangqiang8511/docker-ambari).
