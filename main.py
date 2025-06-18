from selfie.wsgi import application

if __name__ == "__main__":
    from wsgiref.simple_server import make_server
    make_server("0.0.0.0", 8000, application).serve_forever()
