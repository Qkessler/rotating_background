import logbook


def init_logging(filename: str = None):
    level = logbook.TRACE
    logbook.FileHandler(filename, level=level).push_application()
    msg = 'Logging initialized, level: {}, mode: {}'.format(
        level,
        "stdout mode" if not filename else 'file mode: ' + filename
        )
    logger = logbook.Logger('Startup')
    logger.notice(msg)
