#!/usr/bin/env python
"""
Very simple HTTP server in python.
Usage::
    ./dummy-web-server.py [<port>]
Send a GET request::
    curl http://localhost
Send a HEAD request::
    curl -I http://localhost
Send a POST request::
    curl -d "foo=bar&bin=baz" http://localhost
"""
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
import urlparse
from recommend import recommend
import urllib



class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        #print self.rfile.readline()
        f = open("./index.html")
        html = f.read();
        html = html.replace("###value###", "");
        html = html.replace("###Panels###", "");
        f.close();
        f = open("./songs.html")
        songs = f.read()
        f.close();
        html = html.replace("###songsong###", songs)
        self.wfile.write(html);
        

    def do_HEAD(self):
        self._set_headers()
        
    def do_POST(self):
        self._set_headers()
        print "in post method"
        self.data_string = self.rfile.read(int(self.headers['Content-Length']))
        instring =  self.data_string;
        inf = urlparse.parse_qs(instring)["input"][0]
        f = open('./index.html')
        html = f.read();
        f.close()
        f = open('./panel.html')
        panelM = f.read();
        f.close();

        imgs = ["https://pbs.twimg.com/profile_images/612578451694850048/c6B-UB2E.jpg",
                "https://ichef.bbci.co.uk/images/ic/256x256/p01bqf55.jpg",
                "https://pbs.twimg.com/profile_images/645575329705238529/OztmM324.jpg"
                ]


        print "Query", inf 
        results = recommend(inf)
        print results
        panels = "";
        for i in range(3):
            panel = panelM
            panel = panel.replace("###img###", imgs[i])
            panel = panel.replace("###Rank###", "Rank #"+str(i+1))
            panel = panel.replace("###Song###", "Song Name: "+results["similar_song"][i])
            panel = panel.replace("###Art###", "Artist Name: "+results["similar_artist"][i])
            query = {
                'q':results["similar_song"][i]+" "+results["similar_artist"][i]
            }
            panel = panel.replace("###url###", "https://www.youtube.com/results?search_query="+urllib.urlencode(query)[2:]);
            panels += panel
        html = html.replace("###value###", inf);
        html = html.replace("###Panels###", panels)

        f = open("./songs.html")
        songs = f.read()
        f.close();
        html = html.replace("###songsong###", songs)


        self.wfile.write(html);
        return
        
def run(server_class=HTTPServer, handler_class=S, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd...'
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
