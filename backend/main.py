"""All other routes without major calls"""
from flask import Flask, jsonify, redirect, session, url_for
from flask_cors import CORS
import login
import signup
import visualize
import pets
from shop import get_items
from flasgger import Swagger
from dotenv import load_dotenv
from authlib.integrations.flask_client import OAuth
import os

app = Flask(__name__)
CORS(app, supports_credentials=True, origins=["http://localhost:5173"])

swagger = Swagger(app)

load_dotenv()

AUTH0_CLIENT_ID = os.getenv("AUTH0_CLIENT_ID")
AUTH0_CLIENT_SECRET = os.getenv("AUTH0_CLIENT_SECRET")
AUTH0_DOMAIN = os.getenv("AUTH0_DOMAIN")
AUTH0_CALLBACK_URL = os.getenv("AUTH0_CALLBACK_URL")

oauth = OAuth(app)
auth0 = oauth.register(
    "auth0",
    client_id=AUTH0_CLIENT_ID,
    client_secret=AUTH0_CLIENT_SECRET,
    api_base_url=f"https://{AUTH0_DOMAIN}",
    access_token_url=f"https://{AUTH0_DOMAIN}/oauth/token",
    authorize_url=f"https://{AUTH0_DOMAIN}/authorize",
    client_kwargs={"scope": "openid profile email"},
)

# Temporary
# All returns are temporary
@app.route('/')
def home():
    """Temporary Home route which includes a message with API endpoints from other files"""
    return jsonify({
        'message': "Welcome to FindAPet API!",
        'endpoints_': {
            "application": "/application",
            "get_questionnarie": "/questionnarie",
            "post_questionnarie": "/questionnarie/results",
            "settings": "/settings_post",
            "post_settings": "/settings_get",
            "login": "/login",
            "swagger": "/apidocs"
            }
    })

@app.route("/callback")
def callback():
    """Creates a callback for auth0"""
    auth0.authorize_access_token()
    user_info = auth0.get("userinfo").json()
    session["user"] = user_info
    return redirect("/")

@app.route('/about')
def about():
    """
    About the Adoption company
    ---
    post:
        summary: About Page for the each of the memembers and point of the company
    """
    return "<h1>About page</h1>"

@app.route('/shop')
def shop():
    """Shop Page that returns h1 tag"""
    return "<h1>Shop Page<h1>"

@app.route('/faqs')
def faq():
    """FAQs page"""
    return "<h1>FAQs<h1>"

@app.route('/login', methods = ['POST'])
def post_login():
    """
    Authenticate user login
    ---
    requestBody:
        required: true
        content:
            application/json:
              schema:
                type: object
                properties:
                  username:
                    type: string
                    description: Users unique username
                  password:
                    type: string
                    description: Users password
        responses:
            '200':
                description: Authenticate result
                content:
                  application/json:
                    schema:
                        type: object
                        properties:
                            message:
                                type: string
                                description: Confirmation of successful authentication or an error
    """
    return login.login()

@app.route('/settings_get', methods=['GET'])
def g_settings():
    """
    get settings using helper file
    ---
    parameters:
        - name: dark_mode
          in: query
          required: false
          type: boolean
          description: users prefrence for dark mode
        - name: text_size
          in: query
          required: false
          type: integer
          description: display text size (default value is provided)
        - name: image_size
          in: query
          required: false
          type: integer
          decription: Image size on website
        - name: high_contrast
          in: query
          required: false
          type: boolean
          description: Indicates prefrece for high-contrast mode
    responses:
        '200':
            description: User prefrenences or error message
            content:
                application/json:
                  schema:
                    type: object
                    properties:
                      prefrences:
                        type: object
                        description: Current user settings
                      error:
                        type: string
                        description: Error messaee if prefrences retrival failed.
    """
    return visualize.settings()

@app.route('/settings_post', methods=['POST'])
def p_settings():
    """
    post settings using helper file
    ---
    requestBody:
        required: true
        content:
            application/json:
              schema:
                type: object
                properties:
                    dark_mode:
                        type: boolean
                        description: Sets dark mode prefrence
                    text_size:
                        type: integer
                        description: Updates the text size on the website
                    image_size:
                        type: integer
                        description: Updates the image size on the website
                    high_contrast:
                        type: boolean
                        description: Set high-contrast prefrence
    responses:
        '200':
            description: Prefrence update result
            contetnt:
                application/json:
                schema:
                    type: object
                    properties:
                        message:
                            type: string
                            description: confirmation of successful prefrence update or error
    """
    return visualize.post_settings()

@app.route('/application', methods=['POST'])
def p_application():
    """
    application for customer to fill out
    ---
    parameters:
        - name: Full Name
          in: query
          required: true
          type: string
          description: First and Last name
        - name: Phone Number
          in: query
          required: true
          type: integer
          description: 10 digit number to call (first form of contact)
        - name: Email
          in: query
          required: true
          type: string
          description:  email address to have a second form of contact
        - name: Address
          in: query
          required: true
          type: string
          description: Street Address
        - name: City
          in: query
          required: true
          type: string
          description: City you live in
        - name: Postal Code
          in: query
          required: true
          schema:
            type: string
          descriptiom: 10-digit postal code
    responses:
        '200':
            description: "Successful sign up message"
        """
    return signup.application()

@app.route('/questionnarie', methods=['GET'])
def g_questionnarie():
    """
    Get questionnarie using helper file
    ---
    parameters:
        - name: specified_dog_breed
          in: query
          required: true
          type: boolean
          description: Specifies if a particular breed is preferred
        - name: service_dog
          in: query
          required: true
          type: boolean
          description: Specifies if the user is looking for a service dog
        - name: hypoallergenic_dog
          in: query
          required: true
          type: boolean
          description: Specifies if a hypoallergenic is preferred
        - name: house_trained
          in: query
          required: true
          type: boolean
          description: Specifies if a house trained dog is preferred
    responses:
        '200':
            description: Quiz information retrival status
    """
    return signup.get_questionnarie()

@app.route('/questionnarie/results', methods=['POST'])
def p_questionnarie():
    """
    Post questionnarie using helper file
    ---
    requestBody:
        required: true
        content:
            application/json:
              schema:
                type: object
                properties:
                    specified_dog_breed:
                        type: boolean
                        description: Specifies if a particular breed is preferred
                    service_dog:
                        type: boolean
                        description: Specifies if the user is looking for a service dog
                    hypoallergenic_dog:
                        type: boolean
                        description: Specifies if a hypoallergenic is preferred
                    house_trained:
                        type: boolean
                        description: Specifies if a house trained dog is preferred
    resposes:
        '200':
            description: Submission status of questionnaire results
            content:
                application/json:
                  schema:
                    type: object
                    properties:
                    status:
                        type: string
                        description: Confirms successful submission of questionnaire results

    """
    return signup.post_questionnarie()

@app.route('/user', methods=['GET'])
def user_get():
    """Endpoint to fetch user data based on email address."""
    return signup.user()

@app.route('/settings_get', methods=['GET'])
def g_settings_vsl():
    """visualization settings using helper file"""
    return visualize.settings()

@app.route('/settings_got', methods=['POST'])
def p_settings_vsl():
    """visuaization settings get using get"""
    return visualize.post_settings()

@app.route('/pets_get', methods=['GET'] )
def g_pets():
    """Gets Dogs"""
    return pets.get_pets()

@app.route('/items_get', methods=['GET'])
def g_items():
    """Gets items"""
    return get_items()

if __name__ == "__main__":
    app.run(debug=True)
