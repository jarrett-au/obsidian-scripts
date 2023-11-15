import os
import argparse

def replace_in_file(file_path, old_str, new_str):
    with open(file_path, 'r', encoding='utf-8') as file:
        file_content = file.read()

    file_content = file_content.replace(old_str, new_str)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(file_content)

def traverse_directory(directory, old_str, new_str):
    for root, dirs, files in os.walk(directory):
        for file in files:
		        if file.endswith('.md'):
		            file_path = os.path.join(root, file)
		            replace_in_file(file_path, old_str, new_str)

# 创建命令行参数解析器
parser = argparse.ArgumentParser(description='Replace strings in files in a directory tree.')
parser.add_argument('-s', '--string', dest='old_new_str', nargs=2, metavar=('old_str', 'new_str'), help='the old and new strings to replace')
parser.add_argument('-d', '--directory', dest='directory', metavar='directory', help='the directory to traverse')
args = parser.parse_args()

# 检查必要的参数是否提供
if not args.old_new_str:
    parser.error('Please provide the old and new strings using the -s or --string argument.')
if not args.directory:
    parser.error('Please provide the directory to traverse using the -d or --directory argument.')

old_str, new_str = args.old_new_str
traverse_directory(args.directory, old_str, new_str)
