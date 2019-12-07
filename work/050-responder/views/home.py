# -*- coding: utf-8 -*-

"""Define landing page views."""

import responder

from api import api


@api.route("/")
def index(_, response: responder.Response) -> None:
    response.html = api.template("/index.html", recreator="Tibor")
