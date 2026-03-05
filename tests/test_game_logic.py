from logic_utils import check_guess, get_range_for_difficulty


# --- Existing outcome tests (fixed to unpack tuple) ---

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# --- Bug fix: inverted hint messages ---

def test_too_high_message_says_go_lower():
    # When guess is too high, the hint should tell the player to go lower
    _, message = check_guess(60, 50)
    assert "LOWER" in message

def test_too_low_message_says_go_higher():
    # When guess is too low, the hint should tell the player to go higher
    _, message = check_guess(40, 50)
    assert "HIGHER" in message

def test_win_message_says_correct():
    _, message = check_guess(50, 50)
    assert "Correct" in message


# --- Bug fix: difficulty range ---

def test_easy_range():
    low, high = get_range_for_difficulty("Easy")
    assert low == 1
    assert high == 20

def test_normal_range():
    low, high = get_range_for_difficulty("Normal")
    assert low == 1
    assert high == 100

def test_hard_range():
    low, high = get_range_for_difficulty("Hard")
    assert low == 1
    assert high == 50
