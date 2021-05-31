import logging
# check out how logging is working
logging.basicConfig(filename='Test.log',level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')

def add (x, y):
    return x + y
def sub(x, y):
    return x - y

value1 = 24
value2 = 12

logging.info("Test started")
logging.debug('adding : {} + {}'.format(value1,value2))
logging.debug('subdividing  : {} - {}'.format(value1,value2))
add_result = add(value1,value2)
sub_result = sub(value1,value2)
logging.info(add_result)
logging.info(sub_result)
logging.debug('adding : {} + {}'.format("name",'d'))
add_result = add("name",'d')
logging.error(add_result)
logging.info("Test ended")