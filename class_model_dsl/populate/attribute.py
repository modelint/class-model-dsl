"""
attribute.py – Create an attribute relation
"""

import logging

class Attribute:
    """
    Build all attributes for a class
    """
    def __init__(self, mmclass, parse_data):
        """Constructor"""
        self.logger = logging.getLogger(__name__)

        self.mmclass = mmclass
        self.parse_data = parse_data
        self.type = parse_data.get('type', "<unresolved>")

        attr_values = dict(
            zip(self.mmclass.model.table_headers['Attribute'],
            [self.parse_data['name'], self.mmclass.name, self.mmclass.domain, self.type])
        )
        self.mmclass.model.population['Attribute'].append(attr_values)

        for i in self.parse_data['I']:
            # Add Identifier if it is not already in the population
            if i not in self.mmclass.identifiers:
                id_values = dict(
                    zip(self.mmclass.model.table_headers['Identifier'],
                        [i, self.mmclass.name, self.mmclass.domain])
                )
                self.mmclass.model.population['Identifier'].append(id_values)
                self.mmclass.identifiers.add(i)

            # Include this attribute in the each of its identifiers
            id_attr_values = dict(
                zip(self.mmclass.model.table_headers['Identifier Attribute'],
                    [i, self.parse_data['name'], self.mmclass.name, self.mmclass.domain])
            )
            self.mmclass.model.population['Identifier Attribute'].append(id_attr_values)