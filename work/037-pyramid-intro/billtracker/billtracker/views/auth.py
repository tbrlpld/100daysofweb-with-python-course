from pyramid.httpexceptions import HTTPFound
from pyramid.security import (
    remember,
    forget,
)
from pyramid.view import (
    forbidden_view_config,
    view_config,
)


from billtracker.data import repository


@view_config(
    route_name="login",
    renderer="../templates/login.pt",
)
def login(request):
    if request.user is not None:
        raise HTTPFound(location="/")

    next_url = request.params.get("next", request.referrer)
    if not next_url or next_url == "/login":
        next_url = "/"
    message = ""
    login = ""
    if "form.submitted" in request.params:
        login = request.params["login"]
        password = request.params["password"]
        # Login needs to be the ID
        # (this is just because I dont have to name look up yet)
        user = repository.get_user_by_email(login)
        if user is not None and user.check_password(password):
            headers = remember(request, user.id)
            return HTTPFound(location=next_url, headers=headers)
        message = "Login Failed"

    return {
        "message": message,
        "url": request.route_url("login"),
        "next_url": next_url,
        "login": login,
    }


@view_config(route_name="logout")
def logout(request):
    headers = forget(request)
    next_url = request.route_url("login")
    return HTTPFound(location=next_url, headers=headers)


@forbidden_view_config()
def forbidden_view(request):
    next_url = request.route_url("login", _query={"next": request.url})
    return HTTPFound(location=next_url)
