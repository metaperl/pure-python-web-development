# Class B Frameworks 

Class B frameworks are perfect for limited-scope projects, but don't complain when you lack features!



## Taipy

[Taipy](https://www.taipy.io) is a strong Class B framework. The enterprise version could qualify as Class A because it supports 
[authentication and authorization](https://docs.taipy.io/en/release-2.1/manuals/about/).

My one concern is the shorthand for HTML development: can one do full-fledged detailed HTML/CSS development with a Pythonic interface? My skimming of the docs says no, but I could be wrong.

### Resources and discussions

[github link](https://github.com/avaiga/taipy)
["Taipy: an Open-Source Python Only Web App Builder Library"](https://www.reddit.com/r/Python/comments/13iawcm/taipy_an_opensource_python_only_web_app_builder/)

## Highcharts for Python

The [Highcharts for Python Toolkit](https://github.com/highcharts-for-python) is a set of Python libraries that provide a Python wrapper for [the Highcharts suite of JavaScript data visualization libraries](https://www.highcharts.com/), with full integration across the Python ecosystem.

The toolkit features native integrations with:

* Jupyter Labs/Notebook. You can now produce high-end and interactive plots and renders using the full suite of Highcharts visualization capabilities.
* Pandas. Automatically produce data visualizations from your Pandas dataframes
* PySpark. Automatically produce data visualizations from data in a PySpark dataframe.
* ...and more library-specific integrations, including GeoPandas, PyShp, Topjson, Geojson, Asana, and more

Highcharts for Python provides Python object representation for all of the JavaScript objects defined in the Highcharts (JavaScript) API. It provides automatic data validation, and exposes simple and standardized methods for serializing those Python objects back-and-forth to JavaScript object literal notation.


## Reacton – A pure Python port of React for ipywidgets
 ipywidgets is a library for writing interactive widgets in the Jupyter notebook.

Reacton is a pure Python library, that implements a similar API as ReactJS. Instead of rendering to the DOM, it renders to ipywidgets. The ipywidget library is then responsible for rendering in the front end (which could use ReactJS, Vue, or even jQuery).

### Discussion
initial reddit thread.
“Advance your ipywidget app development with Reacton — A pure Python port of React for faster development”


## Streamsync 

Let's first see [what streamsync has to say about itself](https://github.com/ramedina86/streamsync):


Streamsync is an open-source framework for creating data apps. Build user interfaces using a visual editor; write the backend code in Python. Check out a [live demo](https://hello.streamsync.cloud/) of an app.

![Streamsync Builder screenshot](https://raw.githubusercontent.com/ramedina86/streamsync/master/docs/docs/public/sc1.png)

### It's fast.

- Streamsync enables significantly lower response times, when compared to Streamlit.
- It only runs the user script once.
- It uses WebSockets to keep frontend and backend states in sync.

### It's neat.

- Streamsync uses state-driven, reactive user interfaces. A data app's user interface is strictly separated from its logic.
- It uses a consistent yet customisable UI design system.
- No caching needed; the script runs once and things remain in memory. You can use globals and module attributes to store app-wide data.
- Predictable flow of execution. Event handlers are plain, easily testable Python functions. No re-runs, no strange decorators.

### Documentation

Documentation is available online at [streamsync.cloud](https://streamsync.cloud).

### Now for my impressions

Streamsync is not the first product to offer a visual UI for building apps. [Anvil](https://anvil.works) is a mature framework that offers that and is a Class A framework.

Anvil handles user sessions out of the box in a seamless fashion, [Streamsync does not](https://www.reddit.com/r/Python/comments/135i584/comment/jim5ptr/?utm_source=share&utm_medium=web2x&context=3). 

[Datapane](https://docs.datapane.com) allows one to build data apps and it can be embedded in Flask or Django easily. Streamsync cannot. 

[Atri](https://metaperl.github.io/pure-python-web-development/class-a.html#atri) is a Class A framework that allows for visual UI building. 

### Resources and Discussion

* ["Streamsync: UI editor + Python"](https://www.reddit.com/r/Python/comments/135i584/streamsync_ui_editor_python/)
* ["Like Streamlit, but faster and with a visual UI editor. Streamsync."](https://medium.com/@ramiromedina/streamsync-like-streamlit-but-faster-and-with-a-visual-ui-editor-9f98ad17adf)
* [Someone asked about how Streamsync compares with NiceGUI. Someone more experienced than me is requested to enter the conversation.](https://www.reddit.com/r/nicegui/comments/136jj4u/someone_asked_about_how_streamsync_compares_with/)

## Gradio
Gradio can wrap almost any Python function with an easy-to-use user interface. The function could be anything from image enhancer to a tax calculator  but most commonly is the prediction function of a pre-trained machine learning model.

Gradio allows one to quickly create interfaces (either from the console or a Jupyter notebook or https://huggingface.co/spaces)  and `launch()` them.

But it is also possible to customize how UI components look and/or behave.

From my perspective, the weaknesses are:

It is not clear how to integrate output from Gradio into a full-blown web-app.
It offers password-based authentication only.
No support for authorization
### Related Publications
“Making Neural Search Queries Accessible to Everyone with Gradio”

“Dashboard for audio summarization, sentiment analysis, and more!” – article link




## Shiny for Python
Shiny for Python has a clean API and good documentation. Like many class B solutions, it lacks the features for complete web applications – authentication, authorization and sessioning.

## Htag
Htag is a very powerful and elegantly implemented pure-python-web-dev solution. It is the most recent solution by a prolific, talented and motivated author. He gained a lot of experience from his previous products, Gtag and Wyc.

The reason it is Class B is because it is a builder. A very flexible and powerful builder with the ability to be run in ALL of following deployment scenarios:

For a desktop app : You can use the PyWebView runner, which will run the UI in a pywebview container (or “ChromeApp runner”, in a local chrome app mode).
For a web app : You can use the WebHTTP runner, which will run the UI in a web server, and serve the UI on client side, in a browser.
For a android app : You can use the AndroidApp runner, which will run the UI in a kiwi webview thru tornado webserver, and can be embedded in an apk (recipes)
For a pyscript app : you can use the PyScript runner, which will run completly in client side
In fact any display portal which can render html/js/css, whether it be a browser, a pywebview, an android/apk, or anything based on cef, just needs an htag runner for htag to be able to render to it.

As the author states:

Yes … the promise is here : it’s a GUI toolkit for building “beautiful” applications for mobile, web, and desktop from a single codebase.

https://github.com/manatlan/htag#readme
### Demo
A very impressive and expressive demo once it loads.

### Discussions
“Using htag to create a **matplotlib** app for desktop, web or mobile”
“HTag : an IRL mobile app for android : a tricount clone … using py3“
HTag : A new GUI tookit for web/desktop/android from a single codebaseFirst frontend lib for pyscript ;-)”
“htag 0.4.7 (a gui/frontend lib which works very well in pyscript)”
## Neutron
Neutron allows developers to build native Python apps along with CSS and HTML for frontend design. Based on pywebview for it’s native GUI window and JavaScript-Python communication.

## Vue.Py
Vue.py wraps Vue.js. Vue.py is based on Brython and the author is clear about what limitations that currently imposes. The lack of a gallery of applications and small userbase lead to this being a Class B solution.

## JustPy – another Vue.js wrapper
https://justpy.io/

Justpy frees the developer from being concerned about the difference between front-end and back-end development. From the [README](https://github.com/elimintz/justpy):

### JustPy’s backend is built using:

starlette – “a lightweight ASGI framework/toolkit, which is ideal for building high performance asyncio services”.
uvicorn – “a lightning-fast ASGI server, built on uvloop and httptools“.
JustPy’s frontend (which is transparent to JustPy developers) is built using:

Vue.js – “The Progressive JavaScript Framework”
The way JustPy removes the frontend/backend distinction is by intercepting the relevant events on the frontend and sending them to the backend to be processed.

I would rate JustPy over Vue.py for a Vue solution based on apparent maturity. But neither provides solutions for the common issues of a fully mature web application framework.

A recent reddit post shows the commitment of the original author to long-term support of the project. That being said, the lack of response by the author did lead to a significant fork based of JustPy based on Svelte instead of Vue.js.

### Built NiceGUI
JustPy was the library underlying NiceGUI.

### Publications:
“justpy open source community is growing”
## PyFyre
And I plagiarize from the official Github:

Component-based framework. Developers who have experience in using other frontend frameworks should feel quite at home when using PyFyre.
Truly reactive. PyFyre’s virtual DOM allows for simple and efficient state management.
Quick navigation. Navigation between pages is quick with PyFyre’s single-page application design.
Pythonic code with static typing. Developing with PyFyre is much easier with its type hinting and Pythonic style of coding.
Asynchronous programming. Run non-blocking functions out of the box.
CPython interoperability. Developers can limitedly use CPython packages on the client-side web.
JavaScript interoperability. Allowing developers to leverage NPM packages and integrate with existing JavaScript applications.
Pure Python. Build web apps without ever touching other languages like HTML and JavaScript.
And more!
### Discussions
Python Frontend Framework for Building Websites
### Built on Brython
## Transcrypt
http://transcrypt.org/ is a Javascript generator that opts for integration with Javascript libraries instead of Python libraries. The book React to Python demonstrates how to use Transcrypt as the basis for full-blown applications. The sample gallery of applications is impressive. My personal nitpick is that they attempted to make some of numpy available within Transcrypt, breaking with their philosophy to leverage the Javascript ecosystem instead of Python. The clear separation of duties in a web application demands that they leave numpy and related libraries to a back-end API.

Nonetheless, Transcrypt is a polished mature product that anyone wishing the advantages of Python over Javascript is encouraged to use as a DSL for Js/Css/HTML.

By no means should you think every single aspect of CPython is available in Transcrypt: their docs tell you otherwise:

Note that Transcrypt avoids constructs that cannot be made to perform in the browser. This means that Transcrypt and CPython are playing in different leagues. Transcrypt makes it possible for Python programmers to take a lot of their skills to the browser, but it is in no way a replacement for CPython. The two should be regarded as complementary.

Transcrypt documentation.
## Zython
Zython is a webassembly project with a completely different implementation than python-wasm and pyodide, which are both based on emscripten and therefore suffer certain drawbacks that zython is not limited by.

The stated goal of the project is “…to create a WebAssembly build of the core Python and dependent packages, which runs both on the command line with Node.js and in the major web browsers (via npm modules that you can include via webpack). “

I find it unfortunate that the package name python-wasm ` is used in this project: it seems like it creates un-necessary confusion.

### Discussions and articles
official discussion forum
https://www.reddit.com/r/Python/comments/xy4ah5/github_sagemathinczython_webassembly_python_for/
## Bokeh
With Bokeh, you can create JavaScript-powered visualizations without writing any JavaScript yourself. It is also possible to use Bokeh output in traditional frameworks like Django or Flask.

For me, the big question is: what good is a solution that is focused only on abstracting javascript visualizations? Aren’t there other things you can use Javascript for? Why would I choose this when I’m going to need another solution for other Javascript concerns?

The answer lies in the holoviz framework, which provides programmatic access to Bokeh and more.

## pyodide
https://pyodide.org/en/stable/

Python with the scientific stack, compiled to WebAssembly.

Pyodide may be used in any context where you want to run Python inside a web browser.

Pyodide brings the Python 3.9 runtime to the browser via WebAssembly, along with the Python scientific stack including NumPy, Pandas, Matplotlib, SciPy, and scikit-learn. Over 75 packages are currently available. In addition it’s possible to install pure Python wheels from PyPi.

Pyodide provides transparent conversion of objects between Javascript and Python. When used inside a browser, Python has full access to the Web APIs.

### Building Block for
It is what PyScript is built on.

### Articles
https://testdriven.io/blog/python-webassembly/

### Contact
https://pyodide.org/en/stable/project/about.html#communication

### PyWebIO
https://pywebio.readthedocs.io/en/latest/ is a builder with documented integration for Tornado, Flask, Django and aiohttp. It can also execute standalone. It is surprisingly procedural, yet offers decent support for nested rendering using functions instead of objects and methods.

### Sample code
Tokyo Olympics country’s performance ranking

## Skulpt and Brython
are both in-browser Python implementations. But they have different objectives as well as strength and weaknesses. Brython is faster. However Skulpt requires slower execution and load times because it aims for full python compliance. The objective of the products is different: Brython is aiming to be a replacement for Javascript while Skulpt aims to be a Python distribution that has a web browser execution target.

i found a nice chart on this site as well as this site. I dont know who is plagiarizing from who, but the table does give a nice overview of the various low-level solutions;


### Related Reading
https://www.reddit.com/r/Python/comments/2yli88/whats_the_best_implementation_of_a_python/
Skulpt
https://skulpt.org/

### Building block for….
Skulpt is what Anvil, a Class A pure-python-web-dev solution is based on.

## PyWeb3D
PyWeb3D allows you to use the three.js library without writing a JavaScript. As I voiced in my review of Bokeh, one wonders what to do when needing to abstract other aspects of Javascript/HTML/CSS.

### Built on: Brython
Articles and Applications
“Meet PyWeb3D — Three.js With Python Syntax”

## Brython
https://brython.info/

## Streamlit
https://streamlit.io/ is very powerful and very popular, but adding features that you expect in a full-blown web app is hard and hackish or messy depending on who you talk to. However, apparently they have been bought out by Snowlake so they have a strong backing moving forward.

### Application Gallery

In addition to what you see here, the Streamlit forum has a [show the community](https://discuss.streamlit.io/c/streamlit-examples/9) section that boasts 14 posts per week.

[Streamlit running entirely in WebAssembly (using Pyodide)](https://edit.share.stlite.net) 

[Streamlit audio recorder](https://github.com/stefanrmmr/streamlit_audio_recorder)

An impressive [app that memorized all Archaix's knowledge from Youtube](https://archaix.streamlit.app). Archaix is a chronologist with a [youtube channel](https://www.youtube.com/c/archaix138) that boasts 100,000 followers.

[Streamlit meets Headless BI]O(https://medium.com/gooddata-developers/streamlit-meets-headless-bi-cb6196b69671) 

[Streamlit app for doing tarot readings with OpenAI](https://www.reddit.com/r/Python/comments/145t4rg/streamlit_app_for_doing_tarot_readings_with_openai/)

“Made a Streamlit app to show demographic breakdowns by age, race, gender, and education in the biggest 100 US metro areas.”

“Streamlit for Machine Learning Cheat Sheet“

“How to Build a Dividend Investing Dashboard in Python and Streamlit“

“NFT and Metadata Generator – Python & Streamlit“

“I created a Streamlit UI for OpenAI’s Whisper and added some basic scaffolding for transcript summarization“

“Easy Monitoring of dbt Cloud jobs with Streamlit “

“Plotting all public transport in NL livestream using Streamlit”

“I was unhappy with Spotify recommendations, so I used Python+Spotify’s API to make more than 1,000. See the bottom from a Streamlit app to find your playlist.”

SQL Formatter

### Discussions

[Streamlit-Powered Python Web Apps for Team Research](https://www.youtube.com/watch?v=BUCIu4KwcAw)

https://www.reddit.com/r/Python/comments/lnu1r9/i_made_a_covid19_immunityvaccination_tracker_and/

### Articles

[How to Embed a Python Streamlit App in WordPress with Replit](https://www.youtube.com/watch?v=bgj-gab_fuc)

“New Streamlit tutorial, 68 pages, 35 minimal app examples, focus on SQL+Streamlit”

“Build Real-time Data Applications Quickly Using Streamlit And Prisma“

https://analyticsindiamag.com/streamlit-vs-plotlydash-comparison-with-python-examples/

“I was excited about YOLOv7, so I built a sharable object detection application with VDP and Streamlit.“

“Streamlit User and API Authentication with Auth0 Next.js SDK‘

### Resources

[Streamlit Reddit Channel](https://www.reddit.com/r/StreamlitOfficial/)
[Streamlit Community Cloud](https://streamlit.io/cloud) - Deploy, manage, and share your apps with the world,
directly from Streamlit — all for free.
[Streamlit forum](https://discuss.streamlit.io) 