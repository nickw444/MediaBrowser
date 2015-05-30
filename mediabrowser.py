import os
from flask import Flask, render_template, send_file, request, after_this_request, redirect, url_for, safe_join
import re

from config import MAX_FOLDER_DL_SIZE_BYTES, IGNORE_FILES, ROOT_PATHS

app = Flask(__name__)

def get_size(start_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

import zipfile
def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(
                os.path.join(root, file), 
                arcname=os.path.join(root.replace(path, ''), file)
            )

@app.route('/')
def index():
    return render_template('index.html', items=ROOT_PATHS)

@app.route('/<int:id>/<path:path>')
@app.route('/<int:id>/')
def browse(id, path=''):
    path = path.replace('../', '')
    real_path = safe_join(ROOT_PATHS[id].path, path)

    items = {
        'dirs': [],
        'files': [],
    }

    if os.path.isfile(real_path):
        # If it's a file, send it.
        return send_file(real_path, 
            as_attachment=request.args.get('download'))
    else:
        if request.args.get('download'):
            folder_size = get_size(real_path)
            if folder_size > MAX_FOLDER_DL_SIZE_BYTES:
                print("TOO LARGE YO")
                return "Folder too large. Exceeds maximum dl of {} '\
                'bytes".format(MAX_FOLDER_DL_SIZE_BYTES)

            print("Request for DL")
            zipfilename = 'static/zips/{}.zip'.format(
                os.path.basename(os.path.dirname(real_path))
            )
            zipf = zipfile.ZipFile(zipfilename, 'w')
            zipdir(real_path, zipf)
            zipf.close()

            @after_this_request
            def after(r):
                os.unlink(zipfilename)
                print("Done!")
                return r    

            return send_file(zipfilename, 
                attachment_filename=os.path.basename(os.path.dirname(real_path)))

            return "DL"
        else:
            for f in os.listdir(real_path):
                if not re.match(IGNORE_FILES, f):
                    
                    if os.path.isdir(os.path.join(real_path, f)):
                        item = (f, os.path.join(path, f) + '/')
                        items['dirs'].append(item)
                    else:
                        item = (f, os.path.join(path, f))
                        items['files'].append(item)

            return render_template('browse.html', id=id, items=items)

    return "lel"

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == 'meinheld':
        from meinheld import server
        server.listen(("0.0.0.0", 8082))
        server.run(app)
    else:
        app.debug = True
        app.run()
