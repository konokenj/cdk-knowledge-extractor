import os
from .aws_cdk import (
    find_integ_test_files,
    get_module_name,
    get_test_name,
    surround_with_codeblock,
)

OUT_DIR = "dist"

if __name__ == "__main__":
    integ_test_files = find_integ_test_files("repositories/aws-cdk")
    for file in integ_test_files:
        module_name = get_module_name(file)
        test_name = get_test_name(file)
        with open(file, "r") as f:
            content = f.read()
            os.makedirs(f"{OUT_DIR}/{module_name}", exist_ok=True)
            with open(
                f"{OUT_DIR}/{module_name}/{module_name}.{test_name}.md", "w"
            ) as f:
                f.write(surround_with_codeblock(module_name, test_name, content))
