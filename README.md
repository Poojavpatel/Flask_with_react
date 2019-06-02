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
            filename:path.resolve("../../templates/index.html")
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
