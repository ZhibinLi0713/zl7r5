import pytest
import System
import Staff

def test_change_grade(grading_system):

    grading_system.login('goggins', 'augurrox')
    grading_system.usr.change_grade('akend3', 'comp_sci', 'assignment1', 99)
    assert grading_system.users['akend3']['courses']['comp_sci']['assignment1']['grade'] == 99
    grading_system.load_data()


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
