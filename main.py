from Brazil.br_generator import br_generator
from Peru.pe_generator import pe_generator
from Colombia.co_generator import co_generator
from Ecuador.ec_generator import ec_generator
from Mexico.mx_generator import mx_generator
from DominicanRepublic.do_generator import do_generator


def main():
    going = True
    while going:
        country = input("What country do you want to generate the Government ID(BR,CO,DO,EC,PE,MX): ")
        if country == 'br' or country == 'BR':
            br_generator()
        elif country == 'co' or country == 'CO':
            co_generator()
        elif country == 'do' or country == 'DO':
            do_generator()
        elif country == 'ec' or country == 'EC':
            ec_generator()
        elif country == 'pe' or country == 'PE':
            pe_generator()
        elif country == 'mx' or country == 'MX':
            mx_generator()
        else:
            print('Country incorrect')
        status = input("Want to generate a new Government ID(y/n)? ")
        if status == "n" or status == "N":
            going = False


if __name__ == '__main__':
    main()
