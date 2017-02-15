"""
Contains the base class for creating a pipeline.
"""
from abc import ABCMeta, abstractmethod


class Pipeline(metaclass=ABCMeta):
    """
    A Pipeline connects each :class:`~.stage.Stage` which will be executed sequentially.
    """
    
    @abstractmethod
    def add_stage(self, stage):
        """
        Add (append) a stage to the pipeline.

        Args:
            stage (:class:`~.stage.Stage`): The stage to add.
        """
        pass
    
    @abstractmethod
    def add_except_stage(self, stage):
        """
        Add (append) a stage to the **except** error-handling sequence of stages
        (where **except** refers to a **try-except-finally** block when executing each
        :class:`~.stage.Stage` of the pipeline).

        Args:
            stage (:class:`~.stage.Stage`): The stage to add to **except**.
        """
        pass
    
    @abstractmethod 
    def add_finally_stage(self, stage):
        """
        Add (append) a stage to the **finally** sequence of stages (where **finally**
        refers to a **try-except-finally** block when executing each
        :class:`~.stage.Stage`) of the pipeline.
        
        Args:
            stage (:class:`~.stage.Stage`): The stage to add to **finally**.
        """
        pass
