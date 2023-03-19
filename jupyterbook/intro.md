# Pure Python Web Development

![](pure-python-header.png)

This guide is designed to help you find a pure Python web application development solution *fast*. If you want theory, see the “Theoretical Introduction” section below. Otherwise just jump right to the practical guide and choose what works for you.

## Theoretical Introduction
Welcome to 100% pure python web development. Sayonara to the HTML/JS/CSS soup. The driving concept behind 100% pure Python web development was captured long before the WWW existed in Chapter 4 of the classic software engineering text “Structure and Interpretation of Computer Programs”:

> It is no exaggeration to regard this as the most fundamental idea in programming:
The evaluator, which determines the meaning of expressions in a programming language, is just another program.
To appreciate this point is to change our images of ourselves as programmers. We come to see ourselves as designers of languages, rather than only users of languages designed by others.
> 
> -- “Structure and Interpretation of Computer Programs”, Abelson and Sussman

By developing web apps entirely in Python, Python serves as a metalanguage generating the target languages of CSS/HTML/JS!

## If you think about it, we already use tools like lxml to generate XML. 

## We already use dictionaries to abstract away JSON. 

The benefits of Python for XML and JSON are undisputed and widely accepted. So similarly, we are seeking to use Python as a metalanguage for HTML/JS/CSS. 

This greatly simplifies and abstracts web application development. Prior to the web, graphical applications were largely developed in just a single language. Text applications are still this way. Web application has gone through some phases, that I have discussed elsewhere:

1. server side includes
1. CGI scripts
1. Java applets
1. client-server partial page reloaded apps developed with a back-end and front-end
Even though stage 4 is where we are, stage 3 was a more unified approach to GUI development, very similar to the way X-windows and C/TCL/Smalltalk were used to develop GUI apps prior to the web.

The problem we have exists because…

## The web was never really meant for applications: 
The WWW was designed to make information browsable for anyone. Applications were something you downloaded and installed on your personal machine. But before we knew it, people were adding more and more functionality to websites by sticking in a little JQuery here or some PHP there. And before we knew it, the line between website and web application became blurry.

While data storage technologies have changed fairly slowly, the best way to develop in Javascript and even CSS changes quite a bit as you can see.

The need for robust software development was left behind in a frenzy of creating a soup of technologies. But some people saw the pitfall and started working on alternative solutions that allowed a software developer to develop in one language yet generate the plethora of languages needed for a web application. In Java, we saw zk and Vaadin. In Scala, we saw mind-blowing live coding in ScalaJS and in Smalltalk we saw Seaside.

But most impressively we saw UrWeb – a metalanguage inspired by ML that generated typesafe back-end and front-end code, thereby preventing all the things that adhoc-tossed-salad modern web development suffers from:

* code-injection attacks
* invalid HTML
* Dead intra-application links
* mismatches between HTML forms, and the fields expected by their handlers
* client-side code that makes incorrect assumptions about the AJAX-style services that the remote web server provides
* invalid SQL queries
* improper marshaling or unmarshalling in communication with SQL databases or between browsers and web servers

## We thus see why Pure Python Web Development is a necessity:
* security
* ease of development
* learn one language instead of 3 or more rapidly changing languages

## Overview of Python Approaches to NOJS Web Development
We call it “NOJS” web development because as Qooxdoo has shown, with Javascript, you can generate and manipulate CSS and HTML. So JS is the roots and everything else grows from there.

## How shall I avoid Javascript? Let me count the ways…
There are 3 main types of offerings in the Python space for allowing yourself to develop in Python but deliver modern dynamic full-featured web applications:

* Transpilers – these products are primarily concerned with literal translation of Python to JSS/CSS/HTML/Web assembly.
* Application suites – these products are designed to abstract away most or all of the concerns of deploying an industrial strength app.
* Builders are somewhere in between transpilers and application suites. In most cases a builder (or transpiler) is used with a conventional terminal-server webapp framework like Flask or Django. But there can be considerable pain in integrating builder output into a full-suite web application as users of Dash used to experience but with the roll out of django-plotly-dash, this is no longer a problem with Dash.

```{tableofcontents}
```
