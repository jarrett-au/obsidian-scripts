# obsidian-scripts
Some useful python scripts for Obsidian(Powered by ChatGPT)

## [批量替换当前目录下文件内容](./str_replace.py)
### 功能介绍

该脚本用于批量替换[[Obsidian]]中当前目录下[[Markdown]]文件中所包含的指定字符串。

### 参数说明

- `-d, --directory`：指定要处理的目录路径（建议加引号）。
- `-s, --string`: 指定新旧字符串（空格分隔）
	- `old_str[String]`: 要替换的旧字符串。
	- `new_str[String]`: 替换后的新字符串。
- `-h, --help`：显示帮助信息。


## [批量修改 Obsidian Frontmatter](./frontmatter.py)
### 功能介绍

该脚本用于向[[Obsidian]]文件的 Frontmatter 部分中添加指定属性。它会递归地遍历指定目录及其子目录下的所有 [[Markdown]] 文件，并在文件的 Frontmatter 部分对属性进行操作。

### 参数说明

- `-d, --directory`：指定要处理的目录路径。
- `-p, --property`：指定要添加的属性名称。
- `-h, --help`：显示帮助信息。

### 使用

```bash
# 添加属性
python frontmatter.py -d "</path/to/directory>" -m add -p <property_name>
# 删除属性
python frontmatter.py -d "</path/to/directory>" -m remove -p <property_name>
# 修改属性
python frontmatter.py -d "</path/to/directory>" -m remove -p <old_property_name> <new_property_name>
```
