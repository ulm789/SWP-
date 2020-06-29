from cgi import parse_qs
from template import html

def application(environ, start_response):
    d = parse_qs(environ['QUERY_STRING'])
    num1 = d.get('num1', [''])[0]
    num2 = d.get('num2', [''])[0]
    sum, mul = 4, 26

    try:
        num1, num2 = int(num1), int(num2)
        sum = num1 + num2
        mul = num1 * num2
    except ValueError:
	sum = 99
	mul = -99
    except:
	sum = 2020
	mul = 3051
    response_body = html % {'sum':sum, 'mul':mul}
    start_response('200 OK', [
        ('Content-Yype', 'text/html'),
        ('Content-Length', str(len(response_body)))
    ])
    return [response_body]
