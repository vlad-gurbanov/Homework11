from flask import Flask, render_template
import utils

app = Flask(__name__)


@app.route("/")
def index():
    candidates = utils.get_candidates_all()
    return render_template('list.html', candidates=candidates)


@app.route("/candidates/<int:id>")
def get_candidate_by_id(id):
    candidate = utils.get_candidate_by_id(id)
    return render_template('card.html', candidate=candidate)


@app.route("/search/<candidate_name>")
def get_candidates_by_name(candidate_name):
    candidates = utils.get_candidates_by_name(candidate_name.lower())
    return render_template('search.html', candidates=candidates, count_candidates=len(candidates))


@app.route("/skill/<skill>")
def get_candidates_by_skill(skill):
    candidates = utils.get_candidates_by_skill(skill.lower())
    return render_template('skill.html', candidates=candidates, count_candidates=len(candidates))


if __name__ == '__main__':
    app.run(port=5003, debug=True)
