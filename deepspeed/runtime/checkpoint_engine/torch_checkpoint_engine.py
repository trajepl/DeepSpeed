import torch
from deepspeed.utils import logger
from deepspeed.runtime.checkpoint_engine.checkpoint_engine import \
    CheckpointEngine


class TorchCheckpointEngine(CheckpointEngine):
    def __init__(self, config_params=None):
        super().__init__(self, config_params)

    def create(self, tag):
        print(f"[Torch] Checkpoint {tag} is begin to save!")

    def save(self, state_dict, path: str):
        logger.info(f"[Torch] Saving {path}...")
        torch.save(state_dict, path)
        logger.info(f"[Torch] Saved {path}.")
        return None

    def load(self, path: str, map_location=None):
        logger.info(f"[Torch] Loading checkpoint from {path}...")
        partition = torch.load(path, map_location=map_location)
        logger.info(f"[Torch] Loaded checkpoint from {path}.")
        return partition

    def commit(self, tag):
        print(f"[Torch] Checkpoint {tag} is ready now!")
        return True
