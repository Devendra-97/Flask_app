import pytest
import EndpointProcess
from mock_data import MockCursor,MockValue

@pytest.mark.parametrize(
    "update_result, resp", [
        (True, True),
        (False, False)
    ]
)
def test_add_new_question(mocker, update_result, resp):
    """
    test add_new_question
    Case 1: Update successful
    Case 2: Failed to update
    """
    mocker.patch("flask_restx.Api.payload", return_value={})
    mocker.patch("backend.ques_collection.find", return_value=MockCursor())
    mocker.patch("backend.ques_collection.insert", return_value={})
    mocker.patch("backend.ques_collection.update", return_value=update_result)
    response = EndpointProcess.add_new_question()
    assert response == resp


@pytest.mark.parametrize(
    "update_result, resp", [
        (True, True),
        (False, False)
    ]
)    

def test_add_new_answer(mocker, update_result, resp):
    """
    test add_new_answer
    Case 1: Update successful
    Case 2: Failed to update
    """
    mocker.patch("flask_restx.Api.payload", return_value={})
    mocker.patch("backend.ans_collection.find", return_value=MockCursor())
    mocker.patch("backend.ans_collection.insert", return_value={})
    mocker.patch("backend.ans_collection.update", return_value=update_result)
    response = EndpointProcess.add_new_answer()
    assert response == resp 




def test_get_all(mocker):
   
    mocker.patch("backend.ques_collection.find",return_value={"question":"Q","topic":["a","b"]})
    mocker.patch("json.dumps", return_value="")
    mocker.patch("json.loads",return_value={})
    mocker.patch("backend.ans_collection.find",return_value={"answer":"A!","qid":"2"})
    mocker.patch("json.dumps", return_value="")
    mocker.patch("json.loads",return_value={})
    response = EndpointProcess.get_all()
    assert response == {}




@pytest.mark.parametrize(
    "k,resp", [
        ("Please Enter Correct Id", "Please Enter Correct Id")

    ]
) 

def test_search_by_id(mocker,k,resp):
    mocker.patch("backend.ques_collection.find", return_value=MockCursor())
    mocker.patch("backend.ans_collection.find", return_value=MockCursor())
    mocker.patch("json.dumps", return_value=MockValue())
    mocker.patch("json.loads",return_value=MockValue())
    response=EndpointProcess.search_by_id("_id")
    assert response== resp


# @pytest.mark.parametrize(
#     "k,resp", [
#         ({"topic": ["c","a"]}, True)
#     ]
# ) 

def test_search_by_topic(mocker):
    mocker.patch("flask_restx.Api.payload", return_value={})
    mocker.patch("backend.ques_collection.find",return_value={})
    mocker.patch("json.dumps", return_value="")
    mocker.patch("json.loads",return_value={})
    mocker.patch("backend.ans_collection.find",return_value=MockValue())
    
    
   
    response=EndpointProcess.search_by_topic()
    assert response == []







