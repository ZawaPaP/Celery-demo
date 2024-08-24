# logging_config.py
import logging.config

import yaml


def init_logging(config_path="logging_config.yaml"):
    with open(config_path, "r") as file:
        config = yaml.safe_load(file)
    logging.config.dictConfig(config)
