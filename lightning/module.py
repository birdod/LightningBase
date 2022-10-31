from typing import Any, Dict, List, Optional, Tuple
from omegaconf import DictConfig

import pytorch_lightning as pl
import torch
import torch.nn as nn
from torch.optim import Optimizer
from torch.optim.lr_scheduler import LambdaLR
from torch.optim import AdamW

from modeling import EmbeddingClassifier, TwoLayerCls

class EmbeddingModule(pl.LightningModule):
    def __init__(self, config: DictConfig):
        super().__init__()
        
    def forward(self, x):

    def training_step(
        self,
        batch: List, 
        batch_idx: int
    ) -> torch.Tensor:

    def validation_step(
        self,
        batch: List, 
        batch_idx: int
    ) -> torch.Tensor:

    def configure_optimizers(self)