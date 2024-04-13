import json
import os
import sys

from extender import attribute_map
from extender import skill_map
from extender import spell_source_map
from extender import cooldown_type_map
from jinja2 import Template
from types import SimpleNamespace

def load_se_json(filename):
    with open(filename, 'r') as file:
        data = json.load(file, object_hook=lambda d: SimpleNamespace(**d))
        return data

def generate_template(character):
    with open('PartyEditor.lsx.j2') as f:
        template = Template(f.read())
        output_text = template.render(character=character,
                                      attribute_map=attribute_map,
                                      skill_map=skill_map,
                                      spell_source_map=spell_source_map,
                                      cooldown_type_map=cooldown_type_map)
    return output_text

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("""
    Usage: python convert_party_editor.py <input filename>
    Example: python convert_party_editor.py character.json
    """)
        sys.exit(2)

    filename = sys.argv[1]
    character = load_se_json(filename)
    lsx = generate_template(character)
    print(lsx)
