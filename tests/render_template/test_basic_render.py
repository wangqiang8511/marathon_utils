# Test Basic Rendering

import json

from marathon_utils import render_template


def test_basic_render():
    context = {"instances": 1}
    tmpl_res = render_template.render_template(
        "apps/tests/test_basic.json.tmpl", context)
    data = json.loads(tmpl_res)
    assert int(data["instances"]) == 1
