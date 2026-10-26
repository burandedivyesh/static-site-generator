import os
import shutil
from helper import extract_title, markdown_to_htmlnode, markdown_to_blocks


def trial():
    markdown_path = "/home/thatguy/Personal/Work/thatguy/static-site-generator/contents/index.md"
    markdown = ""
    with open(markdown_path, "r") as f:
        markdown = f.read()

    # Step 1 convert to blocks
    blocks = markdown_to_blocks(markdown)
    print("Step 1: ---------------------------------------")
    for block in blocks:
        print(block)
        print("-----------next block-------------")

    # Step 2 block to htmlnode
    


    
def copy_files(source_path:str, dest_path:str):
    if os.path.exists(dest_path):
        shutil.rmtree(dest_path)
        os.mkdir(dest_path)
    else:
        os.mkdir(dest_path)

    source_dir_list = os.listdir(source_path)
    print(f"Dir: {source_path}, Contents: {source_dir_list}")

    for item in source_dir_list:
        path = os.path.join(source_path, item)
        if os.path.isfile(path):
            shutil.copy(path, dest_path)
            print(f"Copied file: {path} to {dest_path}")
            continue
        target = os.path.join(dest_path, item)
        copy_files(path, target)

    return

def generate_page(source_path, template_path, dest_path):
    print(f"Generating page from: {source_path} to {dest_path} using {template_path}.")
    markdown = ""
    with open(source_path, "r") as f :
        markdown = f.read()

    template = ""
    with open(template_path, "r") as f:
        template = f.read()

    title = extract_title(markdown)
    content = markdown_to_htmlnode(markdown).to_html()

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", content)

    target = ""
    if os.path.exists(dest_path):
        target = os.path.join(dest_path, "index.html")
    else:
        os.mkdir(dest_path)
        target = os.path.join(dest_path, "index.html")

    with open(target, "w") as f:
        f.write(template)

    return 

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    src_content_list = os.listdir(dir_path_content)

    # Fetching template.html globally
    template = ""
    with open(template_path, "r") as f:
        template = f.read()


    for item in src_content_list:
        # for every file here that ends in .md
        path = os.path.join(dir_path_content, item)

        if item.endswith(".md"):
            markdown = ""
            with open(path, "r") as f:
                markdown = f.read()

            title = extract_title(markdown)
            content = markdown_to_htmlnode(markdown).to_html()

            template_rpl = template.replace("{{ Title }}", title).replace("{{ Content }}", content)

            target = ""
            if os.path.exists(dest_dir_path):
                target = os.path.join(dest_dir_path, "index.html")
            else:
                os.mkdir(dest_dir_path)
                target = os.path.join(dest_dir_path, "index.html")

            with open(target, "w") as f:
                f.write(template_rpl)
                print(f"File: {item} written in dir: {target}")

            continue # Skip the next part

        dst_path = os.path.join(dest_dir_path, item)
        if os.path.exists(dst_path):
            shutil.rmtree(dst_path)
            os.mkdir(dst_path)
        else:
            os.mkdir(dst_path)

        generate_pages_recursive(path, template_path, dst_path)

    return 

            

            





def main():
    # Copy static files to public
    source_path = "/home/thatguy/Personal/Work/thatguy/static-site-generator/static"
    dest_path   = "/home/thatguy/Personal/Work/thatguy/static-site-generator/public"
    copy_files(source_path, dest_path)

    # Export HTML to public
    markdown_path = "/home/thatguy/Personal/Work/thatguy/static-site-generator/contents/index.md"
    template_path = "/home/thatguy/Personal/Work/thatguy/static-site-generator/template.html"
    html_path     = "/home/thatguy/Personal/Work/thatguy/static-site-generator/public"
    # generate_page(markdown_path, template_path, html_path)
    # trial()
    content_path = "/home/thatguy/Personal/Work/thatguy/static-site-generator/contents"
    dst_dir_path = "/home/thatguy/Personal/Work/thatguy/static-site-generator/public"
    generate_pages_recursive(content_path, template_path, dst_dir_path)



 




   


if __name__ == "__main__":
    main()

