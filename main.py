from model.Band import Band
from model.ElectricPiano import ElectricPiano
from model.StringInstrument import StringInstrument
from model.musician import Musician
from flask import Flask, request, abort, jsonify
import requests, json

band = None
app = Flask(__name__)
musicians = {}
instruments = {}

@app.route('/api/musician', methods=['POST'])
def post_musician():
    content = request.json
    if content is None or len(content) < 4:
        return "Missing required parameters!", 404  # report error by return
    musician_parameters = [content["musician"], content["first_name"], content["last_name"],
                           content["email"]]
    if musician_parameters[0].lower() == 'musician':
        if len(musician_parameters) < 4:
            abort(404, "Missing required musician parameters!")  # report error by abort
        musician = Musician.from_string(musician_parameters[1], musician_parameters[2],
                                        musician_parameters[3])
        band.add_musician(musician)
        print("musicians instance", str(musician))
        response = app.response_class(
            response=json.dumps({"musician_id": str(musician)}),
            status=201,
            mimetype='application/json'
        )
        return response
    else:
        abort(404, "Missing required valid command parameter!")


# type,manufacturer,model, musician_email
@app.route("/api/instrument", methods=['POST'])
def post_instrument():
    content = request.json
    if content is None or len(content) < 4:
        return "Missing required parameters!", 404
    instrument_parameters = [content["type"], content["manufacture"], content["model"], content["musician_email"]]
    if instrument_parameters[0].lower().replace(" ", "") == 'electricpiano':
        electric_piano = ElectricPiano.from_string(instrument_parameters[0], instrument_parameters[1],
                                                   instrument_parameters[2])
        band.add_instrument(instrument_parameters[3], electric_piano)

        response = app.response_class(
            response=json.dumps({"ElectricPiano": str(electric_piano)}),
            status=201,
            mimetype='application/json'
        )
        return response
    elif instrument_parameters[0].lower().replace(" ", "") == 'stringinstrument':
        string_inst = StringInstrument.from_string(instrument_parameters[0], instrument_parameters[1],
                                                   instrument_parameters[2])
        band.add_instrument(instrument_parameters[3], string_inst)
        response = app.response_class(
            response=json.dumps({"StringInstrument": str(string_inst)}),
            status=201,
            mimetype='application/json'
        )
        return response


# RemoveInstrument,type,manufacturer,model, musician_email
@app.route("/api/delete", methods=['POST'])
def post_delete():
    content = request.json
    if content is None or len(content) < 5:
        abort(404)
    delete_parameters = [content["action"], content["name"], content["manufacture"], content["model"],
                         content["musician_email"]]
    if len(delete_parameters) < 4:
        abort(404, "Missing required delete parameters!")

    band.remove_instrument(delete_parameters[1], delete_parameters[2],
                           delete_parameters[3], delete_parameters[4])

    response = app.response_class(
        response=json.dumps({"delete": content}),
        status=201,
        mimetype="application/json"
    )
    return response


@app.route("/api/instruments", methods=['GET'])
def get_all_instruments():
    if musicians == {}:
        abort(404, "missing musician dict is empty")
    musician_emails = list(musicians.keys())
    for item in range(len(musician_emails)):
        musician = musicians[musician_emails[item]]
        for instr in musician.get_instruments():
            instruments.update({musician_emails[item]: f"{instr}"})
    print(instruments)
    return app.response_class(response=json.dumps(instruments), status=200, mimetype="application/json")


@app.route("/api/instruments/<string:email>", methods=['GET'])
def get_instruments_by_musician(email):
    if musicians == {}:
        abort(404, "missing musician dict is empty")
    musician = musicians[email]
    instr_obj = {}
    for instr in musician.get_instruments():
        instr_obj.update({f"{email}": f"{instr}"})
    print(instr_obj)
    return app.response_class(response=json.dumps(instr_obj), status=200, mimetype="application/json")


if __name__ == "__main__":
    band = Band()
    musicians = band.musicians
    app.run(debug=True)
    try:
        pass
    except Exception as e:
        print(e)
