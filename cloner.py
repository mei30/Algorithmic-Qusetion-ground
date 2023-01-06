import argparse
import os
import subprocess


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="TemplateCloner",
            description="Tiny script that intented to clone a C++ based algorithmic issue ground template")

    parser.add_argument('-p', '--path', dest='path', help="The path to your prefered issue location.", required=True)
    parser.add_argument('-i', '--issue', dest='issue', help="The name of your issue or problem that you want to resolve.", required=True)

    args = parser.parse_args()

    make_issue_dir_command = f'mkdir {args.path}/{args.issue}'
    copy_command = f'cp -r ./template {args.path}/{args.issue}'

    try:
        subprocess.check_output(make_issue_dir_command, shell=True)
        subprocess.check_output(copy_command, shell=True)
    except subprocess.CalledProcessError as e: 
        print(e.output)
    
