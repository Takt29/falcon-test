# -*- Coding: utf-8 -*-

import falcon
import json


def create_json_resp(d: dict) -> str:
    return json.dumps(d, indent=2)


class SampleResource(object):
    @staticmethod
    def on_get(req, resp):
        resp.body = create_json_resp({
            "title": "hello world",
            "sentence": "This is a test program."
        })
        resp.status = falcon.HTTP_200 # デフォルトで200なので無くて良い

wsgi_app = falcon.API()
app.add_route("/hello", SampleResource())

if __name__ == "__main__":
    from wsgiref import simple_server
    
    httpd = simple_server.make_server("localhost", 8000, app)
    httpd.serve_forever()


"""
def wsgi_app(environ, start_response):

    method = environ.get('REQUEST_METHOD')

    if method == 'POST':
        wsgi_input = environ['wsgi.input']
        content_length = int(environ.get('CONTENT_LENGTH', 0))
        request_body = wsgi_input.read(content_length).decode('UTF-8')
        form = json.loads(request_body)

        print(form['events'])
        print('events' in form)
        
        if 'events' in form:
            for event in form['events']:
                callback.process_event(event)
        else:
            callback.post_error(None, "Can't find events.");

    
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    response_body = 'Success'
    yield response_body.encode()

if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    httpd = make_server('localhost', 5555, wsgi_app)
    httpd.serve_forever()
    
"""