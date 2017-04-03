def app(environ, start_response):
    status = '200 OK'
    headers = [ ('Content-Type', 'text/plain')]
    request = environ[QUERY_STRING]
    body = [str(i+'\n','ascii') for i in request.split('&')]
    start_response(status, headers)
    return [body]
    
