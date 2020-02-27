import pytest
import System

def test_login(grading_system):

   grading_system.login('akend3', '123454321' )
   assert grading_system.usr.name=='akend3'
   assert grading_system.usr.password=='123454321'


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
