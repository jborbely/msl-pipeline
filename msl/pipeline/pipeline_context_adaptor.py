"""
An adaptor class for the :class:`~.stage.PipelineContext` interface.
"""
from msl.pipeline import PipelineContext
from msl.pipeline import PipelineException


class PipelineContextAdaptor(PipelineContext):
    """
    An adaptor class for the :class:`~.stage.PipelineContext` interface.
    """
    def __init__(self):
        self._exception = None
    
    def get_exception(self):
        """
        Returns:
            An :py:class:`Exception`.
        """
        return self._exception

    def add_exception(self, exception):
        """
        Add an exception.

        Args:
            exception (:py:class:`~.pipeline.exception.PipelineException`): The
                exception that occurred in a pipeline.
        """
        if not isinstance(exception, PipelineException):
            raise TypeError('The input must be of type PipelineException')
        self._exception = exception
