import argparse
from deep_translator import GoogleTranslator

LANGUAGE_ES = 'es'
LANGUAGE_EN = 'en'
MAX_LEN = 70

def generate_branch_name(ticket_number, desc):
    desc = translate_to_english(desc)
    normalized_desc = generate_normalize_desc(desc)
    options =  {
        "Feat": f"feat/{ticket_number}-{normalized_desc}",
        "Bug": f"fix/{ticket_number}-{normalized_desc}",
        "Pre Feat": f"feat/{ticket_number}-{normalized_desc}_pre",
        "Pre Bug": f"fix/{ticket_number}-{normalized_desc}_pre",
        "Prod Feat": f"feat/{ticket_number}-{normalized_desc}_prod",
        "Prod Bug": f"fix/{ticket_number}-{normalized_desc}_prod",
        "Commit for dev/pre Feat": f"feat:[{ticket_number}]-{normalized_desc}",
        "Commit for dev/pre Bug": f"fix:[{ticket_number}]-{normalized_desc}",
        "Commit for prod hotfix Feat": f"feat:[PATCH][{ticket_number}]-{normalized_desc}",
        "Commit for prod hotfix Bug": f"fix:[PATCH][{ticket_number}]-{normalized_desc}",
    }

    for key, value in options.items():
        print(f"{key}:\n {value}")

def generate_normalize_desc(desc):
    normalized_desc = desc.lower().replace(' ', '-').replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u')
    if len(normalized_desc) > MAX_LEN:
        normalized_desc = normalized_desc[:MAX_LEN]
    return normalized_desc

def translate_to_english(description):
    translator = GoogleTranslator(source=LANGUAGE_ES, target=LANGUAGE_EN)
    return translator.translate(description)
 
def run():
    parser = argparse.ArgumentParser(description='Branch Name Generator')
    subparsers = parser.add_subparsers(dest='command')
    create_parse = subparsers.add_parser('create', help="create a new name of branch")
    create_parse.add_argument('-t', '--ticket', required=True,type=int, help="number of ticket")
    create_parse.add_argument('-d', '--description', required=True, help="description of ticket")
    args = parser.parse_args()

    generate_branch_name(args.ticket,args.description)
if __name__ == "__main__":
    run()