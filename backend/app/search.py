from app.models import Resume


def search_resumes(resumes: list[Resume], query: str) -> list[Resume]:
    q = query.strip().lower()
    if not q:
        return []
    return [
        r for r in resumes
        if q in r.title.lower()
        or q in r.summary.lower()
        or any(q in skill.lower() for skill in r.skills)
    ]