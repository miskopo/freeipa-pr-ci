from .common import logging_init_stream_handler, TimeoutException
from .tasks import Build, RunPytest, RunWebuiTests, RunPytest2, RunPytest3

# Singleton constant used to store stats file path
BOX_STATS_FILE = None
