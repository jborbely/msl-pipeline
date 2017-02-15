"""
Package for creating a sequential pipeline.

The following constants are provided in the **msl.pipeline** package.
"""
import time
from collections import namedtuple

from .stage import Stage
from .pipeline import Pipeline
from .pipeline_context import PipelineContext
from .pipeline_exception import PipelineException
from .pipeline_context_adaptor import PipelineContextAdaptor
from .sequential_pipeline import SequentialPipeline
from .log_error_stage import LogErrorStage

version_info = namedtuple('version_info', 'major minor micro releaselevel')(0, 1, 0, 'beta')
""":func:`~collections.namedtuple`: Contains the version information as a (major, minor, micro, releaselevel) tuple."""

__version__ = '{}.{}.{}'.format(*version_info)
__author__ = 'Joseph Borbely'
__copyright__ = '\xa9 2017{}, {}'.format(time.strftime('-%Y') if int(time.strftime('%Y')) > 2017 else '', __author__)
