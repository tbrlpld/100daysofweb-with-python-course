from contextlib import redirect_stdout
import io
import json
import tempfile

import pycodestyle


TEMPFILE = tempfile.NamedTemporaryFile(dir="/tmp")


def lambda_handler(event, context):
    code = event.get("code")
    output = ""

    if code:
        with open(TEMPFILE.name, "w") as f:
            f.write(code + "\n")
            f.seek(0)

            pep = pycodestyle.Checker(f.name)

            capture = io.StringIO()
            with redirect_stdout(capture):
                pep.check_all()

            output = capture.getvalue()

    return {
        "statusCode": 200,
        "body": json.dumps(output),
    }


# if __name__ == '__main__':
#     print("OK:")
#     print(lambda_handler({"code": "print('something')"}, None))
#     print("")
#     print("NOK:")
#     print(lambda_handler({"code": "  print('something')"}, None))
