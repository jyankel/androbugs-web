from flask_mongoengine import MongoEngine
from mongoengine import DateTimeField, FloatField, IntField, StringField, DictField, ListField

db = MongoEngine()


class Apk(db.Document):
    '''
    Class defining APKs
    '''
    package_name = StringField(required=True)
    time_starting_analyze = DateTimeField(required=True)
    apk_filepath_absolute = StringField(required=True)
    file_md5 = StringField(required=True)
    vector_total_count = IntField(required=True)
    time_finish_analyze = DictField()
    analyze_tag = StringField()
    platform = StringField()
    time_loading_vm = FloatField()
    details = DictField()
    time_analyze = FloatField()
    targetSdk = IntField()
    file_sha256 = StringField()
    package_version_code = IntField()
    signature_unique_analyze = StringField()
    analyze_mode = StringField()
    apk_file_size = FloatField()
    analyze_engine_build = IntField()
    package_version_name = IntField()
    minSdk = IntField()
    file_sha1 = StringField()
    file_sha512 = StringField()
    time_total = FloatField()
    analyze_status = StringField()
    comment = StringField()
    devices = ListField()

    meta = {
        'collection': 'AnalyzeSuccessResults',
        'auto_create_index': False
    }

class FastApkVectors(db.Document):
    '''
    FastApkVectors
    '''
    package_version_code = IntField()
    analyze_engine_build = IntField()
    analyze_mode = StringField()
    package_name = StringField()
    level = StringField()
    file_sha512 = StringField()
    vector = StringField()
    analyze_tag = StringField()
    signature_unique_analyze = StringField()

    meta = {
        'collection': 'AnalyzeSuccessResultsFastSearch',
        'auto_create_index': False
    }
