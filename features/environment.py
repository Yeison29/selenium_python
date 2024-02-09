from selenium import webdriver
from loguru import logger


def browser_init(context):
    """
    :param context: Behave context
    """

    logger.add("selenium_logs/{time}.log", rotation="500 MB", level="DEBUG")

    context.driver = webdriver.Chrome()
    # context.browser = webdriver.Safari()
    # context.browser = webdriver.Firefox()

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)

    def selenium_logger(message):
        logger.debug(message)

    webdriver.remote.remote_connection.logger = selenium_logger


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    logger.add("selenium_logs/{time}.log", rotation="500 MB", level="DEBUG")
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
    logger.remove()
