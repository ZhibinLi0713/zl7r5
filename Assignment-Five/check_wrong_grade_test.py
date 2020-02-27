import pytest
import System

def test_check_grades(grading_system):
    #test a student want to check grade in course which he/she doesn't attend
    grading_system.login('akend3', '123454321')
    assert grading_system.usr.check_grades('cloud_computing')

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
