import os
import re
import sys
import argparse


class Frontmatter:
    @staticmethod
    def add_property(file_path, property_name):
        """
        Adds a property to the front matter of a file.

        Args:
            file_path (str): The path of the file.
            property_name (str): The name of the property to add.
        """
        pattern = r'---\n(.*?)---'
        content = Frontmatter._read_file_content(file_path)
        match, matched_content = Frontmatter._get_frontmatter_matches(pattern, content)

        if match and property_name in matched_content:
            return

        updated_content = content.replace(match.group(1), match.group(1).strip() + f'\n{property_name}:\n  - \n')
        Frontmatter._write_file_content(file_path, updated_content)

    @staticmethod
    def remove_property(file_path, property_name):
        """
        Removes a property from the front matter of a file.

        Args:
            file_path (str): The path of the file.
            property_name (str): The name of the property to remove.
        """
        pattern = r'(---\n.*?---)'
        content = Frontmatter._read_file_content(file_path)
        match, matched_content = Frontmatter._get_frontmatter_matches(pattern, content)

        if not match:
            return

        property_pattern = fr"({property_name}:.*?\n)(?=---|\S)"
        # Find the first match using property_pattern
        match_result = re.search(property_pattern, matched_content, re.DOTALL)
        if match_result:
            # Remove the matched group from matched_content
            updated_content = content.replace(match.group(1), matched_content.replace(match_result.group(1), ''))
            Frontmatter._write_file_content(file_path, updated_content)

    @staticmethod
    def edit_property(file_path, old_property_name, new_property_name):
        """
        Edits the name of a property in the front matter of a file.

        Args:
            file_path (str): The path of the file.
            old_property_name (str): The current name of the property.
            new_property_name (str): The new name of the property.
        """
        pattern = r'---\n(.*?)---'
        content = Frontmatter._read_file_content(file_path)
        match, matched_content = Frontmatter._get_frontmatter_matches(pattern, content)

        if match and old_property_name not in matched_content:
            return
        
        if new_property_name in matched_content:
            print(f"{file_path}: {new_property_name} already exists!")
            return

        updated_content = content.replace(match.group(1), matched_content.replace(f'{old_property_name}:', f'{new_property_name}:'))
        Frontmatter._write_file_content(file_path, updated_content)

    @staticmethod
    def process_files(directory, method, *args):
        """
        Processes files in a directory based on the specified method.

        Args:
            directory (str): The directory to process.
            method (str): The method to apply to the files ('add', 'remove', or 'edit').
            *args: Additional arguments depending on the method.
        """
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith('.md'):
                    file_path = os.path.join(root, file)
                    if method == 'add':
                        Frontmatter.add_property(file_path, *args)
                    elif method == 'remove':
                        Frontmatter.remove_property(file_path, *args)
                    elif method == 'edit':
                        Frontmatter.edit_property(file_path, *args)
                    else:
                        raise ValueError('Invalid method specified.')

    @staticmethod
    def _read_file_content(file_path):
        """
        Reads the content of a file.

        Args:
            file_path (str): The path of the file.

        Returns:
            str: The content of the file.
        """
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()

    @staticmethod
    def _write_file_content(file_path, content):
        """
        Writes content to a file.

        Args:
            file_path (str): The path of the file.
            content (str): The content to write.
        """
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)

    @staticmethod
    def _get_frontmatter_matches(pattern, content):
        """
        Retrieves the front matter matches from the content.

        Args:
            content (str): The content to search.

        Returns:
            tuple: A tuple containing the match object and the matched content.
        """
        match = re.search(pattern, content, re.DOTALL)
        if match:
            matched_content = match.group(1)
            return match, matched_content
        return None, None


def main():
    # 创建解析器并定义命令行参数
    parser = argparse.ArgumentParser(description='Add property to YAML')
    parser.add_argument('-d', '--directory', type=str, help='Directory path')
    parser.add_argument('-p', '--property', type=str, nargs='+', help='Property name')
    parser.add_argument('-m', '--mode', type=str, help='Action type')

    # 解析命令行参数
    args = parser.parse_args()

    # 检查必要的参数是否提供
    if not args.directory or not args.property:
        parser.print_help()
        sys.exit(1)

    # 处理指定目录及其子目录下的所有文件
    Frontmatter.process_files(args.directory, args.mode, *args.property)

if __name__ == '__main__':
    main()
