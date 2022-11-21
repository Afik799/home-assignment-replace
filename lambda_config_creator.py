from jinja2 import FileSystemLoader, Environment
import json
import argparse
import urllib


class LambdaConfigCreator:
    def __init__(self):
        self.supported_env = ["dev", "prod", "test"]
        self.departments_mapping = {
            "integrations": "department1",
            "finance": "department2"
        }
        self.template_name = 'template.yaml'

    @staticmethod
    def load_jinja_env(jinja_template_name, jinja_env_path='.'):
        try:
            jinja = Environment(loader=FileSystemLoader(jinja_env_path), trim_blocks=True, lstrip_blocks=True)
            return jinja.get_template(jinja_template_name)
        except Exception as e:
            print("Couldn't find template - {}, error: {}".format(jinja_template_name, str(e)))
            raise Exception("Couldn't find template - {}, error: {}".format(jinja_template_name, str(e)))

    @staticmethod
    def load_json_file(file_name):
        try:
            with open(file_name, "r") as given_file:
                file_json = json.loads(given_file.read())
                return file_json
        except Exception as e:
            print("Couldn't open {}, error: {}".format(file_name, str(e)))
            raise Exception("Couldn't open {}, error: {}".format(file_name, str(e)))

    @staticmethod
    def write_yaml_file(file_name, file_data):
        try:
            with open(file_name, 'w') as f:
                f.write(file_data)
        except Exception as e:
            print("Couldn't create new yaml file.. error: {}".format(str(e)))
            raise Exception("Couldn't create new yaml file.. error: {}".format(str(e)))

    def creating_the_template(self, department, env):
        self.validate_params(department, env)
        json_file_path = "{}{}.json".format(self.departments_mapping.get(department), env)
        template_values_mapping = self.load_json_file(json_file_path)
        if '_route53Url_' in template_values_mapping:
            self.encode_url_spaces(template_values_mapping)
        template = self.load_jinja_env(self.template_name)
        yaml_parse = template.render(givenValues=template_values_mapping)
        return self.write_yaml_file('lambda_values.yaml', yaml_parse)

    def validate_params(self, department, env):
        if department not in self.departments_mapping:
            raise Exception("Unknown department, available departments are: {}".format(", ".join(list(self.departments_mapping.keys()))))
        if env not in self.supported_env:
            raise Exception("Unknown env, available envs are :{}".format(", ".join(self.supported_env)))

    @staticmethod
    def encode_url_spaces(template_values):
        url = template_values.get('_route53Url_')
        try:
            encoded_url = urllib.parse.quote(url)
            template_values['_route53Url_'] = encoded_url
            return template_values
        except Exception as e:
            print("Couldn't encode url {}.. error:{}".format(url, str(e)))
            raise Exception("Couldn't encode url {}.. error:{}".format(url, str(e)))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--department', required=True, help="Department name")
    parser.add_argument('--env', required=True, help="Environment name")
    args = parser.parse_args()
    lambda_config_creator = LambdaConfigCreator()
    lambda_config_creator.creating_the_template(args.department, args.env)
