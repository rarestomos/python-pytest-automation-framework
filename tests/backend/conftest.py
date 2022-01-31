import pytest
import uuid


@pytest.fixture
def invalid_id():
    """
    Setup method that generates UUID that will be used as fake ID in backend test functions
    :return: The ID that does not exist
    """
    not_existing_id = str(uuid.uuid4())
    return not_existing_id
