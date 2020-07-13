from model.Band import Band
from model.ElectricPiano import ElectricPiano
from model.StringInstrument import StringInstrument
from model.musician import Musician
from flask import Flask, request, abort
import requests, json

band = None
app = Flask(__name__)
musicians = {}
instruments = {}


def main(instrument_parameters):
    if not instrument_parameters or len(instrument_parameters) < 3:
        raise ValueError("Missing required parameters!")

    if instrument_parameters[0] == 'ElectricPiano':
        electric_piano = ElectricPiano.from_string(instrument_parameters[0], instrument_parameters[1],
                                                   instrument_parameters[2])
        band.add_instrument(instrument_parameters[3], electric_piano)

    elif instrument_parameters[0] == 'StringInstrument':
        string_inst = StringInstrument.from_string(instrument_parameters[0], instrument_parameters[1],
                                                   instrument_parameters[2])
        band.add_instrument(instrument_parameters[3], string_inst)

    elif instrument_parameters[0] == 'RemoveInstrument':
        if len(instrument_parameters) < 4:
            raise ValueError("Missing required delete parameters!")

        band.remove_instrument(instrument_parameters[1], instrument_parameters[2],
                               instrument_parameters[3], instrument_parameters[4])

    elif instrument_parameters[0] == 'Musician':
        if len(instrument_parameters) < 4:
            raise ValueError("Missing required musician parameters!")

        musician = Musician.from_string(instrument_parameters[1], instrument_parameters[2],
                                        instrument_parameters[3])

        band.add_musician(musician)
        print(musicians)
    else:
        raise ValueError("Missing required valid command parameter!")


@app.route('/api/musician', methods=['POST'])
def post_musician():
    content = request.json
    if content is None or len(content) < 4:
        return "Missing required parameters!", 404
    musician_parameters = [content["musician"], content["first_name"], content["last_name"],
                           content["email"]]
    response = app.response_class(
        response=json.dumps({"musician": content}),
        status=200,
        mimetype='application/json'
    )
    main(musician_parameters)
    return response, 200


# type,manufacturer,model, musician_email
@app.route("/api/instrument", methods=['POST'])
def post_instrument():
    content = request.json
    if content is None or len(content) < 4:
        return "Missing required parameters!", 404
    instrument_parameters = [content["type"], content["manufacture"], content["model"],
                             content["musician_email"]]
    response = app.response_class(
        response=json.dumps({"instrument": content}),
        status=200,
        mimetype='application/json'
    )
    main(instrument_parameters)
    return response, 200


# RemoveInstrument,type,manufacturer,model, musician_email
@app.route("/api/delete", methods=['POST'])
def post_delete():
    content = request.json
    if content is None or len(content) < 5:
        abort(404)
    delete_parameters = [content["action"], content["name"], content["manufacture"], content["model"],
                         content["musician_email"]]
    response = app.response_class(
        response=json.dumps({"delete": content}),
        status=200,
        mimetype="application/json"
    )
    main(delete_parameters)
    return response, 200


@app.route("/api/instruments", methods=['GET'])
def get_all_instruments():
    musician_emails = list(musicians.keys())
    for item in range(len(musician_emails)):
        musician = musicians[musician_emails[item]]
        for instr in musician.get_instruments():
            instruments.update({musician_emails[item]: f"{instr}"})
    print(instruments)
    return app.response_class(response=json.dumps(instruments), status=200, mimetype="application/json")


if __name__ == "__main__":
    band = Band()
    musicians = band.musicians
    app.run(debug=True)
    try:
        pass
    except Exception as e:
        print(e)
