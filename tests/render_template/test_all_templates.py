# Test all templates in templates folder


import os
import json

from marathon_utils import render_template


def test_all_templates():
    project_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    app_templates_folder = os.path.join(
        os.path.join(project_dir, "templates"), "apps")
    print app_templates_folder
    abs_template_folder = os.path.split(app_templates_folder)[0]
    for root, dirs, files in os.walk(app_templates_folder):
        rel_dir = root[len(abs_template_folder)+1:]
        for name in files:
            template_name = os.path.join(rel_dir, name)
            if template_name.endswith("tmpl"):
                try:
                    json.loads(
                        render_template.render_template(template_name, {}))
                except Exception as e:
                    assert False, "%s: %s" % (template_name, e)
