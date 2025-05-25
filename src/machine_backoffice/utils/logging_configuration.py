import logging
import sys
import pyfiglet
from colorama import Fore, Style, init
from uvicorn.logging import DefaultFormatter

init(autoreset=True)

LOGGING_CONFIGURED = False

LOG_COLORS = {
    "DEBUG": Style.BRIGHT + Fore.CYAN,
    "INFO": Style.BRIGHT + Fore.GREEN,
    "WARNING": Style.BRIGHT + Fore.YELLOW,
    "ERROR": Style.BRIGHT + Fore.RED,
    "CRITICAL": Style.BRIGHT + Fore.RED,
}

LOG_ICONS = {
    "DEBUG": "🔍",
    "INFO": "🚀",
    "WARNING": "⚠️",
    "ERROR": "❌",
    "CRITICAL": "🔥",
}


class ColoredFormatter(DefaultFormatter):
    def format(self, record):
        log_color = LOG_COLORS.get(record.levelname, Style.RESET_ALL)
        log_icon = LOG_ICONS.get(record.levelname, "")
        log_message = super().format(record)
        return f"{log_color}{log_icon} {log_message}{Style.RESET_ALL}"


def setup_logging():
    global LOGGING_CONFIGURED
    if LOGGING_CONFIGURED:
        return
    LOGGING_CONFIGURED = True

    start_banner = pyfiglet.figlet_format("-----", font="standard")
    banner = pyfiglet.figlet_format("Machine Backoffice", font="standard")
    end_banner = pyfiglet.figlet_format("-----", font="standard")
    print(f"{Fore.CYAN}{start_banner}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{banner}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{end_banner}{Style.RESET_ALL}")

    machine_backoffice_logger = logging.getLogger("machine_backoffice")
    machine_backoffice_logger.setLevel(logging.INFO)

    if not machine_backoffice_logger.hasHandlers():
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(ColoredFormatter("%(levelprefix)s %(message)s"))
        machine_backoffice_logger.addHandler(handler)

    uvicorn_logger = logging.getLogger("uvicorn")
    for handler in uvicorn_logger.handlers:
        if handler.formatter:
            handler.setFormatter(ColoredFormatter(handler.formatter._fmt))

    logging.root = machine_backoffice_logger
    logging.getLogger = lambda name=None: machine_backoffice_logger


setup_logging()