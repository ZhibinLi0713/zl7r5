import pytest
import System
import Staff
import Professor
#test teacher cannot drop student they don't teach
def test_professor_drop_student(grading_system):

   grading_system.login('saab', 'boomr345')
   assert 'saab' in grading_system.courses['databases']['professor']

   grading_system.usr.drop_student('hdjsr7', 'databases')


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
