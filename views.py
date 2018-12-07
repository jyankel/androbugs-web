import flask
from flask import request, jsonify
from models import Apk, FastApkVectors


def index():
    '''
    Current home page returns all analyzed APKs
    :return: all APKs
    '''
    apks = Apk.objects.all()
    return flask.render_template('index.html', apks=apks)


def update():
    '''
    Updates the comment field from the index view
    :return: Success or failure
    '''
    comment = request.form['comment']
    id = request.form['id']
    Apk.objects(id = id).update(
        set__comment = comment
    )

    return jsonify('success')


def delete(id):
    '''
    Delete an existing apk record
    :return: Success or failure
    '''
    Apk.objects(id = id).delete()
    return index()

def detail(md5):
    '''
    Displays apks with same name
    :return: the view template
    '''
    apk = Apk.objects.get(file_md5=md5)
    print "***********************"
    print apk.details
    return flask.render_template('detail.html', apk=apk, package_name=apk.package_name)


def level(name):
    '''
    Displays apks containing vulnerabilities of a certain level
    :param name: package name of apk clicked
    :return: level template
    '''
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
