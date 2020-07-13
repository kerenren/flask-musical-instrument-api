from model.Band import Band
from model.ElectricPiano import ElectricPiano
from model.StringInstrument import StringInstrument
from model.musician import Musician

band = None


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

    else:
        raise ValueError("Missing required valid command parameter!")


if __name__ == "__main__":
    band = Band()
    while True:
        try:
            inp = input("Enter musician to create(Musician, first_name, last_name, email)\n"
                        "or instrument to create (type,manufacturer,model, musician_email),\n"
                        "or delete (RemoveInstrument,type,manufacturer,model, musician_email):\n")

            if len(inp) == 0:
                raise ValueError("Missing required parameters!")

            inp = inp.strip()
            inst_content = inp.split(',')
            main(inst_content)

        except Exception as e:
            print(e)
