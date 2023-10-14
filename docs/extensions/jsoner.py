from docutils import nodes
from docutils.parsers.rst import Directive, roles
import json

class FunctionsJsonDirective(Directive):
    has_content = True

    def run(self):
        json_content = '\n'.join(self.content)
        try:
            data = json.loads(json_content)
        except json.JSONDecodeError as e:
            error_node = self.state.document.reporter.error(
                f"JSON parsing error (functions.json): {e}",
                nodes.literal
            )
            return [error_node]

        json_node = nodes.literal_block(json_content, json_content)
        return [json_node]

def functions_json_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    try:
        data = json.loads(text)
        pretty_json = json.dumps(data, indent=4)
        json_node = nodes.literal_block(pretty_json, pretty_json)
        return [json_node], []
    except json.JSONDecodeError as e:
        error_node = inliner.reporter.error(
            f"JSON parsing error (functions.json): {e}", line=lineno)
        return [error_node], []

class ClassesJsonDirective(Directive):
    has_content = True

    def run(self):
        json_content = '\n'.join(self.content)
        try:
            data = json.loads(json_content)
        except json.JSONDecodeError as e:
            error_node = self.state.document.reporter.error(
                f"JSON parsing error (classes.json): {e}",
                nodes.literal
            )
            return [error_node]

        json_node = nodes.literal_block(json_content, json_content)
        return [json_node]

def classes_json_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    try:
        data = json.loads(text)
        pretty_json = json.dumps(data, indent=4)
        json_node = nodes.literal_block(pretty_json, pretty_json)
        return [json_node], []
    except json.JSONDecodeError as e:
        error_node = inliner.reporter.error(
            f"JSON parsing error (classes.json): {e}", line=lineno)
        return [error_node], []

def setup(app):
    app.add_directive('functions_json', FunctionsJsonDirective)
    app.add_directive('classes_json', ClassesJsonDirective)
    roles.register_canonical_role('functions_json', functions_json_role)
    roles.register_canonical_role('classes_json', classes_json_role)
