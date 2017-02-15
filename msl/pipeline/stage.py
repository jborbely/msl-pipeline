"""
The basic processing unit in a :class:`~.pipeline.Pipeline`.
"""
from abc import ABCMeta, abstractmethod


class Stage(metaclass=ABCMeta):
    """
    The basic processing unit in a :class:`~.pipeline.Pipeline`.
    """
    
    @abstractmethod
    def execute(self, context):
        """
        Executes the task to be performed by this :class:`~.stage.Stage`.
        
        The input data will be read from the ``context`` manager.
        The output data will be written to the ``context`` manager.
        
        Args:
            context (:class:`~.pipeline_context.PipelineContext`): Keeps the shared
                information between each :class:`~.stage.Stage` in the
                :class:`~.pipeline.Pipeline`.
        """
        pass
