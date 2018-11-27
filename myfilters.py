from androbugs_web import app

@app.template_filter('vector_in_apk')
def is_any(vector_dict=None, search=""):
    if(vector_dict[search]['count'] > 0):
        return True
    return False
