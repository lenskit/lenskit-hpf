"""
Little utiility library for package management.
"""

import re
import warnings
from pathlib import Path
from subprocess import run, PIPE, DEVNULL

_pkg_path = Path(__file__).parent

def gitify_version(tagged):
    """
    Update a version string to include the Git version number, if feasible.
    """
    parent = _pkg_path.parent
    dotgit = parent / '.git'
    if not dotgit.exists():
        # not a git version, return
        return tagged
    
    cmd = ['git', 'describe', '--tags', '--always']
    cp = run(cmd, stdout=PIPE, stdin=DEVNULL, check=True, cwd=_pkg_path)
    descr = cp.stdout.decode('ascii').strip()

    dm = re.match(r'^v?(?:(\d+(?:\.\d+)*)-(\d+)-)?([0-9a-fA-F]+)', descr)
    if not dm:
        warnings.warn(f'unparsable description ‘{descr}’')
        return tagged + '.dev0'
    
    ver = dm.group(1)
    n = dm.group(2)
    hash = dm.group(3)
    if ver == tagged:
        warnings.warn(f'version {tagged} is tagged')
    if n:
        return f'{tagged}.dev{n}+{hash}'
    else:
        return f'{tagged}.dev0+{hash}'


if __name__ == '__main__':
    from . import __version__, __name__ as pkn
    print(pkn, 'version', __version__)