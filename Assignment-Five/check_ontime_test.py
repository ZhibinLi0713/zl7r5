import pytest
import System
import Staff
import Professor
import Student

def test_drop_student(grading_system):

   grading_system.login('akend3', '123454321')
   
   assert grading_system.usr.check_ontime('02/01/20','02/10/20') == True
   assert grading_system.usr.check_ontime('03/10/20','02/10/20') == False



@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
