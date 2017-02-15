"""
A sequential pipeline executes each :class:`~.stage.Stage` in the
:class:`~.pipeline.Pipeline` in sequence.
"""
import logging
from msl.pipeline import Stage
from msl.pipeline import Pipeline
from msl.pipeline import PipelineException
from msl.pipeline import PipelineContext


class SequentialPipeline(Pipeline, Stage):
    """
    A sequential pipeline executes each :class:`~.stage.Stage` in the
    :class:`~.pipeline.Pipeline` in sequence, imitating a **try-except-finally**
    block. If there is an exception in a :class:`~.stage.Stage` then the
    :class:`~.pipeline.Pipeline` stops and performs a cleanup (**finally**).
    
    try:
        execute each stage sequentially
    except :py:class:`Exception`:
        execute except stages
    finally:
        execute finally stages 
    """
    def __init__(self):
        self.stages = []
        self.except_stages = []
        self.finally_stages = []

    def add_stage(self, stage):
        """
        Add (append) a stage to the pipeline.

        Args:
            stage (:class:`~.stage.Stage`): The stage to add.
        """
        if not isinstance(stage, Stage):
            raise TypeError('The input must be of type Stage')
        self.stages.append(stage)
    
    def add_except_stage(self, stage):
        """
        Add (append) a stage to the **except** error-handling sequence of stages
        (where **except** refers to a **try-except-finally** block when executing each
        :class:`~.stage.Stage` of the pipeline).

        Args:
            stage (:class:`~.stage.Stage`): The stage to add to **except**.
        """
        if not isinstance(stage, Stage):
            raise TypeError('The input must be of type Stage')
        self.except_stages.append(stage)

    def add_finally_stage(self, stage):
        """
        Add (append) a stage to the **finally** sequence of stages (where **finally**
        refers to a **try-except-finally** block when executing each
        :class:`~.stage.Stage`) of the pipeline.

        Args:
            stage (:class:`~.stage.Stage`): The stage to add to **finally**.
        """
        if not isinstance(stage, Stage):
            raise TypeError('The input must be of type Stage')
        self.finally_stages.append(stage)
    
    def execute(self, context):
        """
        Executes the task to be performed by this :class:`~.stage.Stage`.

        The input data will be read from the ``context`` manager.
        The output data will be written to the ``context`` manager.

        Args:
            context (:class:`~.pipeline_context.PipelineContext`): Keeps the shared
                information between each :class:`~.stage.Stage` in the
                :class:`~.pipeline.Pipeline`.

        Raises:
            TypeError: If the input argument is the wrong data type.
        """
        if not isinstance(context, PipelineContext):
            raise TypeError('The input must be of type PipelineContext')

        got_error = len(self.stages) == 0

        # checks if there are no stages in the pipeline
        if got_error:
            context.add_exception(PipelineException('No stages in pipeline'))
            if self.except_stages:
                logging.log(logging.ERROR, 'No stages in pipeline')

        # sequentially execute each stage in the pipeline
        for stage in self.stages:
            stage.execute(context)
            got_error = context.get_exception() is not None
            if got_error:
                break
        
        # if any error occurred then execute the except stages
        if got_error:
            for stage in self.except_stages:
                stage.execute(context)

        # execute the finally stages
        for stage in self.finally_stages:
            stage.execute(context)
