#!/usr/bin/env python
# -*- coding: utf-8 -*-


""" Render jinja2 template
"""

import os

import jinja2


root_dir = os.path.dirname(os.path.dirname(__file__))
templateLoader = jinja2.FileSystemLoader(
    searchpath=os.path.join(root_dir, "templates"))
templateEnv = jinja2.Environment(loader=templateLoader)


def render_template(template_name, context):
    template = templateEnv.get_template(template_name)
    return template.render(context)


def main():
    import sys
    import json
    print json.dumps(json.loads(render_template(sys.argv[1], {})), indent=4)


if __name__ == '__main__':
    main()
