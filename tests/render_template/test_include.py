# Test templates with include

import json

from marathon_utils import render_template


def test_include():
    tmpl_res = render_template.render_template(
        "apps/tests/test_docker.json.tmpl", {})
    print tmpl_res
    data = json.loads(tmpl_res)
    assert len(data["healthChecks"]) == 1
