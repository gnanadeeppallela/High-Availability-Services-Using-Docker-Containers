import sys
from StringIO import StringIO
import datetime
from SimpleHTTPServer import SimpleHTTPRequestHandler, test


class MyHTTPHandler(SimpleHTTPRequestHandler):

    __state__ = {}
    __request_start = 1
    __request_list__ = []

    def list_directory(self, path):
        """
        """

        f = StringIO()
        req_no = self.__state__.get('request_no')
        if req_no is None:
            req_no = self.__request_start
        else:
            req_no += 1

        self.__state__['request_no'] = req_no

        req_date = datetime.datetime.now().strftime("%c")
        client_detail = "%s:%s" % (self.client_address[0],
                                   str(self.client_address[1]))

        f.write('<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">')
        f.write("<html>\n<body>\n<pre>")
        f.write("Request No: %s\n" % req_no)
        f.write("Client details: %s\n" % client_detail)
        f.write("Date: %s\n\n" % req_date)
        f.write("<hr>Previous requests:\n%s" % "\n".join(
            self.__request_list__))
        f.write("</pr>\n<hr>\n</body>\n</html>\n")
        length = f.tell()
        f.seek(0)

        self.send_response(200)
        encoding = sys.getfilesystemencoding()
        self.send_header("Content-type", "text/html; charset=%s" % encoding)
        self.send_header("Content-Length", str(length))
        self.end_headers()
        self.__request_list__.append("Req No: %s: Client:%s Date: %s" % (
            req_no, client_detail, req_date))
        return f

if __name__ == '__main__':
    test(HandlerClass=MyHTTPHandler)

