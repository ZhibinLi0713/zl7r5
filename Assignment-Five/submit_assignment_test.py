import pytest
import System
import Staff
import Professor
import Student

def test_drop_student(grading_system):

   grading_system.login('yted91', 'imoutofpasswordnames')
   grading_system.usr.submit_assignment('cloud_computing', 'assignment3', 'this is a submission', '03/29/20')
   grading_system.load_data()
   assert grading_system.users['yted91']['courses']['cloud_computing']['assignment3']['submission'] =='this is a submission'
   assert grading_system.users['yted91']['courses']['cloud_computing']['assignment3']['ontime'] == True


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
