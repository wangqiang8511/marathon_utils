#!/bin/bash

NUM_INSTANCES=${NUM_INSTANCES:-1}
CPUS=${CPUS:-0.1}
MEM=${MEM:-512}
CLUSTER_NAME=${CLUSTER_NAME:-mes0}
ROOT_DOMAIN=${ROOT_DOMAIN:-razerdata.com}
MARATHON_HOST=${MARATHON_HOST:-http://master0.mes0.razerdata.com:8080}

tmpl=$(cat $1)

app=$(eval echo $tmpl)

curl -XPOST \
	-H 'Content-Type:application/json' \
	-H 'Accept: application/json' \
	--data "$app" \
	$MARATHON_HOST/v2/apps
