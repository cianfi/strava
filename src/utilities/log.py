import logging
import os
import datetime
from typing import Optional

class StravaLogger:
    _initialized: bool = False

    def __init__(self) -> None:
        if not self._initialized:
            self.setup_logging()
            StravaLogger._initialized = True
    
    def _file_logger(self) -> logging.Handler:
        """
        This creates the file logger configuration for the logger.

        Returns a file logging.Handler
        """
        os.makedirs("logs", exist_ok=True)
        current_time = datetime.datetime.now(datetime.UTC)
        log_path = f"logs/{current_time.strftime('%d-%m-%y %H:%M:%S')}"

        file_formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(filename)s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )

        file_handler = logging.FileHandler(log_path)
        file_handler.setLevel(level=logging.DEBUG)
        file_handler.setFormatter(file_formatter)
        return file_handler

    def _console_logger(self) -> logging.Handler:
        """
        This creates the console logger configuration for the logger.

        Returns a console logging.Handler
        """
        console_formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )

        console_handler = logging.StreamHandler()
        console_handler.setLevel(level=logging.DEBUG)
        console_handler.setFormatter(console_formatter)
        return console_handler

    def setup_logging(self) -> None:
        """
        This sets up logging basic configuration and getLogger. 

        Returns: None
        """
        logging.basicConfig(level=logging.DEBUG, handlers=[])

        logger = logging.getLogger()
        logger.addHandler(self._console_logger())
        logger.addHandler(self._file_logger())

    def get_logger(self, name: str) -> logging.Logger:
        """
        
        """
        return logging.getLogger(name)
    
# Need this because it creates a Singleton Pattern. This will prevent the creation of multiple StravaLogger instances.
_strava_logger = StravaLogger()

def get_logger(name: Optional[str]) -> logging.Logger:
    if name is None:
        name = "strava"

    return _strava_logger.get_logger(name)