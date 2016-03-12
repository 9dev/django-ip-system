# django-ip-system

Adds simple IP model to your Django project. Allows you to keep track of who created an object in your models.

## Installation

- Add `ip_system` folder to Python path.
- Add `"ip_system"` to your `INSTALLED_APPS`.

## Usage

- Add a new field to your model:


    from ip_system.fields import IpField
    
    class MyModel(models.Model):
        ...
        author_ip = IpField()
            
- Populate it while creating your model objects. Most often you want to create in from current request in your view:


    from ip_system.models import Ip

    def create_object(request):
        obj = MyModel()
        obj.author_ip = Ip.get_or_create(request=self.request)  # or Ip.objects.get_or_create(address=raw_ip_address) 
        ...

## Demo

`django-ip-system` provides a simple demo with example usage. To install it from the console, execute `fab install` command. To run it, type ``fab runserver``.

Of course, to do that you need to have `fabric` installed on your computer.

## Tests

Tests assume that Selenium's ChromeDriver can be found at:

> /usr/bin/chromedriver

It also needs correct permissions. Make sure to run:


    $ sudo chmod a+x /usr/bin/chromedriver

To run all the tests simply type:


    $ fab install
    $ fab testall

## Notes

This package was tested with Python 3.4 and Django 1.8.

## License

MIT

