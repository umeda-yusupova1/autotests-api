import platform
import sys
from pathlib import Path

from config import settings

ALLURE_RESULTS_DIR = Path(settings.allure_results_dir)


def create_allure_environment_file():
    properties = [
        f'{key}={value}\n'
        for key, value in settings.model_dump().items()
    ]
    properties.extend((
        f'os_info={platform.system()}, {platform.release()}\n',
        f'python_version={sys.version}'
    ))

    with open(ALLURE_RESULTS_DIR / 'environment.properties', 'w') as file:
        file.writelines(properties)
