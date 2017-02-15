"""
Logs the error that occurred in a :class:`~.stage.Stage`.
"""
import logging
from msl.pipeline import Stage
from msl.pipeline import PipelineContext


class LogErrorStage(Stage):
    """
    Logs the error that occurred in a :class:`~.stage.Stage`.
    """

    def execute(self, context):
        """
        Logs the error that occurred in a :class:`~.stage.Stage`.

        Args:
            context (:class:`~.pipeline_context.PipelineContext`): Keeps the shared
                information between each :class:`~.stage.Stage` in the
                :class:`~.pipeline.Pipeline`.
        """
        if not isinstance(context, PipelineContext):
            raise TypeError('The input must be of type PipelineContext')
        logging.log(logging.ERROR, context.get_exception())
