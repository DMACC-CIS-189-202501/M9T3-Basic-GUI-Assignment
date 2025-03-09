import pytest
import ast
import importlib

# Test to check for file docstring
def test_file_docstring():
    with open('assignment.py', 'r') as file:
        tree = ast.parse(file.read())
    docstring = ast.get_docstring(tree)
    assert docstring is not None, "DMACC Student, there does not appear to be a docstring at the top of your file. Please add a docstring explaining what your code does."

# Test to check if pick_second_breakfast function exists
def test_pick_second_breakfast_exists():
    try:
        from assignment import pick_second_breakfast
        assert callable(pick_second_breakfast), "DMACC Student, the function 'pick_second_breakfast' does not appear to be defined. Please define the function."
    except ImportError:
        assert False, "DMACC Student, the function 'pick_second_breakfast' does not appear to be defined. Please define the function."

# Test to check if pick_lunch function exists
def test_pick_lunch_exists():
    try:
        from assignment import pick_lunch
        assert callable(pick_lunch), "DMACC Student, the function 'pick_lunch' does not appear to be defined. Please define the function."
    except ImportError:
        assert False, "DMACC Student, the function 'pick_lunch' does not appear to be defined. Please define the function."

# Test to check if pick_dinner function exists
def test_pick_dinner_exists():
    try:
        from assignment import pick_dinner
        assert callable(pick_dinner), "DMACC Student, the function 'pick_dinner' does not appear to be defined. Please define the function."
    except ImportError:
        assert False, "DMACC Student, the function 'pick_dinner' does not appear to be defined. Please define the function."

# Test to check if label is set to grid row 5
def test_label_grid_row():
    try:
        from assignment import label
        assert label.grid_info()['row'] == 5, "DMACC Student, the label is not set to grid row 5. Please set the label to grid row 5."
    except ImportError:
        assert False, "DMACC Student, the label does not appear to be defined. Please define the label."

# Test to check if chk_btn_second_breakfast exists and is correctly configured
def test_chk_btn_second_breakfast():
    try:
        from assignment import chk_btn_second_breakfast, pick_second_breakfast
        assert chk_btn_second_breakfast.grid_info()['row'] == 2, "DMACC Student, the 'chk_btn_second_breakfast' is not set to grid row 2. Please set it to grid row 2."
        assert chk_btn_second_breakfast.cget('text') == 'Second Breakfast', "DMACC Student, the 'chk_btn_second_breakfast' does not have the correct text. Please set the text to 'Second Breakfast'."
        assert chk_btn_second_breakfast.cget('command') == pick_second_breakfast, "DMACC Student, the 'chk_btn_second_breakfast' does not have the correct command. Please set the command to 'pick_second_breakfast'."
    except ImportError:
        assert False, "DMACC Student, the 'chk_btn_second_breakfast' does not appear to be defined. Please define the check button."

# Test to check if chk_btn_lunch exists and is correctly configured
def test_chk_btn_lunch():
    try:
        from assignment import chk_btn_lunch
        assert chk_btn_lunch.grid_info()['row'] == 3, "DMACC Student, the 'chk_btn_lunch' is not set to grid row 3. Please set it to grid row 3."
        assert chk_btn_lunch.cget('text') == 'Lunch', "DMACC Student, the 'chk_btn_lunch' does not have the correct text. Please set the text to 'Lunch'."
        try:
            from assignment import pick_lunch
            assert chk_btn_lunch.cget('command') == pick_lunch, "DMACC Student, the 'chk_btn_lunch' does not have the correct command. Please set the command to 'pick_lunch'."
        except ImportError:
            assert False, "DMACC Student, the 'pick_lunch' does not appear to be defined. Please define the function to complete the check_btn_lunch testing."
    except ImportError:
        assert False, "DMACC Student, the 'chk_btn_lunch' does not appear to be defined. Please define the check button."



# Test to check if chk_btn_dinner exists and is correctly configured
def test_chk_btn_dinner():
    try:
        from assignment import chk_btn_dinner, pick_dinner
        assert chk_btn_dinner.grid_info()['row'] == 4, "DMACC Student, the 'chk_btn_dinner' is not set to grid row 4. Please set it to grid row 4."
        assert chk_btn_dinner.cget('text') == 'Dinner', "DMACC Student, the 'chk_btn_dinner' does not have the correct text. Please set the text to 'Dinner'."
        assert chk_btn_dinner.cget('command') == pick_dinner, "DMACC Student, the 'chk_btn_dinner' does not have the correct command. Please set the command to 'pick_dinner'."
    except ImportError:
        assert False, "DMACC Student, the 'chk_btn_dinner' does not appear to be defined. Please define the check button."

if __name__ == "__main__":
    pytest.main()