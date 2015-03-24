from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase


__author__ = 'shay'


class TagTests(APITestCase):
    def create_tag(self, name, description):
        request_data = {"name": name, "description": description}
        return request_data, self.client.post('/tags/', request_data, format='json')

    def test_tag_create(self):
        """
        Ensure we can create a couple of tags (the correct way)
        """
        request_data, response = self.create_tag("tag1", "tag1_desc")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertDictContainsSubset(request_data, response.data)

        request_data, response = self.create_tag("tag2", "tag2_desc")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertDictContainsSubset(request_data, response.data)

        """
        Verify Tag.name field is unique
        """
        request_data, response = self.create_tag("tag1", "tag1_desc")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {'name': [u'This field must be unique.']})

        """
        Verify Tag.description does not have to be unique
        """
        request_data, response = self.create_tag("tag3", "tag1_desc")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertDictContainsSubset(request_data, response.data)

        """
        Send a GET request to make sure all 3 tags appear on our DB
        """
        #response = self.client.get('/tags/', format='json')
        response = self.client.get(reverse('tag-list'))
        self.assertTrue(response.content.count('pk') == 3)

        """
        Send a GET request for 'tag1'
        """
        #response = self.client.get(reverse('tag-detail', kwargs={'name' : 'tag1'}))
        #response = self.client.get('/tags/?name=1', format='json')
        #response = self.client.get('/tags?name=tag1', format='json')
        #response = self.client.get('/tags/', name="tag1")
        #print response
        #print response.status_code
        url = reverse('tag-detail', args=('pk','name','description'))
        print url