import requests
import os, tempfile, subprocess, re


def download(target, urls='orthlib.txt'):
    with open(urls) as f:
        lines = [l.strip() for l in f]
    lines = [l for l in lines if l and not l.startswith('#')]

    for url in lines:
        mtc = re.match(r'(https?://[^/]+)/(.*\.rar)$', url)
        if mtc is None:
            raise ValueError('unexpected URL: %r' % url)

        path = os.path.join(target, mtc.group(2))
        print('Processing:', path)
        os.makedirs(path, exist_ok=True)

        fname = tempfile.mktemp(suffix='.rar')
        r = requests.get(url)
        with open(fname, 'wb') as f:
            f.write(r.content)
        subprocess.check_call([
            'unrar', 'x', fname, path
        ])
        os.unlink(fname)

if __name__ == '__main__':
    import fire
    fire.Fire(download)