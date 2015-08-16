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
