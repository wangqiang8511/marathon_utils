import os
import json
import argparse

import requests

from marathon_utils.render_template import render_template


marathon_master = os.environ.get("MARATHON_MASTER", "http://localhost:8080")


def post_app(app_json_data):
    print app_json_data
    headers = {}
    headers["Content-Type"] = "application/json"
    headers["Accept"] = "application/json"
    url = "%s/v2/apps" % marathon_master
    r = requests.post(url, data=app_json_data, headers=headers)
    if r.status_code >= 400:
        print "something goes wrong"
        print r.text
        return
    print json.dumps(r.json(), indent=4)
    return True


def delete_app(args):
    headers = {}
    headers["Content-Type"] = "application/json"
    headers["Accept"] = "application/json"
    if args.name == "all":
        print "Should specify correct app name for deleting"
        return False
    url = "%s/v2/apps/%s" % (marathon_master, args.name)
    r = requests.delete(url, headers=headers)
    if r.status_code >= 400:
        print "something goes wrong"
        print r.text
        return False
    print json.dumps(r.json(), indent=4)
    return True


def list_apps(args):
    headers = {}
    headers["Content-Type"] = "application/json"
    headers["Accept"] = "application/json"
    if args.name == "all":
        url = "%s/v2/apps/" % (marathon_master)
    else:
        url = "%s/v2/apps/%s" % (marathon_master, args.name)
    r = requests.get(url, headers=headers)
    if r.status_code >= 400:
        print "something goes wrong"
        print r.text
        return False
    print json.dumps(r.json(), indent=4)
    return True


def config_to_context(config):
    try:
        d = json.loads(config)
        if not d:
            d = {}
    except:
        d = {}
    return d


def load_tempate(name, context):
    return render_template(name, context)


def create_app(args):
    context = {}
    context["instances"] = args.instances
    context["cpus"] = args.cpus
    context["mem"] = args.mem
    config = config_to_context(args.config)
    context.update(config)
    return post_app(load_tempate(args.name, context))


def perform_action(args):
    action = args.action.lower()
    if action not in ["create", "delete", "list"]:
        return False
    if action == "create":
        return create_app(args)
    if action == "delete":
        return delete_app(args)
    if action == "list":
        return list_apps(args)
    return True


def main():
    import sys
    parser = argparse.ArgumentParser(description='mesos marathon')
    parser.add_argument("-a", "--action",
                        required=True, help="action create|delete|list")
    parser.add_argument("-n", "--name", default="all",
                        help="name of tempate/app")
    parser.add_argument("-i", "--instances", default=1,
                        help="number of instances")
    parser.add_argument("-u", "--cpus", default="0.1",
                        help="cpu usage")
    parser.add_argument("-m", "--mem", default="512",
                        help="memory usage")
    parser.add_argument("-c", "--config", default="", help="more configs")
    args = parser.parse_args(sys.argv[1:])
    if perform_action(args):
        sys.exit(0)
    sys.exit(1)


if __name__ == '__main__':
    main()
