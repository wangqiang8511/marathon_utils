#!/usr/bin/env sh

PROJECT_HOME="$(cd "$(dirname "$0")"/..; pwd)"

. $PROJECT_HOME/VERSION
. $PROJECT_HOME/hack/set-default.sh

docker run -it --rm \
  -e MARATHON_MASTER=$MARATHON_MASTER \
  $REPO:$VERSION \
  $@
