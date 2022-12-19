import json


def load_candidates(filename="candidates.json"):
    with open(filename, "r", encoding='utf-8') as f:
      return json.load(f)


def get_candidates_all():
    return load_candidates()


def get_candidate_by_id(id):
    for candidate in load_candidates():
        if id == candidate["id"]:
            return candidate
    return


def get_candidates_by_name(candidate_name):
    result = []
    for candidate in load_candidates():
        if candidate_name.lower() in candidate['name'].lower():
            result.append(candidate)
    return result


def get_candidates_by_skill(skill_name):
    candidates = []
    for candidate in load_candidates():
        if skill_name.lower() in candidate['skills'].lower().split(', '):
            candidates.append(candidate)
    return candidates