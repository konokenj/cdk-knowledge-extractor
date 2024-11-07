from pytest_mock import MockerFixture
from cdk_knowledge_extractor.aws_cdk import (
    find_markdown_files,
    find_integ_test_files,
    get_module_name,
    get_test_name,
    surround_with_codeblock,
)


def test_find_markdown_files(mocker: MockerFixture):
    expected_files = [
        "repositories/aws-cdk/packages/aws-cdk-lib/aws-lakeformation/README.md",
        "repositories/aws-cdk/packages/aws-cdk-lib/aws-codeartifact/README.md",
        "repositories/aws-cdk/packages/aws-cdk-lib/assets/README.md",
    ]

    ignored_files = [
        "repositories/aws-cdk/packages/@aws-cdk-testing/framework-integ/test/aws-lambda-nodejs/test/integ.specifycode.js.snapshot/asset.1a1a5806c7ba6c308e1a83f863e2d6f1f82a6daeb20286116d4a8b049faf1506/README.md",
        "repositories/aws-cdk/packages/@aws-cdk-testing/cli-integ/resources/cli-regression-patches/v2.132.0/NOTES.md",
    ]

    mocker.patch(
        "glob.glob",
        return_value=expected_files + ignored_files,
    )
    integ_test_files = find_markdown_files("repositories/aws-cdk")
    assert list(integ_test_files) == expected_files


def test_find_integ_test_files(mocker: MockerFixture):
    expected_files = [
        "repositories/aws-cdk/packages/@aws-cdk-testing/framework-integ/test/aws-config/test/integ.rule.ts",
        "repositories/aws-cdk/packages/@aws-cdk-testing/framework-integ/test/aws-config/test/integ.rule2.ts",
    ]

    ignored_files = [
        "repositories/aws-cdk/packages/@aws-cdk-testing/framework-integ/test/aws-config/test/hoge.snapshot/integ.rule3.ts",
        "repositories/aws-cdk/packages/@aws-cdk-testing/framework-integ/test/aws-config/test/assets/integ.rule3.ts",
    ]

    mocker.patch(
        "glob.glob",
        return_value=expected_files + ignored_files,
    )
    integ_test_files = find_integ_test_files("repositories/aws-cdk")
    assert list(integ_test_files) == expected_files


def test_get_module_name():
    module_name = get_module_name(
        "repositories/aws-cdk/packages/@aws-cdk-testing/framework-integ/test/aws-config/test/integ.rule.ts"
    )
    assert module_name == "aws-config"


def test_get_test_name():
    test_name = get_test_name(
        "repositories/aws-cdk/packages/@aws-cdk-testing/framework-integ/test/aws-config/test/integ.rule.ts"
    )
    assert test_name == "rule"


def test_surround_with_codeblock():
    codeblock = surround_with_codeblock(
        "mymodule", "test1", "console.log('hello world');"
    )
    assert (
        codeblock
        == """\
## mymodule / test1

```ts
console.log('hello world');
```

"""
    )
