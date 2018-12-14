import flask
import os
#import sys
import tempfile
from flask import request, jsonify
from models import Apk, FastApkVectors
import subprocess
#from subprocess import PIPE
#import AndroBugs_MassiveAnalysis

ANDROBUGS_DIR = "Your Path to AndroBugs_Framework directory"
ANDROBUGS_EXE = "AndroBugs_MassiveAnalysis.py"
ANALYZE_ENGINE_BUILD = 1
ANALYZE_TAG = "AB-TAG"
OUTPUT_DIR = "/tmp/out"

def index():
    """
    Current home page returns all analyzed APKs
    :return: all APKs
    """
    apks = Apk.objects.all()
    return flask.render_template('index.html', apks=apks)


def update(id):
    """
    Updates the comment field from the index view
    :return: Success or failure
    """

    try:
        comment = request.form['comment']
        Apk.objects(id = id).update(
            set__comment = comment
        )
        return jsonify(message="Update successful.")
    except Exception as e:
        return jsonify(message=e.message), 500


def delete(id):
    """
    Delete an existing apk record
    :return: Success or failure
    """
    try:
        Apk.objects(id = id).delete()
        return jsonify(message="Delete successful.")
    except Exception as e:
        return jsonify(message=e.message), 500

    
def detail(id):
    """
    Displays apks with same name
    :return: the view template
    """
    apk = Apk.objects.get(id=id)
    print "***********************"
    print apk.details
    return flask.render_template('detail.html', apk=apk, package_name=apk.package_name)


def level(name):
    """
    Displays apks containing vulnerabilities of a certain level
    :param name: package name of apk clicked
    :return: level template
    """
    apks = Apk.objects(package_name=name)
    return flask.render_template('level.html', apks=apks, package_name=name)


def vector(vector_title):
    vector_title = vector_title.encode('utf-8')
    vectors = FastApkVectors.objects(vector=vector_title)
    apks = []
    for apk in Apk.objects:
        if(vector_title in getattr(apk, "details").keys()):
            apks.append(apk)
    return flask.render_template('vector.html', apks=apks, vectors=vectors, vector_name=vector_title)

def upload():
    """
    Upload an apk and process with the androbugs massive analyzer.
    Customize your path to uploads and androbugs executable path and arguments
    :return: success or failure
    """
    if request.method == 'POST':
        f = request.files.get('file')
        # Create tmp directory to not evaluate an ever-growing directory
        upload_dir = tempfile.mkdtemp()
        filepath = os.path.join(upload_dir, f.filename)
        f.save(filepath)

        # Execute androbugs
        """
        You could import or run subprocess,  Import example below
    
        sys.argv += ['-d' + UPLOAD_DIR, '-b' + str(ANALYZE_ENGINE_BUILD), '-t' + str(ANALYZE_TAG),
                     '-o' + OUTPUT_DIR]
        AndroBugs_MassiveAnalysis.main()
        """

        try:
            process = subprocess.call(['python', ANDROBUGS_EXE, '-d', upload_dir, '-b', str(ANALYZE_ENGINE_BUILD), '-t',
                                       str(ANALYZE_TAG), '-o', OUTPUT_DIR], cwd=ANDROBUGS_DIR)
        except Exception as e:
            return jsonify(message=e.message), 500


        return jsonify(success=1)