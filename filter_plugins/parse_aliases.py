def parse_aliases(lines):
    aliases = []
    current_alias = None

    for line in lines:
        line = line.strip()
        if line.startswith('alias name:'):
            current_alias = line.split('alias name:')[1].strip()
        elif line and current_alias:
            wwn = line.lower().replace('-', ':')
            aliases.append({'name': current_alias, 'wwn': wwn})
    return aliases

class FilterModule(object):
    def filters(self):
        return {
            'parse_aliases': parse_aliases
        }
