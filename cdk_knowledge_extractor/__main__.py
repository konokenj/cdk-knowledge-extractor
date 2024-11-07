import os
import shutil
from .aws_cdk import (
    find_integ_test_files,
    find_markdown_files,
    get_module_name,
    get_test_name,
    surround_with_codeblock,
)

SOURCE_DIR = "repositories/aws-cdk"
OUT_DIR = "dist"

if __name__ == "__main__":
    markdown_files = find_markdown_files(SOURCE_DIR)
    for file in markdown_files:
        # remove prefix from source file path
        dist_path = file.replace(SOURCE_DIR + "/", "")
        # copy file to dist with same directory structure
        os.makedirs(os.path.dirname(f"{OUT_DIR}/docs/{dist_path}"), exist_ok=True)
        shutil.copy(file, f"{OUT_DIR}/docs/{dist_path}")

    integ_test_files = find_integ_test_files(SOURCE_DIR)
    for file in integ_test_files:
        module_name = get_module_name(file)
        test_name = get_test_name(file)
        with open(file, "r") as f:
            content = f.read()
            os.makedirs(f"{OUT_DIR}/integ-tests/{module_name}", exist_ok=True)
            with open(
                f"{OUT_DIR}/integ-tests/{module_name}/{module_name}.{test_name}.md", "w"
            ) as f:
                f.write(surround_with_codeblock(module_name, test_name, content))
