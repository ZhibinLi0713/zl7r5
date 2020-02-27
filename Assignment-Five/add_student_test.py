import pytest
import System
import Staff
import Professor

def test_add_student(grading_system):

   grading_system.login('goggins', 'augurrox')
   grading_system.usr.add_student('akend3', 'cloud_computing')
   gradingSystem.reload_data()
   gradingSystem.login('akend3', 'i123454321')
   courses = gradingSystem.usr.courses
   assert 'cloud_computing' in grading_system.users['akend3']['courses']

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
