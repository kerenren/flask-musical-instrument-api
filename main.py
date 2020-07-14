from model.Band import Band
from model.ElectricPiano import ElectricPiano
from model.StringInstrument import StringInstrument
from model.musician import Musician
from flask import Flask, request, abort, jsonify
import requests, json, string, random

band = None
app = Flask(__name__)
musicians_dict = {}
instruments_dict = {}


def get_random_id(length):
    letters = string.ascii_letters
    numbers = list(range(10))
    result_str = ''.join(random.choice(letters) for i in range(length)) + str(random.choice(numbers)) + (
        random.choice(letters))
    return result_str


def extract_value(values_dic, search_string):
    def check_string(value):
        if search_string in value:
            return value

    for value in values_dic.values():
        item_value = check_string(value)
        if item_value:
            print(item_value)
            return item_value
        # values_string = json.dumps(values)
        # return searchFor in values_string
        # def validate_string():
        #     for value in values_dic.values():
        #         if search_string in value:
        #             print("yes")
        #             return value
        #         else:
        #             print("Nope")
        #             return False
        # return validate_string()


def update_objs_dict(dict_name, objs_dict, length, obj_instance):
    obj_id = get_random_id(length)
    obj_dict = {obj_id: str(obj_instance)}
    objs_dict.update(obj_dict)
    print(dict_name, "has been updated to:\n", objs_dict)
    return obj_dict


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
        musician_dict = update_objs_dict("musicians_dict", musicians_dict, 6, musician)
        response = app.response_class(
            response=json.dumps(musician_dict),
            status=201,
            mimetype='application/json'
        )
        return response
    else:
        abort(404, "Missing required valid command parameter!")


# add a new instrument to a musician
@app.route("/api/instrument", methods=['POST'])
def post_instrument():
    content = request.json
    if content is None or len(content) < 4:
        return "Missing required parameters!", 404
    instrument_parameters = [content["type"], content["manufacture"], content["model"], content["musician_email"]]
    if extract_value(musicians_dict, instrument_parameters[3]) is None:
        abort(404, "The musician doesn't exist")
    if instrument_parameters[0].lower().replace(" ", "") == 'electricpiano':
        electric_piano = ElectricPiano.from_string(instrument_parameters[0], instrument_parameters[1],
                                                   instrument_parameters[2])
        band.add_instrument(instrument_parameters[3], electric_piano)
        instrument_dict = update_objs_dict("instruments_dict", instruments_dict, 4, electric_piano)
        response = app.response_class(
            response=json.dumps(instrument_dict),
            status=201,
            mimetype='application/json'
        )
        return response
    elif instrument_parameters[0].lower().replace(" ", "") == 'stringinstrument':
        string_inst = StringInstrument.from_string(instrument_parameters[0], instrument_parameters[1],
                                                   instrument_parameters[2])
        band.add_instrument(instrument_parameters[3], string_inst)
        instrument_dict = update_objs_dict("instruments_dict", instruments_dict, 4, string_inst)
        response = app.response_class(
            response=json.dumps(instrument_dict),
            status=201,
            mimetype='application/json'
        )
        return response


# Delete an instrument by musician_email, name, manufacturer, model
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


# Get all instruments
@app.route("/api/instruments", methods=['GET'])
def get_all_instruments():
    if instruments_dict == {}:
        abort(404, "instruments_dict is empty")
    return app.response_class(response=json.dumps(instruments_dict), status=200, mimetype="application/json")


# Get all instruments by a specific musician’s email
@app.route("/api/instruments/<string:email>", methods=['GET'])
def get_instruments_by_musician(email):
    if instruments_dict == {}:
        abort(404, "instruments_dict is empty")
    if extract_value(musicians_dict, email) is None:
        abort(404, "the email is not documented")
    musician = musicians[email]
    instr_obj = []
    for instr in musician.get_instruments():
        instr_obj.append(instr.__str__())
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
