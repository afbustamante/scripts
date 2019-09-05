#/usr/bin/python
import re
import subprocess

regex = r"^(master|develop|(feature|release|hotfix)\/[a-z0-9_\.\-\/]+)$"
cmd_branch_name = subprocess.run(["git", "rev-parse", "--abbrev-ref", "HEAD"], capture_output=True)
branch_name = str(cmd_branch_name.stdout, 'utf-8')

#print(branch_name)

if not re.match(regex, branch_name):
    print("Invalid branch name")
    exit(1)
else:
    # Everything is fine
    exit(0)