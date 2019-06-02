# Map_wise

### Steps

* In the root folder create a folder backend (the flask folder)   
    Inside backend folder create two folders static and templates   
    And create a main.py file

* In the root create-react-app frontend

    ```bash
    $ cd frontend
    $ npm run eject
    ```
* (Run eject allows us to configure our build process)    
    To change the default build settings    
    frontend > config > paths.js    

    ```javascript
    appBuild:resolveApp('../backend/staic/react')
    ```
    frontend > config > webpack-config.js

    change all `static/` to `   `   
    on line 473 
    ```javascript
    new HtmlWebpackPlugin(
        {
            inject:true,
            template:paths.appHtml,
            filename:"../../templates/index.html"
        }
    )
    ```

* in frontend > public > index.html add this script tag
    ```html
    <title>React App</title>
    <script>window.token = " {{token}} " </script>
    ```
    Token is passed form flask to react along with render template
    and can be accessed any where in the react app

* Access the token if frontend frontend > src > app.js
    ```html
    <p>My Token is {window.token} </p>
    ```

* in frontend > package.json   add 
    ```
    "homepage":"/static/react"
    ```

* To build the application
    ```bash
    $ cd frontend
    $ npm run build
    ```

    Building automatically creates required files and folders in static/ and templates/

* To run the app backend
    ```bash
    $ cd ..
    $ cd backend
    $ python main.py
    ```
    This will run the app on http://127.0.0.1:5000/

    ![React Homepage|5%](ss/homepage.png?raw=true "React Homepage")

* Hence to run the app
    ```
    $ cd frontend
    $ npm run build
    $ cd ../backend
    $ python main.py
    ```