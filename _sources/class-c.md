# Class C: Solutions that may one day be Class B or Class A

## Starfyre

https://github.com/sansyrox/starfyre is a new framework that the author admits
is unstable. I do not see this making Class A anytime soon and it looks rather
involved to make even simple apps based on [the code for the calculator](https://github.com/sansyrox/first-starfyre-app)

### Discussions

"Starfyre - [A Python Web Framework for creating frontend web applications](https://www.reddit.com/r/Python/comments/13bloxf/starfyre_a_python_web_framework_for_creating/)"

## Enaml-Web
Enaml web is part of a very broad ecosystem:

There is plain old Enaml which can succinctly build desktop applications using their python-powered DSL
There is Enaml-web which is a variant of Enaml for the web
There is atom-db, which is their asynchronous ORM
And there is Atom, which is a very capable object system for Python. Their object system has observers and data validation. It is almost as good as Traitlets, which is slightly more powerful because you can generate command-line interfaces from Traitlets classes easily.
Enaml-web has a couple of demo projects. Why is it class C?

you can do the simple things that it can do with simpler tools and less code
no roadmap or facilities to do complex world-class web apps
the user base is apparently small
the developer base is apparently small
to it’s merit, the code is frequently updated
very few real world examples. just two sample projects
## PyScript
PyScript is developed by Anaconda. Superficially, and only superficially, PyScript seems to be just like Brython – you embed Python in some tags in HTML and walla, dynamic web pages with Python not Javascript.

But PyScript sets itself apart from Brython because it is based on Pyodide. In the words of the co-author:

> Pyodide is the same *CPython* interpreter you run on your laptop, but compiled to target WebAssembly. (Just as CPython is compiled to target x86 or M1 assembly on your laptop.)
> This is why the various native C/C++ extensions for Python can also be supported: they are compiled to target WebAssembly as well.
> This has nothing to do with Javascript. It’s certainly not the case that “Pyodide is Python written in JS” — that is more like Brython. (Such an approach could never import numpy, pandas, scipy, etc. without also rewriting all of those in Javascript as well.)
> 
> -- Peter Wang, CEO of Anaconda
Since Anaconda has already developed Panel, one would wonder why PyScript. Wang states:

> This is a broader and more fundamental capability than Panel. You can run just about any Python in the browser. And you can wrap Javascript libraries. So we have examples showing interaction with Three.JS, with d3, etc.

According to Wang, the intent of PyScript is:

> … to empower programming for millions of people who find existing stuff too complex. Learning even a single language is hard enough. These folks will not be able to learn all the complexity of JS, modern web dev and devops, etc etc.
> 
> With PyScript, they just write in a single language, with a little bit of HTML, and they have something that they can share with any friends and colleagues, with zero deployment complexity. They can email them the file, or copy it on a thumb drive.
> 
> -- Peter Wang, CEO of Anaconda

Currently the interest in PyScript far outstrips its ability to offer a productive solution to prospective users. However, the strong corporate backing and large team of developers for the product indicate that it may well be a Class A system in the next year or so. It has tremendous potential. As the author of htag has stated:

This thing is the most incredible thing I’ve seen for some years … In the JavaScript and python world

It opens/unlocks a lot of things …

Coming from brython, it unlocks full python … In the right way (thanks wasm)

Sure, there are a lot of improvements/gaps, before it could be supported natively in VM browsers … But it’s the way to go …

But the promise is here … You can code python (and pip any libs you want), with just a js include … For now ! Can’t imagine all the things which will come soon … Pretty excited !

manatlan
### Q&A
Can you pass objects between JS and Python?
Passing objects is supported. In the OpenAI API example, you will see js -> py with:

from js import localStorage, document, console, XMLHttpRequest

“from js import…” imports js objects directly into PyScript’s Python.
Going in the other direction (py -> js), you can use PyScript.runtime.globals.get('my_variable_name')

XMLHttpRequest is what I used to make the HTTP requests as requests is not supported. An alternative would be to use pyodide.http.pyfetch

### References:

https://docs.pyscript.net/latest/guides/passing-objects.html

https://docs.pyscript.net/latest/guides/http-requests.html

### Related Publications
“I made an interactive Pandas cheat sheet using PyScript“
“Using the Azure SDK for Python in Pyodide and PyScript”
https://www.reddit.com/r/Python/comments/ug1pf6/python_in_html_new_project_by_anaconda_with_all/
https://www.reddit.com/r/Python/comments/uhbby4/whats_the_difference_between_pyscript_template/
https://www.reddit.com/r/Python/comments/ugl19x/anaconda_new_from_anaconda_python_in_the_browser/
https://www.reddit.com/r/Python/comments/uhm1oe/meet_pyscript_new_framework_from_anaconda_that/
https://www.reddit.com/r/Python/comments/ujicyq/i_tested_pyscript_and_you_can_literally_write/
https://bas.codes/posts/pyscript-todo
### Built on pyodide


## UiDOm
UIdom official repo

Built on dominate
## Gooey
And I plagiarize:

Gooey converts your Console Applications into end-user-friendly GUI applications. It lets you focus on building robust, configurable programs in a familiar way, all without having to worry about how it will be presented to and interacted with by your average user.

Why?
Because as much as we love the command prompt, the rest of the world looks at it like an ugly relic from the early ’80s. On top of that, more often than not programs need to do more than just one thing, and that means giving options, which previously meant either building a GUI, or trying to explain how to supply arguments to a Console Application. Gooey was made to (hopefully) solve those problems. It makes programs easy to use, and pretty to look at!

Who is this for?
If you’re building utilities for yourself, other programmers, or something which produces a result that you want to capture and pipe over to another console application (e.g. *nix philosophy utils), Gooey probably isn’t the tool for you. However, if you’re building ‘run and done,’ around-the-office-style scripts, things that shovel bits from point A to point B, or simply something that’s targeted at a non-programmer, Gooey is the perfect tool for the job. It lets you build as complex of an application as your heart desires all while getting the GUI side for free.

## Wooey
per the Wooey docs:

Wooey is a simple web interface to run command line Python scripts. Think of it as an easy way to get your scripts up on the web for routine data analysis, file processing, or anything else.

## Remi
It breaks my heart to put Remi in the Class C section. The author works very hard on his product and is very responsive.

It offers a class-based approach to user interface generation. It operates using an internal webserver and has limited support for traditional authentication and authorization.

It primarily is good at building user interfaces for personal use. It is far older than Gradio.

## Abstracloud
Abstracloud reminds me of Gradio but with commercial restrictions. The pricing model and non-FOSS distribution method seem to be a bit limiting. For instance, comparing their pricing model with Anvil’s, we see that we can have 50,000 data table rows in the free account at Anvil whereas any storage requires a jump up to the paid plan.

### Publications
https://www.reddit.com/r/Python/comments/wg13qr/lib_that_generates_web_uis_for_your_scripts_they/
###Deliverables
https://www.reddit.com/r/Python/comments/wg4ml7/i_made_a_simple_weight_tracker_that_displays/
## Rapydscript
https://github.com/atsepkov/RapydScript is a Class C system primarily because it is not Python and it is not Javascript. They do have an impressive set of gallery examples but the mailing list and source code have no activity since May 2021. When one attempts to make a new language, one must first have users as well as libraries and if there is any attrition in either, then the language becomes less desirable over time. We’ve seen it happen with Coffeescript as well as Cappucino and Objective-J. To be sure, Python has warts and Javascript has even more warts but I once saw an IRC chat where someone was arguing about rewriting Emacs in Common Lisp and the other person said: “your opinion is no substitute for millions of lines of working code”. In other words, a perfect language is nothing without libraries an userbase.

## Rapydscript-ng – a fork of RapydScript
https://github.com/kovidgoyal/rapydscript-ng is a fork of the Rapydscript ng. there have been no commit to the repo since Dec 2021. To fork a language to create even another variant means that rapydscript-ng shares the same hazards of adoption as Rapydscript itelf

## Ryact and Breact
Ryact and Breact are emulations of react. Ryact is built on rapydscript and is 10x faster than Breact, which is built on Brython. As a single author, he has not been able to keep up with all the demands of industrial-grade software engineering in his projects.

### Built on rapydscript and Brython
WASMer for Python: Pyodide’s little brother?
https://github.com/wasmerio/wasmer-python – is a WebAssembly runtime for Python. It seems to have less popularity as a builder than Pyodide. Also the development team and userbase appear to be smaller.

## Domonic
Domonic is a builder also. It contains quite a few sub-packages, some of which might be better elsewhere:

* html : Generate html with python 3 😎
* dom : DOM API in python 3 😲
* javascript : js API in python 3 😳
* terminal || cmd : call terminal commands with python3 😱 (see at the end)
* JSON : utils for loading / decorating / transformin
* SVG : Generate svg using python
* aframe || x3d tags : auto generate 3d worlds with aframe.

* The author also has a stripped down package called htmlx that will be discussed in the HTML only section.

### Why is Domonic rated so low?
Well, the doc and the source code repo are very current, so that cannot be why. Basically it is an unfinished project with very few deliverables. For example in the docs about the d3 interface, he states ‘WARNING: this package is still in dev. expect bugs ‘. The approach to pure Python web development seems a bit less elegant than other projects. For instance, the need to manually wrap d3 and then do an incomplete job of it shows how much more limited this project is than Transcrypt which can use any Javascript library without any particular wrapping.

The author also developed htmlx, which is a stripped down version of domonic, limited primarily to rendering HTML.

## Wave
https://h2oai.github.io/wave/ is good at building realtime streaming dashboards. It has support for OpenID and Basic Auth but has no examples or express concern for integration with Flask or Django, even though they feel it probably should work.

I installed Wave and played around with the tour. I had problems getting some of the examples to work on Windows. Even so, I find Wave to be very succinct and very powerful.

It is modular and dynamic. By modular, I mean, that building a website is as simple as populating Python data structures with objects. By dynamic, I mean I was impressed by the ability to edit a live website directly from the Python REPL. Just think: a live site could have updates from cron jobs.

I was a bit put-off by having to learn two different ways to use Wave: one for scripts and one for apps. To make things simple for myself, I would just always write apps. Also, the tutorial would do well to have 2 directories – one for scripts and one for apps instead of putting all Python examples in an apps directory.

I also did not like the way to model was initialized in the rendering method. I started a discussion about that.

