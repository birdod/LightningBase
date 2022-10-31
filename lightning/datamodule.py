import os
from typing import Any, Dict, List, Optional, Tuple

import pytorch_lightning as pl
from omegaconf import DictConfig
from torch.utils.data import DataLoader


class EmbeddedDataModule(pl.LightningDataModule):
    def __init__(self, config: DictConfig):
        super().__init__()
        self.config = config
    
    def setup(self, stage: Optional[str] = None):

    
    def train_dataloader(self) -> DataLoader:
        
    def val_dataloader(self) -> DataLoader:

        