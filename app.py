import os, json
from datetime import datetime
from flask import Flask, request, flash, url_for, redirect, render_template, abort, send_from_directory, send_file, make_response
from werkzeug import secure_filename
import shutil
import base64 as b
import p_fmodules.load_epg as mle


app = Flask(__name__)
app.config.from_pyfile('flaskapp.cfg')
ALLOWED_EXTENSIONS = set(['zip', 'txt'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/reloadepg", methods=['GET','POST'])
def reload_epg():
    mle.reload_epg()
    return json.dumps({'RESP':'SUCCESS'}) 

# @app.route("/getepg", methods=['POST',])
# def get_epg():
#     if request.method == 'POST':
#         # print(request.headers)
#  
#         tv_ids = request.headers['tv_ids']
#  
#         return json.dumps(get_epg(tv_ids.split("#"))) 
# #         return json.dumps(mle.get_epg(tv_ids.split("#"))) 
#     else:
#         return json.dumps({'EPG_ERROR':'USE_POST'})
    
@app.route("/getepg_all", methods=['GET',])
def get_epg_all():
    if request.method == 'GET':
        out = json.dumps(mle.get_epg_all())
#         print(out)
        return out 
    else:
        return json.dumps({'EPG_ERROR':'USE_POST'})


# @app.route('/<path:resource>')
# def serveStaticResource(resource):
#     return send_from_directory('static/', resource)
# 
# @app.route("/test")
# def test():
#     return "<strong>It's Alive!</strong>"
# 
# @app.route("/getepg", methods=['POST',])
# def get_epg():
#     if request.method == 'POST':
#         # print(request.headers)
# 
#         tv_ids = request.headers['tv_ids']
# 
#         return json.dumps(get_epg(tv_ids.split("#"))) 
# #         return json.dumps(mle.get_epg(tv_ids.split("#"))) 
#     else:
#         return json.dumps({'EPG_ERROR':'USE_POST'})
# 
# @app.route("/getepg_all", methods=['GET',])
# def get_epg_all():
#     if request.method == 'GET':
#         return json.dumps(mle.get_epg_all()) 
#     else:
#         return json.dumps({'EPG_ERROR':'USE_POST'})
# 
# 
# @app.route("/reloadepg", methods=['GET','POST'])
# def reload_epg():
#     mle.load_epg()
#     return json.dumps({'RESP':'SUCCESS'}) 
# 
# @app.route("/load_image", methods=['GET', 'POST'])
# def rli():
#     # print("********************************* ARGS ********************")
#     _url = request.args.get('img_url', 'NULL')
#     # print(_url)
#     if 'NULL' not in _url:
#         # print("********************************* BASE64 ********************")
#         _url = b.b64decode(_url).decode("utf-8") 
#         resp = piu.load_image(_url)
#         if resp.status_code == 200:
#             resp = make_response(resp.content)
#             resp.headers['Content-Type'] = 'image/jpeg'
#             # resp.headers['Content-Disposition'] = 'attachment; filename=img.jpg'
#             return resp            
# 
#     return json.dumps({'RESP':'NULL'}) 

#############################################################################################

# from apscheduler.schedulers.background import BackgroundScheduler
# from datetime import datetime
# 
# def _schedule_load_epg():
#     print("LOADING EPG AT:: ", datetime.now())
#     mle.load_epg()
# 
# scheduler = BackgroundScheduler()
# 
# job = scheduler.add_job(_schedule_load_epg, 'cron', hour=6, minute=10, id='LOAD_EPG', max_instances=1, replace_existing=True)
# # job = scheduler.add_job(_schedule_load_epg, 'cron', hour=6, minute=0, id='LOAD_EPG', max_instances=1, replace_existing=True)
# 
# scheduler.start()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
