from pytest_mock import MockerFixture
from cdk_knowledge_extractor.aws_cdk import (
    find_integ_test_files,
    get_module_name,
    get_test_name,
    surround_with_codeblock,
)

expected_files = [
    "repositories/aws-cdk/packages/@aws-cdk-testing/framework-integ/test/aws-config/test/integ.rule.ts",
    "repositories/aws-cdk/packages/@aws-cdk-testing/framework-integ/test/aws-config/test/integ.rule2.ts",
]

ignored_files = [
    "repositories/aws-cdk/packages/@aws-cdk-testing/framework-integ/test/aws-config/test/hoge.snapshot/integ.rule3.ts",
    "repositories/aws-cdk/packages/@aws-cdk-testing/framework-integ/test/aws-config/test/assets/integ.rule3.ts",
]


def test_find_integ_test_files(mocker: MockerFixture):
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
