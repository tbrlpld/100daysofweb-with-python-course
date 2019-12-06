import responder

api = responder.API()


def main():
    api.run()


@api.route("/")
def hello(_, response: responder.Response) -> None:
    response.content = "Hello World"


if __name__ == "__main__":
    main()
