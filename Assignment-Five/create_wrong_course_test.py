import pytest
import System

def test_submit_assignment(grading_system):
    #test if the student entered a wrong course
    grading_system.login('hdjsr7', 'pass1234')
    assert grading_system.usr.submit_assignment('wrong_course', 'assignment1', 'test', '02/20/20') == False


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
