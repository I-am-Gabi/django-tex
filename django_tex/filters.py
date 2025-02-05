from django.utils.formats import localize_input
from django.template.defaultfilters import register


def do_linebreaks(value):
    return value.replace('\n', '\\\\\n')


def do_latex_escape(value):
    return (str(value)
            .replace("\\", "\\textbackslash ")
            .replace('&', '\\&')
            .replace('$', '\\$')
            .replace('%', '\\%')
            .replace('#', '\\#')
            .replace('_', '\\_')
            .replace('{', '\\{')
            .replace('}', '\\}')
            )


def do_capitalize(value):
    return str(value).capitalize()


def do_join(value):
    return (', '.join(value))


tex_specific_filters = {
    'localize': localize_input,
    'linebreaks': do_linebreaks,
    'latex_escape': do_latex_escape,
    'capitalize': do_capitalize,
    'join': do_join,
}

FILTERS = register.filters.copy()
FILTERS.update(tex_specific_filters)
