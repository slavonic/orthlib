'''
Recursively scans a directory and re-writes each file as utf-8 text file,
assuming it is in the text cp1251 encoding...
'''
import os


def kill1251(fname):
    with open(fname, 'rb') as f:
        text = f.read()
    text = text.decode('cp1251').encode('utf-8')
    with open(fname, 'wb') as f:
        f.write(text)
    print('Processing:', fname)

def rc_kill1251(dirname):
    for x in os.listdir(dirname):
        path = os.path.join(dirname, x)
        if os.path.isdir(path):
            rc_kill1251(path)
        elif os.path.isfile(path):
            kill1251(path)

if __name__ == '__main__':
    import fire
    fire.Fire(rc_kill1251)
