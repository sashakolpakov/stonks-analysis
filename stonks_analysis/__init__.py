"""
Stonks Analysis Package - Financial data analysis and visualization tools
"""

from . import utils
from .utils import download_data, compute_generic_features

__version__ = "0.1.0"
__all__ = ["utils", "download_data", "compute_generic_features"]