# Class A Frameworks

Class A: Fully-featured, Industrial Strength Rock-solid Products
In this section, we list products that are solving real-world problems and are ready for production deployment… just download, install and follow the instructions to whip out a solution to your issue PRONTO, because hundreds of other have already done the same.

## Panel
Panel is stunning. As a pure Python framework it is powerful with a 
[huge array of components](https://panel.holoviz.org/reference/index.html). 
But when you look at [the ecosystem it is a part of](https://holoviz.org),
it truly becomes mind-blowing.
The number of display formats is [vast](https://github.com/holoviz/panel/issues/2).
It makes visualization simple and powerful. Just look at [how simple it is to throw up 
a working visual analysis with 3 variables](https://panel.holoviz.org/getting_started/build_app.html).

If this were not enough, it can run within Juypyter notebooks or web pages. The Jupyter notebook version updates
as you edit the code [as shown here](https://panel.holoviz.org/getting_started/core_concepts.html#notebook).


### Built on Bokeh

### Discussions

["Helping a user use 
plotly graphs
 and interactivity with Panel"](https://discourse.holoviz.org/t/plotly-figure-not-updating-correctly-from-panel-widgets-connected-using-panel-bind/5628)

### Application Gallery

[using MapLibre with ReactiveHTML](https://discourse.holoviz.org/t/issue-using-maplibre-with-reactivehtml/5616/4)

[A tree widget from jsTree](https://discourse.holoviz.org/t/a-tree-widget-from-jstree/1904/11)

## Django

Django can be considered a pure Python web framework. In most cases, one still uses CSS and HTML, but one does not use
Javascript. I think the main aim of pure Python web frameworks is to eliminate using another turing-complete language (Javascript).
Also, there are plenty of libraries that allow one to generate CSS and HTML via Python. 

### Django with Hypergen

[Hypergen](https://github.com/runekaagaard/django-hypergen/tree/main) is a production-ready solution, having been deployed in projects spanning tens of thousands of lines, serving over 100,000 unique users more than 10 million requests.

In hypergen you craft templates using pure Python. Instead of declaring `<p>hi</p>` in an HTML file, simply invoke `p("hi")` within your view. Composing Python functions keeps templates DRY and streamlined. If you've ever written JSX, Hypergen's syntax will feel familiar.

Hypergen has Reactive Liveviews: Effortlessly bridge frontend and backend. Connect browser events like onclick straight to backend actions. With these actions, Django views can instantly refresh the frontend with new HTML, send notifications, and more, all while natively working with Python data types.

It also has Websockets: Hypergen brings realtime to the forefront with Django Channels. Set up is a breeze - quickly establish consumers and instantly react to live events. It's realtime made simple and friendly.

Production Ready: We've deployed Hypergen in projects spanning tens of thousands 

### Django with HTMX / Unpoly

[HTMX](https://htmx.org/) and [Unpoly](https://unpoly.com/) can both be used with Django to create single-page 
web applications that are reactive and responsive but without the need to code in Javascript.





### Django and  HTML Over the Wire

The book [Building SPAs with Django and HTML Over the Wire](https://www.packtpub.com/product/building-spas-with-django-and-html-over-the-wire/9781803240190)   teaches how to build a single-page application (SPA) in Django withouts learning a JavaScript rendering framework such as React, Vue, or Angular. Instead you move the logic to Python.

#### Django LiveViews

[Django LiveViews](https://github.com/Django-LiveView/liveview) is where I learned about the book "Django and  HTML Over the Wire".
The developer and user community for this project appear to be quite small.

## Flask

Flask has [HTMX integration](https://github.com/edmondchuc/flask-htmx)  and can also be used with [Unpoly](https://unpoly.com/).

[Flask-Meld](https://github.com/mikeabrahamsen/Flask-Meld) has not seen updates in 2 years but may still be useable.

## Reflex (formerly Pynecone)
Pynecone  compiles to a traditional React (NextJS flavor) app. Wrapping React components is quite straightforward. The authors had used Streamlit in the past, and found it great to get started with but for more complex apps found it limiting in terms of components, styling, and performance. In Pynecone, the frontend compiles down to a NextJS app, so you have full customizability on how the app looks. Streamlit can also be slow in some cases as it reruns the entire script on user events, whereas in Pynecone only the state deltas are transmitted. Also for performance and SEO nextjs is great.

### Scalability-a-go-go!
Pynecone has excellent scalability: you can horizontally scale and connect your servers to a Redis instance so they can access the user state. The authors use FastAPI for their Python server behind the scenes for handling frontend events and sending back state deltas.

Also, when running a Pynecone app in production mode, you can use NextJS SSG to prerender the entire frontend to html.

### Compared to NiceGUI

https://www.reddit.com/r/Python/comments/1b7bgwn/comment/ktn7kgd/?utm_source=share&utm_medium=web2x&context=3

### Compared to Streamlit

https://www.reddit.com/r/Python/comments/1b7bgwn/comment/kti7wiq/?utm_source=share&utm_medium=web2x&context=3



### Reference links
Official site - https://reflex.dev

reddit - https://www.reddit.com/r/reflex/

github - https://github.com/reflex-dev/reflex

### Application Gallery
https://pynecone.io/docs/gallery

### Discussion

[Pynecone is now Reflex](https://www.reddit.com/r/Python/comments/1545w7e/pynecone_is_now_reflex_web_apps_in_pure_python/)

https://www.reddit.com/r/Python/comments/zh0pmy/pynecone_web_apps_in_pure_python/

“Show HN Dec 14 2022“ - https://news.ycombinator.com/item?id=33922754




## Lona

A distinguishing feature of Lona is that It abstracts web on the DOM level. This way you can build whatever you can think of, and not only use the widgets, the developers provide.

It comes with a powerful component system, to create high-level components for specialized use-cases:
* https://lona-web.org/1.x/contrib/lona-picocss/index.html
* https://lona-web.org/1.x/contrib/chartjs/index.html

Lona is a single-page-application framework, and [only replaces the parts of a page which actually changed](https://lona-web.org/1.x/tutorial/02-html/index.html#view-show).

Lona can use Django models and the Django auth system.


### Built on top of Jinja2 and aiohttp. 

According to the author Lona is based on aiohttp and uses asyncio internally. The Lona API is completely synchronous to make development easier. In contrast, with asyncio its possible to block the core event loop of the entire service without even noticing it. therefore Lona defines an API that feels like asyncio but can be integrated with blocking code seamlessly.

Traditional templating is still possible if wanted. The Lona HTML API also [comes with a HTML parser, that converts HTML strings into Lona node trees, that than can be manipulated](https://lona-web.org/1.x/tutorial/02-html/index.html#html-strings). This is very similar what the browser does with its DOM API


### Discussions

["Lona 1.14 finally adds support for Channels"](https://www.reddit.com/r/Python/comments/13qfg7s/lona_114_finally_adds_support_for_channels/) 

https://www.reddit.com/r/Python/comments/ptcje9/lona_a_web_framework_for_responsive_web_apps_in/

https://www.reddit.com/r/Python/comments/qasyxe/true_multi_user_applications_with_lona_174/

### Resources

https://www.reddit.com/r/lona_web_org/


## Solara

Solara bills itself as an Open Source library that lets you use and build data-focused web apps (data apps) using reusable UI components. Your app will work in the Jupyter notebook and production-grade web frameworks (FastAPI, Starlette, Flask, ...).

[Solara](https://solara.dev) is built on [Reacton](https://reacton.solara.dev/en/latest/), which is itself Class B. Reacton is an excellent building block and Solara is showing great promise.

* authorization is possible [via many methods](https://github.com/widgetti/solara/discussions/89) most of which you will need to develop yourself
* it  allows for [clean separation of model and view](https://github.com/widgetti/solara/discussions/88) and [the todo example](https://solara.dev/examples/utilities/todo) gives a good example of this. 

What is very laudable is that it shows how easy reuse is [compared to dash](https://solara.dev/docs/tutorial/dash) and they continue with showing how their framework [improves over streamlit](https://solara.dev/docs/tutorial/streamlit). They are also very clear about why they have [improved over Dash as well](https://solara.dev/docs/tutorial/dash).

They do not have authentication and authorization out of the box, but [they do clearly show](https://github.com/widgetti/solara/discussions/89) how it can be implemented.

## NiceGUI
[NiceGUI](https://nicegui.io) has a very clean and well-documented API. NiceGUI is not just limited to web applications. It was initially designed for use of micro-devices and robots. The [1.12 release has made it possible to have desktop apps as well.](https://www.reddit.com/r/Python/comments/127kiep/nicegui_12_paves_the_way_for_electronlike/). 

They post regularly in reddit-python and also have [their own subreddit](https://www.reddit.com/r/NiceGUI/).

NiceGUI  [breaks with the common frontend/backend distinction](https://www.reddit.com/r/Python/comments/12m03v5/comment/jg949bq/?utm_source=share&utm_medium=web2x&context=3). You simply create python objects which are synced to the browser and called upon for user interactions. Thereby there is no "form submit" system. You can simply [bind](https://nicegui.io/documentation#bindings) to a data model. Or read the values from the elements, as shown in [their auth example](https://github.com/zauberzeug/nicegui/blob/a4fe698876f21b848d77828e00da55d2c3ab0559/examples/authentication/main.py#L45).

### Handling resource intensive tasks

[NiceGUI is designed to "just work" with other, normal Python libs](https://www.reddit.com/r/Python/comments/12m03v5/comment/jg9bg1j/?utm_source=share&utm_medium=web2x&context=3). Including file access, Sqlalchemy, sqlite, USB camera, GPIO pins etc. The only thing you need to keep in mind is that we are running an event loop with asyncio. So cpu intensive tasks must be scheduled into sub-processes and io intensive tasks into threads. But asyncio has good APIs for that

### “No thanks Streamlit”
Streamlit is gaining major adoption in the Class B space but taking a fresh look at Streamlit revealed it does too much magic when it comes to state handling. 

The NiceGUI team is unabased about saying that [Streamlit is quite broken](https://www.reddit.com/r/Python/comments/127kiep/comment/jeft4lj/?utm_source=share&utm_medium=web2x&context=3) for the [reasons stated here](https://github.com/zauberzeug/nicegui/discussions/21).

### built on FastAPI
The authors of NiceGUI chose FastAPI for some specific reasons even though my personal research would have me reach for Sanic or even [Starlite/Litestar](https://www.may69.com/starlite). Now you can write fully featured web applications in NiceGUI.

[NiceGUI delivers all resources from the same route](https://www.reddit.com/r/Python/comments/12m03v5/comment/jg93jlk/?utm_source=share&utm_medium=web2x&context=3). So it's completely offline (as is required for all the mobile robots they build).

### Application Gallery
Interactive images – discussion and demo link

Execute custom JS – discussion and link to demo

### Discussions

"[Release: NiceGUI 1.2.7](https://www.reddit.com/r/Python/comments/12m03v5/release_nicegui_127_with_uidownload_easier_color/) with ui.download, easier color definitions, "aggrid from pandas dataframe" and much mor"

“NiceGUI: Let any browser be the frontend for your Python code“

NiceGUI versus JustPy – very informative discussion.

### FAQs

#### why Vue? Please use Web Components.

[Thank you for your feedback!](https://www.reddit.com/r/Python/comments/127kiep/comment/jei54bu/?utm_source=share&utm_medium=web2x&context=3) We understand the benefits of Web Components, such as interoperability and framework agnosticism. NiceGUI was developed with Vue due to its simplicity, ease of use, and rich ecosystem. However, it also allows you to use arbitrary HTML/JS, so you're not strictly limited to Vue components. It would be great to se contributions that simplify/encourage the usage of Web Components.

#### Is it possible to integrate this with libraries like plotly or bokeh?

[We already have pyplot and plotly.And Altair is in the making.](https://www.reddit.com/r/Python/comments/127kiep/comment/jei3uop/?utm_source=share&utm_medium=web2x&context=3) While there was some interest in adding Bokeh, we are still looking for someone creating a pull-request.

#### Can nicegui run on browser without a connection to internet? Like just use it to manipulate a local dataset.

Yes. We use it on non-connected robots all the time. By default NiceGUI self-serves all dependencies.

#### Can you just adjust spaces between elements like Checkboxes easier than streamlit?

[you can use low-level css or tailwind](https://nicegui.io/documentation#styling), so all flexibility with very little code

#### Flet vs NiceGUI

> Flutter is cool. And doing it from Python is also great :-)
I think the biggest difference is the rendering approach. Flutter (and hence Flet) basically paint everything inside a fullscreen canvas. That means you will get pixel-perfect layouts on every browser. NiceGUI on the other hand creates html elements. These can be searched, indexed, augmented with browser plugins. It's just normal web stuff driven from the Python world. It also enables NiceGUI to embed all the existing web libraries out there :-)
> https://www.reddit.com/r/Python/comments/127kiep/comment/jehvby7/?utm_source=share&utm_medium=web2x&context=3

#### Pynecone vs NiceGUI

r-trappe [states](https://www.reddit.com/r/Python/comments/127kiep/comment/jefuv5s/?utm_source=share&utm_medium=web2x&context=3)

> Pynecone has a very interesting approach: They use Python as a language to build a fully functional frontend. That means they precompile html, js and css like all the other web frameworks out there. That makes it somewhat independent of the backend and provides some interesting optimization opportunities. But:

> NiceGUI was initially build for accessing and controlling hardware as shown in our webcam demo); I'm not sure how it would be done with Pynecone

> NiceGUI encourages the use of standard Python (callbacks, if-statements,..), Pynecone on the other hand uses explicit State classes and provides constructs like pc.cond and pc.foreach.

> NiceGUI uses Vue/Quasar for the frontend while Pynecone is build on NextJS- NiceGUI generates HTML/JS/CSS via templates on the fly while Pynceone has an explicit compile step; so NiceGUI can be run with normal "Python" instead of using a command like "pc"

while both frameworks use FastAPI for the backend, in NiceGUI you can actually use your own App and simply extend it with NiceGUI to provide additional UI; Pynecone hides FastAPI which makes it harder to provide other API endpoints (for example to serve images from memory instead of files).

> NiceGUI can now run in a native window :-)




## ReactPy

[ReactPy](https://github.com/reactive-python/reactpy) is a library for building user interfaces in Python without having to write Javascript. ReactPy interfaces are made from components which look and behave similar to those found in ReactJS.

In order to maintain full compatibility with all Python packages, [ReactPy is server side rendered](https://www.reddit.com/r/Python/comments/1274w68/comment/jee45m8/?utm_source=share&utm_medium=web2x&context=3). So all Python packages will work exactly as you expect. The only data that gets transmitted to the client is the current HTML document (with a little bit of extra magic).

We don't transpile between languages, so Python code gets to stay pure. Our ReactPy hooks and rendering logic are functionally equivalent to ReactJS, except we use Python asyncio to keep things moving.

### Tons of backends to use!

ReactPy has official support for the following backends: Flask, FastAPI, Sanic, Tornado, Django, Jupyter, Plotly-Dash.



### Articles

[ReactPy: Will it Dethrone JavaScript as the Top Choice?](https://poletto.dev/reactpy-will-it-dethrone-javascript-as-the-top-choice) 

Getting started with Reactpy - https://www.kdnuggets.com/2023/06/getting-started-reactpy.html

### Discussions

https://www.reddit.com/r/Python/comments/1274w68/reactpy_build_reactjs_interfaces_in_pure_python/

### FAQs

#### How would this work if I was to make a database call in a component? What happens under the hood?

https://www.reddit.com/r/Python/comments/1274w68/comment/jee100p/?utm_source=share&utm_medium=web2x&context=3



## Anvil
http://anvil.works is an abstraction over all web development provided in a cloud web-based environment. It is a freemium product.

Someone really likes Anvil:

For me, the final choice is about productivity. Anvil isn’t an isolated tool to ‘generate HTML and JS’. It’s an integrated suite of *all the tools needed to build and deploy complete, full stack software projects, with pure Python: database and visual UI builder, server and client functionality, with essential features (user management, email, web APIs, PDF printing, Git integration and version management, Google services integration, etc.), all built in. It’s the simplicity enabled by Anvil’s overall design, the scope of its APIs, the deployment capabilities, and all the features it brings together (far beyond HTML, CSS, and JS generation), together with the breadth of capability enabled by the full Python ecosystem available natively, which makes it ridiculously productive, like no other system I’ve ever seen (writing code for 40+ years).

### Built on skulpt
Anvil uses skulpt under the hood.

### Publications
“Turning a Jupyter Notebook into a Web App“

### Application Gallery
“Prototyping a YC Startup Each Day – Meter Feeder (YC Winter 16)“

YC Prototypes #2: Building Magic in 2.4 hours



## Atri

[Atri](https://atrilabs.com) *can* be a pure python framework and it meets all Class A requirements. But at the same time, it is not limited to Python.

On the surface Atri reminds me of Anvil (which is built on Skulpt) because of the visual GUI builder. But one difference is the customization of the UI is done via React in Atri but done via Python in Anvil.

Atri is also more flexible about backend development. Currently, they support Python for backend development but they are planning to add support for NodeJS soon.

Using Atri framework, developers **do not need to write and document REST APIs. Instead, they rely upon the object model which acts as a single source of truth.** This also has other benefits as well such as reducing compliance breaches.

### Application Gallery

https://atrilabs.com/showcase

### Built on - FastAPI, React

Being built on FastAPI is a question mark for me because [Starlite seems better designed](https://may69.com/starlite/).



## Dash
Dash has several eye-catching bulletpoints about it:

Instead of passive dashboards, one can build truly interactive analytical apps: apps can have forms and buttons to take input and update the graphical dashboard in realtime.
Ready for desktop and mobile and can produce print-ready PDFs on demand: has 2 (competing?) standards for responsive UI development: dash mantine and dash bootstrap.
there is Dash and Dash Enterprise. The enterprise version has other advanced features such as allowing an end-user to run GPU accelerated workflows to process hundreds of millions of records asynchronously.
### Built on plotly and ReactJS
### Resources
Ann Marie Ward has over 30 repositories with beginner and advanced Dash material. She is Co-author of “The Book of Dash“. A few highlights:

Multi-page app examples – modern Dash has evolved beyond having singe page apps.
django-plotly-dash – Expose plotly dash apps as Django tags. Multiple Dash apps can then be embedded into a single web page, persist and share internal state, and also have access to the current user and session variables.

### Discussion and Publications
“Pip Install Plotly-Dash | Top 10 Useful Resources for Learning / Building Dashboards within the Framework” – highly recommended video and YouTube channel.

“Dash Dashboards, Multi-Paged Quick Development with Python & React Tutorial“

https://link.medium.com/GtsQEdqt7eb

“A quick introduction to Dash“

“Dash is React for Python, R, and Julia“

### Applications
“Plotly/Dash is the Best Framework for Frontend Development IMO“


### From Class C to Class A
The goal is this guide is to rate frameworks that make simple web jobs simple AND allows you to scale out to develop the next top-100 web property if necessary. The class-grading-system was setup so that only highly reliable, robust AND feature-complete products were class A. At one point, Dash was nearly class C because my research revealed that one former user said:

If it’s a simple project, sure.

Otherwise it’s terrible. We switched from dash to fastapi + React. No regrets ever since.

TheGuyWithoutName
but a recent post to reddit showed that Dash can do it all – simple things, Jupyter things and yes, top 100 web property things as well.





## Epyk
[Epyk](https://github.com/epykure/epyk-ui) is compatible with most common Web Python Frameworks (i.e., Flask and Django). By default, the server package embeds a Flask app as it is easier to install and ready to use.

It has good documentation and a nice gallery of working programs

## Flet
Flet allows you to to build Flutter apps in Python. And that’s a big deal because

Flutter is an open source framework by Google for building beautiful, natively compiled, multi-platform applications from a single codebase.

We are talking real power here. It’s basically a corporate supported version of Htag, which is a monumental single-developer effort with similar capability. Another much older product it resembles is Muntjac, which is a port of Vaadin to Python and no longer actively supported.

### Discussions
“Combining Flet with FastAPI“
“Python is great for GUI (UI)/Front End Design . If you really want to give your boring Python Script a nice looking User Interface, then you definitely should check out this 30-min Tutorial. A Flutter for Python Library called Flet will be used here. And it is Cross Platformed !“





## Nagare
Nagare has earned a class A ranking. It has been around for over a decade and was one of the first frameworks to offer a pure python approach to web application development. It is very complete and their consulting firm has delivered several impressive large-scale apps. They were very supportive of me when I deployed an application to a Fortune 500 company using it. It is very much a work of art and creativity.

That being said, it has simple JS to Python transpilation only, primarily limited to the “onclick” event of a link/button..

It was inspired by the Seaside framework for smalltalk.

It is based on component-based OO instead of inheritance.

It is not designed to leverage all the power in Javascript to create reactive, highly interactive apps.

That being said, if your desire is object-oriented HTML production interfaced to an object-relational store on the back (SQLAlchemy), it is very Zen for this purpose.

It is categorized as class A because it can solve problems. It borders on Class B because it cannot offer all javascript functionality. Also, the author of nagare did not make good on his promise to integrate muntjac into Nagare. Muntjac was a Python program that brought the entire Vaadin widget set into Python, making for good-looking professional web apps.

## Reahl
Reahl is another tool barely hanging onto Class A rating. The main positive attribute of this framework is that it has tons of widgets out of the box for everything to do full-fledged web applications. I used it on a consulting project and did not have to look outside of it for anything.

The authors are very intelligent and responsive. I would encourage you to study it’s approach to web application development carefully before choosing it. Also read the discussion group and closed issues. To be frank, I do not see eye-to-eye with the developers on certain choices. But all in all, I have nothing but praise for how much rapid support they gave me on a corporate project I did with Reahl that was completed successfully. While both Nagare and Reahl are object-oriented super-mature systems, they embrace OO Python in drastically different ways.

## PuePy

[PuePy](https://puepy.dev/ is a reactive frontend framework written entirely in Python and heavily inspired by Vue.js. Both in Web Assembly (via [PyScript](https://pyscript.net/)), PuePy lets developers choose between a full-featured CPython/Pyodide runtime or a MicroPython runtime. With pages, components, and an optional-client side router, localstorage and sessionstorage proxies, and the ability to use Web Components directly, PuePy is ideal for line-of-business or single page apps. To see an example app demonstrating PuePy's capabilities, see [ExpenseLemur.com](https://expenselemur.com) and its [source code](https://github.com/kkinder/expenselemur).
