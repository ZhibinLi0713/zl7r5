import pytest
import System

def test_check_password(grading_system):

   assert grading_system.check_password('akend3', '123454321' )==True
   assert grading_system.check_password('akend3', '12345')==False
   assert grading_system.check_password('akend3', '54321')==False
   assert grading_system.check_password('akend3', 'bestTA')==False




@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

