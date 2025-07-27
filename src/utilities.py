import os
import shutil
from markdowntohtmlnotes import *

def refresh_directory(source_dir, target_dir):
    target_abspath = os.path.abspath(target_dir)
    source_abspath = os.path.abspath(source_dir)

    if not os.path.exists(source_abspath) or not os.path.exists(target_abspath):
        return f'Error: The source directory {source_dir} or target directory {target_dir} does not exist.'
    
    if os.path.exists(target_abspath):
        tar_files = os.listdir(target_abspath)
        for tar_file in tar_files:
            tar_filepath = os.path.join(target_abspath, tar_file)
            if os.path.isfile(tar_filepath):
                try:
                    os.remove(tar_filepath)
                except OSError as e:
                    return f'Error: Could not remove file {tar_filepath}. Reason: {e}'
            elif os.path.isdir(tar_filepath):
                if tar_filepath != source_abspath:
                    try:
                        shutil.rmtree(tar_filepath)
                    except OSError as e:
                        return f'Error: Could not remove directory {tar_filepath}. Reason: {e}'
    else:
        return f'Error: The target directory {target_dir} does not exist.'
    
    if os.path.exists(source_abspath):
        src_files = os.listdir(source_abspath)
        for src_file in src_files:
            src_filepath = os.path.join(source_abspath, src_file)
            tar_filepath = os.path.join(target_abspath, src_file)
            if os.path.isfile(src_filepath):
                try:
                    shutil.copy(src_filepath, tar_filepath)
                except OSError as e:
                    return f'Error: Could not copy file {src_filepath} to {tar_filepath}. Reason: {e}'
            if os.path.isdir(src_filepath):
                try:
                    shutil.copytree(src_filepath, tar_filepath)
                except OSError as e:
                    return f'Error: Could not copy directory {src_filepath} to {tar_filepath}. Reason: {e}'
    return f'Success: Refreshed directory {target_dir} with contents from {source_dir}.'

def extract_title(markdown):
    lines = markdown.splitlines()
    for line in lines:
        if line.strip().startswith('# '):
            return line[2:]
    return None

def generate_page(from_path, template_path, dest_path, basepath=None):
    from_abspath = os.path.abspath(from_path)
    template_abspath = os.path.abspath(template_path)
    dest_abspath = os.path.abspath(dest_path)
    if not os.path.exists(from_abspath):
        print(f'Error: The source file {from_path} does not exist.')
        return
    if not os.path.exists(template_abspath):
        print(f'Error: The template file {template_path} does not exist.')
        return
    dest_dir = os.path.dirname(dest_abspath)
    if not os.path.exists(dest_dir):
        try:
            os.makedirs(dest_dir, exist_ok=True)
        except OSError as e:
            print(f'Error: Could not create destination directory for {dest_abspath}. Reason: {e}')
            return
    print(f'Generating page from {from_abspath} to {dest_abspath} using {template_abspath}')
    md_f = open(from_abspath, 'r', encoding='utf-8')
    md_content = md_f.read()
    md_f.close()
    template_f = open(template_abspath, 'r', encoding='utf-8')
    template_content = template_f.read()
    template_f.close()
    html_content = markdown_to_html_node(md_content).to_html()
    title = extract_title(md_content)
    html_page_content = template_content.replace('{{ Content }}', html_content)
    html_page_content = html_page_content.replace('{{ Title }}', title)
    if basepath:
        html_page_content = html_page_content.replace('href="/', 'href="' + basepath)
        html_page_content = html_page_content.replace('src="/', 'src="' + basepath)
    with open(dest_abspath, 'w', encoding='utf-8') as dest_f:
        dest_f.write(html_page_content)

def get_all_md_files(source_dir, extension=None):
    files = []
    for dirpath, _, filenames in os.walk(source_dir):
        for filename in filenames:
            if extension and not filename.endswith(extension):
                continue
            abspath = os.path.join(dirpath, filename)
            files.append(abspath)
    return files


def generate_pages_recursive(source_dir, template_file_path, dest_dir, basepath=None):
    if not os.path.exists(source_dir):
        print(f'Error: The source directory {source_dir} does not exist.')
        return
    if not os.path.exists(template_file_path):
        print(f'Error: The template file {template_file_path} does not exist.')
        return
    if not os.path.exists(dest_dir):
        try:
            os.makedirs(dest_dir, exist_ok=True)
        except OSError as e:
            print(f'Error: Could not create destination directory {dest_dir}. Reason: {e}')
            return
    md_files = get_all_md_files(source_dir, '.md')
    for md_file in md_files:
        dest_file = md_file.replace(source_dir, dest_dir).replace('.md', '.html')
        generate_page(md_file, template_file_path, dest_file, basepath)
