import logging


log = logging.getLogger()

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

debug_info_log = logging.FileHandler('debug_info.log', encoding='utf-8')
debug_info_log.setLevel(logging.DEBUG)
debug_info_log.setFormatter(formatter)
log.addHandler(debug_info_log)

warnings_errors_log = logging.FileHandler('warnings_errors.log', encoding='utf-8')
warnings_errors_log.setLevel(logging.WARNING)
warnings_errors_log.setFormatter(formatter)
log.addHandler(warnings_errors_log)


log.debug('Это сообщение уровня DEBUG.')
log.info('Это сообщение уровня INFO.')
log.warning('Это сообщение уровня WARNING.')
log.error('Это сообщение уровня ERROR.')
log.critical('Это сообщение уровня CRITICAL.')
