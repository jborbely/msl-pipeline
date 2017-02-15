"""
The pipeline context allows different :class:`~.stage.Stage`\'s to collaborate
by sharing data.
"""
from abc import ABCMeta, abstractmethod


class PipelineContext(metaclass=ABCMeta):
    """
    The pipeline context allows different :class:`~.stage.Stage`\'s to
    collaborate by sharing data.
    
    This interface defines error handling in the pipeline since
    it is important that errors are checked in each :class:`~.stage.Stage`
    to decide if the (:class:`~.pipeline.Pipeline`) should be terminated
    and how to cleanup resources if there were exceptions.
    """

    @abstractmethod
    def get_exception(self):
        """
        Returns the exception that occurred in a :class:`~.stage.Stage`.
        """
        pass

    @abstractmethod
    def add_exception(self, exception):
        """
        Adds an exception that occurred during the execution of 
        a :class:`~.stage.Stage`.
        
        Args:
            exception (:class:`~.pipeline_exception.PipelineException`): The
                pipeline exception that occurred
        """
        pass
