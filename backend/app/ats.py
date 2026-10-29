import re


def _tokens(text: str) -> set[str]:
    return set(re.findall(r"[\w+#.]+", text.lower()))


def ats_score(resume_text: str, job_text: str) -> int:
    job = _tokens(job_text)
    if not job:
        return 0
    return round(100 * len(job & _tokens(resume_text)) / len(job))