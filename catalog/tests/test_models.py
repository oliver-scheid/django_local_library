from django.test import TestCase

from catalog.models import Author




# Create your tests here.
class YourTestClass(TestCase):
    @classmethod
    # setUpTestData() is called once at the beginning of the test run for class-level setup. 
    # You'd use this to create objects that aren't going to be modified or changed in any of the test methods.
    def setUpTestData(cls):
        #print("setUpTestData: Run once to set up non-modified data for all class methods.")
    # Set up non-modified objects used by all test methods
        Author.objects.create(first_name='Big', last_name='Bob')

    # setUp() is called before every test function to set up any objects that may be modified by the test 
    # (every test function will get a "fresh" version of these objects).
    #def setUp(self):
        #print("setUp: Run once for every test method to setup clean data.")
        #pass

    #Below those we have a number of test methods, which use Assert functions to test whether conditions are true, 
    # false or equal (AssertTrue, AssertFalse, AssertEqual). If the condition does not evaluate as expected then 
    # the test will fail and report the error to your console.

    #Test first_name
    def test_first_name_label(self):
        # Get an author object to test
        author = Author.objects.get(id=1)
        # Get the metadata for the required field and use it to query the required field data
        field_label = author._meta.get_field('first_name').verbose_name
        # Compare the value to the expected result
        self.assertEquals(field_label, 'first name')

    def test_first_name_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('first_name').max_length
        self.assertEquals(max_length, 100)

    #Test last_name
    def test_last_name_label(self):
        # Get an author object to test
        author = Author.objects.get(id=1)
        # Get the metadata for the required field and use it to query the required field data
        field_label = author._meta.get_field('last_name').verbose_name
        # Compare the value to the expected result
        self.assertEquals(field_label, 'last name')

    def test_last_name_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('last_name').max_length
        self.assertEquals(max_length, 100)

    #Test date_of_birth
    def test_date_of_birth_label(self):
        author=Author.objects.get(id=1)
        field_label = author._meta.get_field('date_of_birth').verbose_name
        self.assertEquals(field_label, 'date of birth')

    #Test date_of_death
    def test_date_of_death_label(self):
        author=Author.objects.get(id=1)
        field_label = author._meta.get_field('date_of_death').verbose_name
        self.assertEquals(field_label, 'died')

    #Test __str__()
    def test_object_name_is_last_name_comma_first_name(self):
        author = Author.objects.get(id=1)
        expected_object_name = f'{author.last_name}, {author.first_name}'
        self.assertEquals(expected_object_name, str(author))

    #Test get_absolute_url()
    def test_get_absolute_url(self):
        author = Author.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEquals(author.get_absolute_url(), '/catalog/authors/1')


    #def test_false_is_false(self):
        #print("Method: test_false_is_false.")
        #self.assertFalse(False)

    #def test_false_is_true(self):
        #print("Method: test_false_is_true.")
        #self.assertTrue(False)

    #def test_one_plus_one_equals_two(self):
        #print("Method: test_one_plus_one_equals_two.")
        #self.assertEqual(1 + 1, 2)

    #=>NOTE: You should not normally include print() functions in your tests as shown above. 
    # We do that here only so that you can see the order that the setup functions are called in the console (in the following section).