from importlib.metadata import PackageNotFoundError, version
from importlib.resources import files

__package_name__ = "MOTOR_MEDS"

try:
    __version__ = version(__package_name__)
except PackageNotFoundError:  # pragma: no cover
    # package is not installed
    __version__ = "unknown"

PREPROCESS_CFG = files(__package_name__).joinpath("configs/preprocess.yaml")
PRETRAIN_CFG = files(__package_name__).joinpath("configs/pretrain.yaml")
FINETUNE_CFG = files(__package_name__).joinpath("configs/finetune.yaml")
PREDICT_CFG = files(__package_name__).joinpath("configs/predict.yaml")

__all__ = ["PREPROCESS_CFG", "PRETRAIN_CFG", "FINETUNE_CFG", "PREDICT_CFG"]
