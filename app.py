"""Smart Sort - QR-based waste segregation guide and bin reporting."""
import os
from functools import wraps

from flask import (Flask, abort, flash, redirect, render_template, request,
                   session, url_for)

import db
from content import CATEGORIES, STATUSES, UI


def create_app(config=None):
    app = Flask(__name__)
    app.config.update(
        SECRET_KEY=os.environ.get("SECRET_KEY", "dev-only-change-me"),
        DATABASE=os.environ.get("DATABASE_URL", "smartsort.db"),
        ADMIN_PASSWORD=os.environ.get("ADMIN_PASSWORD", "admin"),
    )
    if config:
        app.config.update(config)
    if not os.path.exists(app.config["DATABASE"]):
        db.init_db(app.config["DATABASE"], load_sample=True)
    app.teardown_appcontext(db.close_db)

    def lang():
        l = request.values.get("lang", "en")
        return l if l in ("en", "ta") else "en"

    def admin_required(view):
        @wraps(view)
        def wrapped(*a, **kw):
            if not session.get("admin"):
                return redirect(url_for("login"))
            return view(*a, **kw)
        return wrapped

    @app.context_processor
    def inject():
        return dict(lang=lang(), UI=UI, CATEGORIES=CATEGORIES, STATUSES=STATUSES)

    @app.route("/")
    def index():
        bins = db.get_db().execute("SELECT * FROM bins ORDER BY location, category").fetchall()
        return render_template("index.html", bins=bins)

    @app.route("/bin/<code>")
    def guide(code):
        b = db.get_db().execute("SELECT * FROM bins WHERE code=?", (code,)).fetchone()
        if b is None:
            abort(404)
        return render_template("guide.html", bin=b, cat=CATEGORIES[b["category"]],
                               sent=request.args.get("sent"))

    @app.route("/report", methods=["POST"])
    def report():
        code = request.form.get("bin_code", "")
        status = request.form.get("status", "")
        note = request.form.get("note", "").strip()[:300]
        d = db.get_db()
        if status not in STATUSES or d.execute("SELECT 1 FROM bins WHERE code=?", (code,)).fetchone() is None:
            abort(400)
        d.execute("INSERT INTO reports (bin_code, status, note) VALUES (?,?,?)", (code, status, note))
        d.commit()
        return redirect(url_for("guide", code=code, lang=lang(), sent=1))

    @app.route("/login", methods=["GET", "POST"])
    def login():
        if request.method == "POST":
            if request.form.get("password") == app.config["ADMIN_PASSWORD"]:
                session["admin"] = True
                return redirect(url_for("dashboard"))
            flash("Wrong password.")
        return render_template("login.html")

    @app.route("/logout")
    def logout():
        session.clear()
        return redirect(url_for("index"))

    @app.route("/dashboard")
    @admin_required
    def dashboard():
        d = db.get_db()
        open_reports = d.execute(
            "SELECT r.*, b.location, b.category FROM reports r JOIN bins b ON b.code=r.bin_code "
            "WHERE r.resolved=0 AND r.status!='ok' ORDER BY r.created_at DESC").fetchall()
        by_status = d.execute("SELECT status, COUNT(*) n FROM reports GROUP BY status").fetchall()
        weight = d.execute(
            "SELECT b.category, ROUND(SUM(w.weight_kg),1) kg FROM waste_logs w "
            "JOIN bins b ON b.code=w.bin_code GROUP BY b.category").fetchall()
        bins = d.execute("SELECT code, location FROM bins ORDER BY code").fetchall()
        wmax = max([r["kg"] for r in weight], default=1) or 1
        smax = max([r["n"] for r in by_status], default=1) or 1
        return render_template("dashboard.html", open_reports=open_reports, by_status=by_status,
                               weight=weight, bins=bins, wmax=wmax, smax=smax)

    @app.route("/log", methods=["POST"])
    @admin_required
    def log_weight():
        try:
            kg = float(request.form.get("weight_kg", ""))
            if kg < 0:
                raise ValueError
        except ValueError:
            abort(400)
        d = db.get_db()
        if d.execute("SELECT 1 FROM bins WHERE code=?", (request.form.get("bin_code"),)).fetchone() is None:
            abort(400)
        d.execute("INSERT INTO waste_logs (bin_code, weight_kg) VALUES (?,?)",
                  (request.form["bin_code"], kg))
        d.commit()
        return redirect(url_for("dashboard"))

    @app.route("/resolve/<int:rid>", methods=["POST"])
    @admin_required
    def resolve(rid):
        d = db.get_db()
        d.execute("UPDATE reports SET resolved=1 WHERE id=?", (rid,))
        d.commit()
        return redirect(url_for("dashboard"))

    return app


if __name__ == "__main__":
    create_app().run(debug=os.environ.get("FLASK_DEBUG") == "1", host="0.0.0.0")
