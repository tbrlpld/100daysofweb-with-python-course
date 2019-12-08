# -*- coding: utf-8 -*-

"""Define the responder api instance."""

import os

import responder

package_dir = os.path.dirname(os.path.abspath(__file__))
static_dir = os.path.join(package_dir, "static")
template_dir = os.path.join(package_dir, "templates")

api = responder.API(
    static_dir=static_dir,
    templates_dir=template_dir,
    debug=True,
)
