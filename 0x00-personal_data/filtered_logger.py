#!/usr/bin/env python3
import re
import logging

def filter_datum(fields, redaction, message, separator):
    """Returns log message obfuscated"""
    pattern = '|'.join(f'{field}=[^{separator}]*' for field in fields)
    return re.sub(pattern, lambda m: f"{m.group().split('=')[0]}={redaction}",
                   message)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields):
        """Constructor"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields


    def format(self, record: logging.LogRecord) -> str:
        """Filters values in in incoming log records"""
        NotImplementedError