import pytest
import System
import Staff
import Professor

def test_drop_student(grading_system):

   grading_system.login('goggins', 'augurrox')
   grading_system.usr.drop_student('akend3', 'comp_sci')
   grading_system.load_data()
   assert 'comp_sci' not in grading_system.users['akend3']['courses']

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
