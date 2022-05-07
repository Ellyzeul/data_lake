from model import Index


def read():
    response, status_code = Index.read()

    return response, status_code
