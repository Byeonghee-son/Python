import logging

logging.basicConfig(level=logging.CRITICAL)

def add(a,b):
    ret = a + b
    #print(a,b,ret)
    logging.debug(f'Debug:{ret}')
    logging.info(f'Info:{ret}')
    logging.warning(f'Warning:{ret}')
    logging.error(f'Error:{ret}')
    logging.critical(f'Critical:{ret}')

    return ret

add(10,20)