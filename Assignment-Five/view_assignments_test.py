import pytest
import System
import Staff
import Professor
import Student

def test_view_assignments(grading_system):

    grading_system.login('akend3', '123454321')
    assert grading_system.usr.view_assignments('databases')[0]==['assignment1','1/5/20']


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
