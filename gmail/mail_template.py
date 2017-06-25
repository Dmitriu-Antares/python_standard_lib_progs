import os

def get_temp_path(path):
    file_path=os.path.join(os.getcwd(),path)
    if not os.path.isfile(file_path):
        raise Exception('It`s not valid path')
    else:
        return file_path

def get_temp(path):
    file_path=get_temp_path(path)
    return open(file_path).read()

def renderer(template,ctx):
    return template.format(**ctx)
