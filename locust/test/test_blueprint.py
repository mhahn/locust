from testcases import LocustTestCase
from locust.blueprint import Blueprint


class TestBlueprint(LocustTestCase):

    def test_blueprint_get_toplevel_value(self):
        blueprint = Blueprint({'event': {'primary_key': 1234}})
        self.assertEqual(blueprint.event.primary_key, 1234)

    def test_blueprint_get_nested_value(self):
        blueprint = Blueprint({'event': {'nested': {'value': 1234}}})
        self.assertEqual(blueprint.event.nested.value, 1234)

    def test_blueprint_get_value_from_list(self):
        blueprint = Blueprint({'tickets': [{'primary_key': 1234}]})
        self.assertEqual(blueprint.tickets._0.primary_key, 1234)

    def test_blueprint_raises_attribute_error(self):
        with self.assertRaises(AttributeError):
            blueprint = Blueprint({})
            blueprint.nonexistant

    def test_blueprint_invalid_list_index_raises_attribute_error(self):
        with self.assertRaises(AttributeError):
            blueprint = Blueprint({})
            blueprint._k1

    def test_blue_print_update(self):
        blueprint = Blueprint({})
        blueprint.update({'event': {'primary_key': 1234}})
        self.assertEqual(blueprint.event.primary_key, 1234)

    def test_blue_print_clone(self):
        data = {'test': 1}
        blueprint1 = Blueprint(data)
        blueprint2 = blueprint1.clone()
        blueprint2.update({'test': 2})
        self.assertNotEqual(blueprint1.test, blueprint2.test)
