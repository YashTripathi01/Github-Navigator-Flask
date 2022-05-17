# Container will keep all of the application components and their dependencies.
# Factory provider. It will create a Github client.
# Configuration provider. It will provide an API token and a request timeout for the Github client. We will specify the location of the configuration file. The configuration provider will parse the configuration file when we create a container instance.

from dependency_injector import containers, providers
from github import Github

from . import services


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=['.views'])
    config = providers.Configuration(yaml_files=['config.yml'])

    github_client = providers.Factory(
        Github, login_or_token=config.github.auth_token, timeout=config.github.request_timeout)

    search_service = providers.Factory(
        services.SearchService, github_client=github_client)
