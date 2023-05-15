import subprocess

def bash(command, *, dry_run=False):

    if dry_run:
        print(command)
        return

    res = subprocess.run(command, close_fds=True, stdout=subprocess.PIPE, shell=True)
    output = res.stdout.decode()
    return output
