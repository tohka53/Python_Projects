from spyne import Application, rpc, ServiceBase, Integer, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

class HelloService(ServiceBase):
    @rpc(Integer, Unicode, _returns=Unicode)
    def say_hello(ctx, times, name):
        return 'Hello, %s! ' % name * times

application = Application([HelloService], tns='my.namespace.com', in_protocol=Soap11(validator='lxml'), out_protocol=Soap11())

wsgi_application = WsgiApplication(application)

if __name__ == '__main__':
    import logging
    from wsgiref.simple_server import make_server
    logging.basicConfig(level=logging.DEBUG)
    server = make_server('0.0.0.0', 8000, wsgi_application)
    server.serve_forever()
