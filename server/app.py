# -*- coding: utf-8 -*- 
import os, sys
import logging
import flask
import optparse
import tornado.wsgi
import tornado.httpserver
from werkzeug import secure_filename 
import draw_roc


TEMPLATE_DIRNAME = os.path.abspath('../client')
UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set(['txt']) 

app = flask.Flask(__name__, template_folder=TEMPLATE_DIRNAME) 
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 


def allowed_file(filename): 
   return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS 

def get_filename(filename):
   return filename.rsplit('.', 1)[0]

@app.route('/', methods=['GET', 'POST']) 
def upload_file(): 
   print 'update file .......'
   if flask.request.method == 'POST': 
      file = flask.request.files['file'] 
      if file and allowed_file(file.filename): 
         filename = secure_filename(file.filename) 
         name = get_filename(filename)
         print name
         file.save(os.path.join(UPLOAD_FOLDER, filename)) 
         #roc process
         map_val = draw_roc.process_test(os.path.join(UPLOAD_FOLDER, filename), name)
         #get roc iamge url
         file_url_roc = flask.url_for('static', filename=name+'_roc.png') 
         file_url_roc2 = flask.url_for('static', filename=name+'_roc2.png') 
         #print file_url
         result = [file_url_roc, file_url_roc2, str(map_val)]
         return flask.render_template('index.html', has_result=True, result=result) 
   else:
      return flask.render_template('index.html', has_result=False) 

def start_tornado(app, port=5000):
    http_server = tornado.httpserver.HTTPServer(tornado.wsgi.WSGIContainer(app))
    http_server.listen(port)
    print("Tornado server starting on port {}".format(port))
    tornado.ioloop.IOLoop.instance().start()

def start_from_terminal(app):
    parser = optparse.OptionParser()
    parser.add_option('-d', '--debug', help="enable debug mode", action="store_true", default=False)
    parser.add_option('-p', '--port', help="which port to serve content on", type='int', default=8080)
    parser.add_option('-g', '--gpu', help="use gpu mode", action="store_true", default=False)

    opts, args = parser.parse_args()
 
    if opts.debug:
        app.run(debug=True, host='0.0.0.0', port=opts.port)
    else:
        start_tornado(app, opts.port)

if __name__ == '__main__': 
    logging.getLogger().setLevel(logging.INFO)
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    start_from_terminal(app) 



