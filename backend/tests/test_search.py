from app.models import Resume
from app.search import search_resumes

RESUMES = [
    Resume("a@x.com", "Python Developer", skills=["Python", "FastAPI"]),
    Resume("b@x.com", "Frontend Developer", skills=["React", "TypeScript"]),
]


def test_search_by_title():
    assert len(search_resumes(RESUMES, "frontend")) == 1


def test_search_by_skill():
    assert search_resumes(RESUMES, "fastapi")[0].owner_email == "a@x.com"


def test_empty_query_returns_nothing():
    assert search_resumes(RESUMES, "  ") == []