# picturepy

## Deployment of a Flask Application on Render

This is a guide for deploying a Python Flask application using Gunicorn and Render, a cloud hosting service for web applications.

## Requirements

- Python 3.x
- Flask
- Gunicorn
- Git
- Render account (sign up for free at [render.com](https://render.com))

## Project Structure

Your project should have the following structure:

my_project/
|-- app.py
|-- requirements.txt
|-- runtime.txt

`app.py` should contain the Flask application code.

`requirements.txt` should list all the dependencies required by your project.

`runtime.txt` should specify the version of Python to be used.

## Deployment Steps

1. Create an account on [Render](https://render.com) and log in.

2. Create a new Web Service from the Render dashboard and choose "Python + Flask" as the template.

3. Connect your Git repository to the Render service.

4. In the `requirements.txt` file, add the following dependencies:

flask
gunicorn

Install:
`py -m pip install -r requirements.txt`

5. In the `runtime.txt` file, specify the version of Python you are using:

python-3.8.x

6. Commit and push the changes to your Git repository.

7. In the Render dashboard, navigate to the "Builds" section and trigger a manual build.

8. Once the build is successful, navigate to the "Web Services" section, and find the URL of your application under the "Endpoint" column.

9. Access your application using the endpoint URL. You should now see your Flask application running on Render.

## Conclusion

With these steps, you should now have a working Flask application deployed on Render using Gunicorn. If you encounter any issues, refer to the Render documentation or contact their support team for assistance.

https://gist.github.com/mjul/32d697b734e7e9171cdb
https://medium.com/csmadeeasy/send-and-receive-images-in-flask-in-memory-solution-21e0319dcc1
