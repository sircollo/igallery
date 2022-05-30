# iGallery
## Author
[Collins Sirwani](https://github.com/sircollo)

## Description
This is a personal gallery application to display photos for others to see. Its built using Django Framework

### Prerequisites
You need to install the following:
```
  Django - 4.0.4
  Virtual Environment
```

### Installation
```
  -Git clone https://github.com/sircollo/igallery

  -cd igallery

  -install virtual env

  -pip install -r requirements.txt

  -python3.8 manage.py runserver

```
## Technologies Used

  * Python3.8
  * Django 4.0.4
  * Bootstrap
  * PostgreSQL
  * CSS
  * Heroku

## Running tests
```
  -python3.8 manage.py test gallery
```

### Breakdown of tests
Unittest to test model classes methods like save, update and delete. e.g
```
  def test_save_method(self):
    self.image.save_image()
    images = Image.objects.all()
    self.assertTrue(len(images)>0)
```
The above tests if an image instance can be saved.

## User Story
A user can:

  * View different photos that interest me.
  * Click on a single photo to expand it and view its details
  * Search for different categories of photos. (ie. Travel, Food)
  * Copy a link to the photo to share with my friends.
  * View photos based on the location they were taken.

## BDD
Feature: Test images can be added in the Django Admin

Scenario: Django Admin can add new images

  Given I am on the Django Admin

  When I click on the "Add" button

  Then I am on the add new image input form

  Then I add new image details

  Then I click save

### Deployment
Read here on how to [Deploy](https://gist.github.com/newtonkiragu/42f2500e56d9c2375a087233587eddd0)


### Preview

[Live Link](https://le-igallery.herokuapp.com/)


### License

[MIT License](https://github.com/sircollo/igallery/blob/main/license)

Copyright (c) 2022
