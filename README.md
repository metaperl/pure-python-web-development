# Pure Python Web Development: **NO** CSS, JSS, or HTML Needed or Wanted!


> It is no exaggeration to regard this as the most fundamental idea in programming:

    The evaluator, which determines the meaning of expressions in a 
    programming language, is just another program.

> To appreciate this point is to change our images of ourselves as programmers. 
> We come to see ourselves as designers of languages, 
> rather than only users of languages designed by others.
> 
> -- [Structure and Interpretation of Computer Programs](https://mitpress.mit.edu/sites/default/files/sicp/full-text/book/book-Z-H-25.html#%_chap_4), Chapter 4.


By developing web apps entirely in Python, Python serves as a
metalanguage generating the target languages of CSS/HTML/JS. 

If you think about it, we already use tools like lxml to generate
XML. So similarly, we are seeking other tools for HTML/JS/CSS.

This greatly simplifies and abstracts web application development. Prior to
the web, graphical applications were largely developed in just a
single language. Text applications are still this way. Web
application has gone through some phases, that [I have discussed
elsewhere](https://metacpan.org/pod/HTML::Seamstress#A-BRIEF-HISTORY-of-Dynamic-HTML-Generation-(Templating)):  

1. server side includes
2. CGI scripts
3. Java applets
4. client-server partial page reloaded apps developed with a back-end and front-end

Even though stage 4 is where we are, stage 3 was a more unified approach to
GUI development, very similar to the way X-windows and C/TCL/Smalltalk
were used to develop GUI apps prior to the web. 

The problem we have exists because the web was never really meant for applications:
it was designed to make information browseable for anyone. Applications were
something you downloaded and installed on your personal machine. But before we knew
it, people were adding more and more functionality to websites by sticking in a 
little JQuery here or some PHP there. And before we knew it, the line between
web site and web application became blurry.

While data storage technologies have changed fairly slowly, the best way to develop
in Javascript and even CSS changes quite a 
bit [as you can see](https://github.com/kamranahmedse/developer-roadmap). 

The need for robust software development was left behind in a frenzy of creating
a soup of technologies. But some people saw the pitfall and started working on
alternative solutions. In java we saw zk and Vaadin. In Scala we saw 
[mind-blowing](https://www.youtube.com/watch?v=Ksoi6AG9nbA)
live coding in [ScalaJS](http://www.scala-js.org/).
And in Smalltalk we saw [Seaside](http://seaside.st/). 

But most impressively we saw [UrWeb](http://impredicative.com/ur/) - a 
metalanguage inspired by ML that generated typesafe back-end and front-end code,
thereby preventing all of the things that adhoc modern web development suffers from:

* code-injection attacks
* invalid HTML
* Dead intra-application links
* mismatches between HTML forms and the fields expected by their handlers
*  client-side code that makes incorrect assumptions about the "AJAX"-style services that the remote web server provides
* invalid SQL queries
* improper marshaling or unmarshaling in communication with SQL databases or between browsers and web servers

## And thus we see why Pure Python Web Development is a necssity:

* security
* ease of development
* learn one language instead of 3 or more rapidly changing languages

## Overview of Python Approaches to NOJS Web Development

We call it "NOJS" web development because as [Qooxdoo](https://qooxdoo.org/) 
has shown, with Javascript,
you can generate and manipulate CSS and HTML. So JS is the roots and everything
else grows from there.

There are 3 main types of offerings in the Python space for allowing
yourself to develop in Python but deliver modern dynamic full-featured 
web applications:

1. Transpilers - these products are primarily concerned with literal
   translation of Python to JSS/CSS/HTML/Web assembly.
1. Application suites - these products are designed to abstract away most or all
   of the concerns of deploying an industrial strength app.
1. Builders are somewhere in between transpilers and application
   suites. In most cases a builder (or transpiler) is used with a
   conventional terminal-server webapp framework like Flask or
   Django. But there can be [considerable
   pain](https://www.reddit.com/r/Python/comments/p109o0/lona_a_web_framework_for_responsive_web_apps_in/h8aty2l?utm_source=share&utm_medium=web2x&context=3)
   in integrating builder output into a full-suite web application as users of Dash
   have unfortunately found out.
   
# Transpilers

## Transcrypt
http://transcrypt.org/ is a Javascript generator that opts for integration 
with Javascript libraries instead of Python libraries. The book 
[React to Python](https://pyreact.com/) demonstrates how to use Transcrypt as the
basis for full-blown applications.

## Rapydscript
https://github.com/atsepkov/RapydScript

### Rapydscript-ng - a fork of RapydScript
https://github.com/kovidgoyal/rapydscript-ng

## pyodide 
https://pyodide.org/en/stable/

Python with the scientific stack, compiled to WebAssembly.

Pyodide may be used in any context where you want to run Python inside a web browser.

Pyodide brings the Python 3.9 runtime to the browser via WebAssembly, along with the Python scientific stack including NumPy, Pandas, Matplotlib, SciPy, and scikit-learn. Over 75 packages are currently available. In addition it’s possible to install pure Python wheels from PyPi.

Pyodide provides transparent conversion of objects between Javascript and Python. When used inside a browser, Python has full access to the Web APIs.

### Contact

https://pyodide.org/en/stable/project/about.html#communication

## Skulpt
https://skulpt.org/

## Brython
https://brython.info/

##  WASMer for Python
https://github.com/wasmerio/wasmer-python - A complete and mature 
WebAssembly runtime for Python.


# Application Suites

## Anvil

http://anvil.works is an abstraction over all web development
provided in a cloud web-based environment. It is a freemium product.

## Dashborg 
https://www.dashborg.net/ is unique. You could 
call it a more
sane approach to 
[the nightmare that Angular is](https://gist.github.com/tdd/5ba48ba5a2a179f2d0fa). 
It allows one to
create full applications but using a "live" version of HTML that
dynamically self-populates using *either* Go or Python back-ends. 

It is interesting, but it works backwards from the way I think: I would rather
have a computer program generate HTML/JS/CSS rather than have my turing-complete
language limited by HTML. 

So I would say it would not interest me much in the same way that Angular does 
not - the less powerful language is orchestrating the use of a more powerful
language.

Other past tools in this vein are OpenLaszlo.


## JustPy
https://justpy.io/

Justpy has a callback based approach to input events.

## Nagare

[Nagare](https://github.com/nagareproject/core#readme) was the first framework
to eliminate HTML and programmatically create simple JS interactions. 

It was inspired by the [Seaside framework for smalltalk](http://seaside.st/).

It is based on component-based OO instead of inheritance.

It is not designed to leverage all the power in Javascript to create
reactive, highly interactive apps. 

That being said, if your desire is object-oriented HTML production interfaced to
an object-relational store on the back (SQLAlchemy), it is very Zen for this purpose.


## Reahl 
https://www.reahl.org/ is an object-oriented widget 
approach to eliminating the need
to focus on JS/HTML.
 


# Builders


## Dash  
https://dash.plotly.com/ is built on top of flask and 
[with some effort](https://community.plotly.com/t/flask-login-suport-for-dash/5934)
you can build complete web applications based on Flask.

The default [authentication](https://dash.plotly.com/authentication) is based on
either
bare bones Basic Auth or Dash Enterprise.

Dash has a large following and is a product of [Plotly](https://plotly.com/), a
commercial company that offers an enterprise version of Dash.

### Discussion and Publications
https://link.medium.com/GtsQEdqt7eb

[Gallery of apps](https://dash-gallery.plotly.host/Portal/) 

## Lona

https://github.com/fscherf/lona supports [usage of Django
models](https://lona-web.org/cookbook/integrating-django.html)  and
[the Django auth
system](https://lona-web.org/contrib/django-auth.html). 

To account for big HTML trees written in python, [Lona supports
widgets](https://www.reddit.com/r/Python/comments/p109o0/lona_a_web_framework_for_responsive_web_apps_in/h8asc0i?utm_source=share&utm_medium=web2x&context=3)
to encapsulate smaller trees an their functionalities. That makes
components reusable. 

Lona has an async approach which allows one to write whole views in one
function and one context. The author [feels it leads to much cleaner
code](https://www.reddit.com/r/Python/comments/p109o0/lona_a_web_framework_for_responsive_web_apps_in/h8ejjyj?utm_source=share&utm_medium=web2x&context=3).

[According to the
author](https://www.reddit.com/r/Python/comments/p109o0/lona_a_web_framework_for_responsive_web_apps_in/h8dlv5j?utm_source=share&utm_medium=web2x&context=3)
Lona is based on aiohttp and uses asyncio internally. The Lona API is
completely synchronous to make development easier. In contrast, with asyncio its
possible to block the core event loop of the entire service without
even noticing it. therefore Lona defines an API that feels like
asyncio but can be integrated with blocking code seamlessly. 

### Discussion

https://www.reddit.com/r/Python/comments/p109o0/lona_a_web_framework_for_responsive_web_apps_in/

## Enaml-Web

https://github.com/codelv/enaml-web


## Ryact
https://github.com/dewball345/ryact

## Epyk
[Epyk](https://epyk-ui.readthedocs.io/en/latest/) is compatible with  
most common Web Python Frameworks (i.e., Flask and Django). By default, the server 
package embeds a Flask app as it is easier to install and ready to use.

It has good documentation and a nice gallery of working programs.


## IDOM 
https://github.com/idom-team/idom is a work in progress.



## PyWebIO
https://pywebio.readthedocs.io/en/latest/ is a builder with documented
integration for Tornado, Flask, Django and aiohttp. It can also
execute standalone. It is surprisingly procedural, yet offers decent
support for nested rendering using functions instead of objects and methods.


## Wave 
https://h2oai.github.io/wave/ is good at building realtime streaming dashboards.
It has [support for OpenID and Basic Auth](https://wave.h2o.ai/docs/security)
but has no examples or express concern for integration with Flask or Django, even
though 
[they feel it probably should work](https://github.com/h2oai/wave/discussions/934).



# Not a Builder but Self-contained and limited


## Streamlit 
https://streamlit.io/ is very powerful, but adding features that you expect in a 
full-blown web app is [hard and hackish](https://discuss.streamlit.io/t/user-authentication/612/18)

### Discussions

https://www.reddit.com/r/Python/comments/lnu1r9/i_made_a_covid19_immunityvaccination_tracker_and/

## Remi
https://github.com/dddomodossola/remi offers a class-based approach to user
interface generation. It operates using an internal webserver and has 
[limited support](https://github.com/dddomodossola/remi#authentication)
for traditional authentication and authorization.

It primarily is good at building user interfaces for personal use.

# Defunct, No recent releases

## AnPyLar
https://www.anpylar.com/ has seen no updates since 2018.

## Muntjac
[Muntjac](https://github.com/rwl/muntjac) is an implementation of
[Vaadin](https://vaadin.com/) for Python. Vaadin is an enterprise level Java
web app framework with a large array of
modern clean javascript widgets. 

While Vaadin abstracted away Javascript through Java, Muntjac did the same
for Python in an impressive way.


## PyJS (formerly PyJamas)
http://pyjs.org/ used to be called PyJamas but that name has been
reserved for something altogether different now. 

## Timothy Crosley Products

### Webbot
https://github.com/timothycrosley/WebBot is 

```
a collection of 
several tools that enables building Python web applications 
the same way native ones are built. 

As a result, the WebBot framework encourages reuse, 
concise code, rapid development, and happy developers.
```
### Jiphy

https://github.com/timothycrosley/jiphy is a nearly-defunct transpiler.

### TheDOM

https://github.com/timothycrosley/thedom is for generating HTML and JS

# HTML/CSS only

https://github.com/BrainStormYourWayIn/sierra

https://github.com/Knio/dominate

http://naga.re (JS processing limited to clicks) 

https://pypi.org/project/simple-html/


# Articles 

https://analyticsindiamag.com/streamlit-vs-plotlydash-comparison-with-python-examples/

# Frequently Asked Questions (FAQ)

## Any impressive apps built with these technologies?

### Streamlit
[Gallery](https://streamlit.io/gallery)

["Easy Monitoring of dbt Cloud jobs with Streamlit
"](https://blog.streamlit.io/dbt-cloud-jobs-with-streamlit)

