from flask import Flask, render_template, request
from deep_translator import GoogleTranslator

from models.language_model import LanguageModel
from models.history_model import HistoryModel

from controllers.admin_controller import admin_controller
from controllers.history_controller import history_controller

from os import environ
from waitress import serve
from datetime import datetime


app = Flask(__name__)
app.template_folder = "views/templates"
app.static_folder = "views/static"

app.register_blueprint(admin_controller, url_prefix="/admin")
app.register_blueprint(history_controller, url_prefix="/history")


@app.route("/", methods=["GET"])
def index():
    return render_template(
        "index.html",
        languages=LanguageModel.list_dicts(),
        text_to_translate="O que deseja traduzir?",
        translate_from="pt",
        translate_to="en",
        translated="What do you want to translate?",
    )


@app.route("/", methods=["POST"])
def translate():
    if 'reverse' in request.form:
        return reverse()
    
    text_to_translate = request.form.get('text-to-translate')
    translate_from = request.form.get('translate-from')
    translate_to = request.form.get('translate-to')

    translator = GoogleTranslator(source=translate_from, target=translate_to)
    translated = translator.translate(text_to_translate)

    history_record = HistoryModel({
        "text": text_to_translate,
        "translated_text": translated,
        "translate_from": translate_from,
        "translate_to": translate_to,
        "timestamp": datetime.now()
        }
    )
    history_record.save()

    return render_template(
        "index.html",
        languages=LanguageModel.list_dicts(),
        text_to_translate=text_to_translate,
        translate_from=translate_from,
        translate_to=translate_to,
        translated=translated,
    )


@app.route("/reverse", methods=["POST"])
def reverse():
    text_to_translate = request.form.get('text-to-translate')
    translate_from = request.form.get('translate-from')
    translate_to = request.form.get('translate-to')

    translator = GoogleTranslator(source=translate_from, target=translate_to)
    translated = translator.translate(text_to_translate)

    history_record = HistoryModel({
        "text": text_to_translate,
        "translated_text": translated,
        "translate_from": translate_from,
        "translate_to": translate_to,
        "timestamp": datetime.now()
    })
    history_record.save()

    return render_template(
        "index.html",
        languages=LanguageModel.list_dicts(),
        text_to_translate=translated,
        translate_from=translate_to,
        translate_to=translate_from,
        translated=text_to_translate,
    )


def start_server(host="0.0.0.0", port=8000):
    if environ.get("FLASK_ENV") != "production":
        return app.run(debug=True, host=host, port=port)
    else:
        serve(app, host=host, port=port)


if __name__ == "__main__":
    start_server()
