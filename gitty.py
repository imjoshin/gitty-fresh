import subprocess
import sys

replacements = {
    'git': 'gittyfresh',
    'push': 'yeet',
}

def replace(text, mapping):
    ret = text
    for word in mapping:
        ret = ret.replace(word, mapping[word])
    return ret

def encode(text):
    return replace(text, replacements)

def decode(text):
    return replace(text, {v: k for k, v in replacements.iteritems()})

def git(args):
    popen = subprocess.Popen(['git'] + args, stdout=subprocess.PIPE, universal_newlines=True)
    for stdout_line in iter(popen.stdout.readline, ""):
        yield stdout_line

    popen.stdout.close()
    return_code = popen.wait()

    if return_code:
        raise subprocess.CalledProcessError(return_code, cmd)

def main():
    git_args = [decode(arg) for arg in sys.argv[1:]]
    for line in git(git_args):
        print(encode(line)),

if __name__ == "__main__":
    main()
