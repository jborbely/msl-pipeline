"""
Contains the base class for all pipeline exceptions.
"""


class PipelineException(Exception):
    """
    An custom :py:class:`Exception` for a :class:`~.pipeline.Pipeline`.

    Args:
        message (str): The message for the exception.
    """
    def __init__(self, message):
        Exception.__init__(self, message)
        self._message = message

    @property
    def message(self):
        """
        Returns:
            :py:class:`str`: The :py:class:`Exception` message.
        """
        return self._message
