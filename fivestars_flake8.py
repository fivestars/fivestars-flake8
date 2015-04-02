import ast


class TestIt(object):
    name = 'testit'
    version = '1.0.0'

    def __init__(self, tree, filename):
        self.tree = tree
        self.filename = filename

    def run(self):
        return []


class MutableDefaultArgumentValues(object):
    """ It's 100% perfect, but it will catch the most common cases of using a mutable type as a
        default argument value.
    """
    name = 'mutabledefaults'
    version = '1.0.0'

    def __init__(self, tree, filename):
        self.tree = tree
        self.filename = filename

    @classmethod
    def add_options(cls, parser):
        parser.add_option('--allow-type', action='append', type='string', dest='allowed_types')
        parser.config_options.append('allowed-types')

    @classmethod
    def parse_options(cls, options):
        cls.allowed_types = options.allowed_types if options.allowed_types else []

    def run(self):
        for node in ast.walk(self.tree):
            if isinstance(node, ast.FunctionDef):
                for default in node.args.defaults:
                    if isinstance(default, ast.Dict) or isinstance(default, ast.List):
                        yield (
                            default.lineno, default.col_offset,
                            'FS10 Mutable type as default argument: %s' % type(default).__name__,
                            type(self)
                        )
                        continue
                    elif (isinstance(default, ast.Name) or
                            isinstance(default, ast.Num) or
                            isinstance(default, ast.Str) or
                            isinstance(default, ast.Tuple)):
                        # safe
                        continue
                    elif (isinstance(default, ast.BinOp) or
                            isinstance(default, ast.Attribute)):
                        # Could need further investigation
                        continue
                    elif isinstance(default, ast.Call):
                        if default.func.id == 'set':
                            yield (
                                default.lineno, default.col_offset,
                                'FS10 Mutable type as default argument: %s' % 'Set',
                                type(self)
                            )
                            continue
                    # Notify fivestars-flake8 maintainer to update list of acceptable types
                    if type(default).__name__ not in self.allowed_types:
                        yield (
                            default.lineno, default.col_offset,
                            'FS11 Unrecognized type as default argument: %s' % type(default).__name__,
                            type(self)
                        )
