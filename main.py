def function_cicd(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request):HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>` .
    """

    request_json = request.get_json()
    if request.args and 'message' in request.args:
        return request.args.get('message')
    elif request_json and 'message' in request_json:
        return request_json['message']
    else:
        return f'Function - 1 with v1.0 with CI/CD Pipeline'




#def function_cicd(request):
#    """Responds to any HTTP request.
#    Args:
#        request (flask.Request):HTTP request object.
#    Returns:
#        The response text or any set of values that can be turned into a
#        Response object using
#        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>` .
#    """
#
#    request_json = request.get_json()
#    if request.args and 'message' in request.args:
#        return request.args.get('message')
#    elif request_json and 'message' in request_json:
#        return request_json['message']
#    else:
#        return f'Function - 1 with v1.0 with CI/CD Pipeline'
