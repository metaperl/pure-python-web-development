# Class A Frameworks: fully-featured, rock-solid, industrial-grade frameworks

Class A: Industrial Strength Rock-solid Products
In this section, we list products that are solving real-world problems and are ready for production deployment… just download, install and follow the instructions to whip out a solution to your issue PRONTO, because hundreds of other have already done the same.

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

## Panel
Panel is part of an impressive tool stack. It is focused on making visualization simple and powerful.

Built on Bokeh
Application Gallery
Awesome Panel

## Atri

Atri *can* be a pure python framework and it meets all Class A requirements. But at the same time, it is not limited to Python.

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

## NiceGUI
NiceGUI has a very clean and well-documented API and the authors have built nice deliverables on top of it such as rosys.

One of the contributors gives us a great overview of the current inner workings NiceGUI:


### “No thanks Streamlit”
Streamlit is gaining major adoption in the Class B space but taking a fresh look at Streamlit revealed

it does too much magic when it comes to state handling. 

The NiceGUI author provides a deeper dive into the drawbacks of Streamlit here.

### built on FastAPI
The authors of NiceGUI chose FastAPI for some specific reasons even though my personal research would have me reach for Starlite. Now you can write fully featured web applications in NiceGUI.

### Non-linkable anchor tags:
It is laudable that the NiceGUI website is implemented in NiceGUI itself. That being said, the anchor tags generated by NiceGUI do not have a name attribute and thus you cannot link to parts of a page generated by NiceGUI directly.

### Application Gallery
Interactive images – discussion and demo link

Execute custom JS – discussion and link to demo

### Discussions
“NiceGUI: Let any browser be the frontend for your Python code“

NiceGUI versus JustPy – very informative discussion.

## IDOM
https://github.com/idom-team/idom might be the quintessential builder library – it integrates with Flask, Django, FastAPI and 4 other frameworks… and the same IDOM component can run in all of these frameworks without modifications.

IDOM connects your Python web framework of choice to a ReactJS frontend, allowing you to create interactive websites without needing JavaScript!

https://github.com/idom-team/idom
The documentation for this project is a thorough as it gets. And they have an active discussion board. And the git repo is frequently updated. Definitely a compelling Class A approach to pure python web application development.

### Built on ReactJS
Discussions
In this discussion we learned that IDOM does not transpile to JavaScript. This allows pure component functions to be fully compatible and portable to any Python web framework that supports websockets.

## Epyk
Epyk is compatible with most common Web Python Frameworks (i.e., Flask and Django). By default, the server package embeds a Flask app as it is easier to install and ready to use.

It has good documentation and a nice gallery of working programs

## Flet
Flet allows you to to build Flutter apps in Python. And that’s a big deal because

Flutter is an open source framework by Google for building beautiful, natively compiled, multi-platform applications from a single codebase.

We are talking real power here. It’s basically a corporate supported version of Htag, which is a monumental single-developer effort with similar capability. Another much older product it resembles is Muntjac, which is a port of Vaadin to Python and no longer actively supported.

### Discussions
“Combining Flet with FastAPI“
“Python is great for GUI (UI)/Front End Design . If you really want to give your boring Python Script a nice looking User Interface, then you definitely should check out this 30-min Tutorial. A Flutter for Python Library called Flet will be used here. And it is Cross Platformed !“

## Pynecone
Pynecone  compiles to a traditional React (NextJS flavor) app. Wrapping React components is quite straightforward. The authors had used Streamlit in the past, and found it great to get started with but for more complex apps found it limiting in terms of components, styling, and performance. In Pynecone, the frontend compiles down to a NextJS app, so you have full customizability on how the app looks. Streamlit can also be slow in some cases as it reruns the entire script on user events, whereas in Pynecone only the state deltas are transmitted. Also for performance and SEO nextjs is great.

### Scalability-a-go-go!
Pynecone has excellent scalability: you can horizontally scale and connect your servers to a Redis instance so they can access the user state. The authors use FastAPI for their Python server behind the scenes for handling frontend events and sending back state deltas.

Also, when running a Pynecone app in production mode, you can use NextJS SSG to prerender the entire frontend to html.

### Reference links
Official site github

### Application Gallery
https://pynecone.io/docs/gallery

### Discussion
https://www.reddit.com/r/Python/comments/zh0pmy/pynecone_web_apps_in_pure_python/
“Show HN Dec 14 2022“

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

Lona has an async approach which allows one to write whole views in one function and one context. The author feels it leads to much cleaner code.



### Discussions
https://www.reddit.com/r/Python/comments/ptcje9/lona_a_web_framework_for_responsive_web_apps_in/
https://www.reddit.com/r/Python/comments/p109o0/lona_a_web_framework_for_responsive_web_apps_in/
https://www.reddit.com/r/Python/comments/qasyxe/true_multi_user_applications_with_lona_174/
https://www.reddit.com/r/lona_web_org/

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
