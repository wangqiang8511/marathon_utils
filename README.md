# Introduction

Deploy apps in marathon

# Features

Quickly deploy apps in marathon.

# How to run.


```bash
# Local test
make test

# Build docker
make docker

# Config
mv hack/set-default.sh.tmpl hack/set-default.sh
# Change the config in hack/set-default.sh accordingly.

# Run marathon utils scripts
hack/marathon_utils.sh -h

# List all apps or a particular app
hack/marathon_utils.sh -a list 
hack/marathon_utils.sh -a list  -n /zkweb

# Create an app
hack/marathon_utils.sh -a create -n apps/zk_web/zk_web.json.tmpl

# Delete an app
hack/marathon_utils.sh -a delete -n /zkweb
```

# Predefined Supported Apps

* ZKWEB: web interface for zookeeper

```
hack/marathon_utils.sh -a create -n apps/zk_web/zk_web.json.tmpl
```


* HDFS

```
hack/marathon_utils.sh -a create -n apps/hdfs/hdfs_group.json.tmpl -i 4 -m 2048
```

* HBASE

```
hack/marathon_utils.sh -a create -n apps/hbase/hbase_group.json.tmpl -i 4 -m 2048
```

* SparkJupyter: Python Notebook with pyspark (spark is driven by mesos)

```
hack/marathon_utils.sh -a create -n apps/spark_jupyter/spark_jupyter.json.tmpl \
  -c '{"app_name": "sparkjupytertest", "more_conf": "--driver-memory 1g --conf spark.executor.memory=2g"}' 
```

* Chronos: Distributed cron job manager.

```
hack/marathon_utils.sh -a create -n apps/chronos/chronos.json.tmpl \
  -c '{"app_name": "chronosdev"}' -i 3 -m 768
```

* etcd: A distributed consistent key-value store for shared configuration and service discovery

```
export CLUSTER_SIZE=3
export DISCOVERTY=$(curl https://discovery.etcd.io/new?size=$CLUSTER_SIZE)
hack/marathon_utils.sh -a create -n apps/etcd/etcd.json.tmpl \
  -c '{"app_name": "etcdtest", "cluster_name": "etcdtest", "discovery": "'$DISCOVERTY'"}' \
  -i $CLUSTER_SIZE -m 1024
```

* Elasticsearch

```
export ETCD_SERVER="http://your.etcd.com:2379"

# Create es cluster without addtional client nodes.
hack/marathon_utils.sh -a create -n apps/elasticsearch/es_group.json.tmpl \
    -c '{"group_name": "estest", "es_cluster_name": "estest", "etcd_server": "'$ETCD_SERVER'"}' \
    -i 3 -m 1024

# Create es cluster with addtional client nodes.
hack/marathon_utils.sh -a create -n apps/elasticsearch/es_group.json.tmpl \
    -c '{"group_name": "estest", "es_cluster_name": "estest", "client_instances": 1, "etcd_server": "'$ETCD_SERVER'"}' \
    -i 3 -m 1024
```

* Hive server

```
export AWS_ACCESS_KEY_ID="your_aws_access_key"
export AWS_SECRET_ACCESS_KEY="your_aws_secret_key"
hack/marathon_utils.sh -a create -n apps/hive/metastore.json.tmpl -i 1 -m 2048 \
  -c '{"aws_access_key_id": "'$AWS_ACCESS_KEY_ID'", "aws_secret_access_key": "'$AWS_SECRET_ACCESS_KEY'"}'
hack/marathon_utils.sh -a create -n apps/hive/hiveserver2.json.tmpl -i 1 -m 2048 \
  -c '{"aws_access_key_id": "'$AWS_ACCESS_KEY_ID'", "aws_secret_access_key": "'$AWS_SECRET_ACCESS_KEY'"}'
```


* Presto Cluster

```
# You need to sync your catalog config in etcd first. Or basic catalog will
# applied

export ETCD_SERVER="http://your.etcd.com:2379"
hack/marathon_utils.sh -a create -n apps/presto/presto_group.json.tmpl \
    -c '{"group_name": "test", "etcd_server": "'$ETCD_SERVER'"}' -i 3 -m 2048

# Start airpal web ui for presto.
hack/marathon_utils.sh -a create -n apps/presto/presto_airpal.json.tmpl -m 2048
```

* Mysql: For test purpose, we never suggest deploy mysql in mesos.

```
hack/marathon_utils.sh -a create -n apps/mysql/msyql.json.tmpl
```
