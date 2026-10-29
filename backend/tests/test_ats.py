from app.ats import ats_score


def test_full_match():
    assert ats_score("python fastapi sql", "python sql") == 100


def test_partial_match():
    assert ats_score("python", "python sql") == 50


def test_empty_job_text():
    assert ats_score("python", "") == 0