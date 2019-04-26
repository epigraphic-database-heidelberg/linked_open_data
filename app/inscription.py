from flask import (
    Blueprint, render_template
)
from .models.Inscription import Inscription


bp = Blueprint('inscription', __name__)


@bp.route('/edh/inschrift/<hd_nr>')
def lod_detail_view(hd_nr):
    results = Inscription.query(hd_nr)
    for result in results["results"]["bindings"]:
        print(result)
    return render_template('inscription/detail_view.html', title="Epigraphic Text Database: Detail View", data=hd_nr)
