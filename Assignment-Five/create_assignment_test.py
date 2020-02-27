import pytest
import System
import Staff

def test_create_assignment(grading_system):

   grading_system.login('cmhbf5', 'bestTA')
   grading_system.usr.create_assignment('assignment3', '2/29/20', 'comp_sci')
   assert grading_system.courses['ccomp_sci']['assignments']['assignment3']['due_date'] == '2/29/20'

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
