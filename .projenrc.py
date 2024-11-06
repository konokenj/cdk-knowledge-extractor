from projen.python import PythonProject

project = PythonProject(
    author_email="konoken@amazon.co.jp",
    author_name="Kenji Kono",
    module_name="cdk_knowledge_extractor",
    name="cdk-knowledge-extractor",
    poetry=True,
    version="0.1.0",
)

project.synth()