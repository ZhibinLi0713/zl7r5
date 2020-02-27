import pytest
import System
import Staff
def test_create_assignment_differernt(grading_system):
   #test professor cannot create assignment for other course he doesn't teach.
   grading_system.login('goggins', 'augurrox')
   grading_system.usr.create_assignment('assignment10', '08/15/20', 'cloud_computing')
   assert   grading_system.courses['cloud_computing']['assignments']['assignment10']['due_date'] == '08/15/20'
   assert 'goggins' in grading_system.courses['cloud_computing']['professor']
   

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
