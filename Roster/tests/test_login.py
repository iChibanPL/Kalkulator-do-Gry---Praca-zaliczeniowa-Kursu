import pytest
import logging

@pytest.fixture()
def logger():

        logger = logging.getLogger('Some.Logger')
        logger.setLevel(logging.INFO)

        return logger

def test_logger_with_fixture(logger, caplog):

    logger.info('Ziomeczek')

    assert 'Ziomeczek' in caplog.text