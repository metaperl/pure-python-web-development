# End Notes

## Let's talk Streamlit

Streamlit is by far the most widely used pure Python web application framework. But it has serious drawbacks:

### It collects a lot of data by default without advance notice

https://www.reddit.com/r/Python/comments/121pvdy/warning_streamlit_collects_a_lot_of_data/

### NiceGUI passed on it

https://github.com/zauberzeug/nicegui/discussions/21

### Solara improved on it

https://solara.dev/docs/tutorial/streamlit

### Jacob Ferus criticized it

Jacob Ferus reveals [some shocking limitations](https://medium.com/@dreamferus/should-you-build-your-next-app-in-streamlit-b01adc007f1c) in his article - 

> Streamlit is very constrained. Oh, you would like to change the color of a button? Sorry, no way to do it. You want to add some Javascript/HTML/CSS, nope! Do you need a popup? No, not possible. Some would argue you could do some of these things but it will require ugly hacks. My point is, if you would like to do anything that isn’t part of the rather small set of existing options, you’re going to have a bad time. 

He also covers the inefficiency issue that others have noticed.

### Taipy passed on Streamlit as well.

> we created Taipy because we found that Streamlit fell short when it came to production projects. The whole re-running of your entire code when you press a button and having the front and back on the same thread makes any app that is a bit complex unusable. We also wanted to focus on other business needs like proper support for multi-user, Jupyter, and data orchestration.
> -- [Alyx1337](https://www.reddit.com/r/Python/comments/171dyn9/comment/k3st6ns/?utm_source=share&utm_medium=web2x&context=3)

### Shiny assessed it

Joe Cheng, in his [pydata nyc talk](https://youtu.be/ijRBbtT2tgc?t=342) explains why Shiny is preferable to Streamlit. He absolutely torches the "restart and run-all" model of Streamlit.

### Panel developed a transition guide



The [Panel project](https://panel.holoviz.org) has several articles in which [they compare panel to other frameworks](https://panel.holoviz.org/explanation/index.html#technology-comparisons). Recently, they developed [a guide on switching from Streamlit to Panel](https://panel.holoviz.org/how_to/streamlit_migration/index.html). In doing so, there was no section explicitly motivating such a switch, but I did notice this in [one section](https://panel.holoviz.org/how_to/streamlit_migration/interactivity.html):

Both Streamlit and Panel are reactive frameworks that react when you interact with your application. But they work very differently:

In Streamlit

- your script is run once when a user visits the page.
- your script is rerun top to bottom on user interactions.

In Panel
- your script is run once when a user visits the page.
- only specific, bound functions are rerun on user interactions.

With Panel's interactive architecture you will be able to develop and maintain larger and more complex apps.

Also, [a recent tweet by Marc Skov Madsen](https://twitter.com/MarcSkovMadsen/status/1676958078632353792) mentions a number of advantages:

- integrations to HoloViz, ipywidgets and VTK
- events and crossfiltering
-streaming and async
- possibility to unittest with pytest
- no “run script top to bottom” or session state limitations
- works in Jupyter too

And much, much more



## React in Python –

### Transcrypt

[An entire book](https://pyreact.com) has been written on using React from Transcrypt. That being said,
Transcrypt is [suffering from some maintenance issues](https://may69.com/downgrades-and-upgrades-to-the-rating-of-pure-python-web-application-solutions/).

### enter Pynecone
Pynecone is a new project that compiles to the NextJS flavor of React. It has an impressive gallery.

### Now ReactPy

https://www.reddit.com/r/Python/comments/1274w68/reactpy_build_reactjs_interfaces_in_pure_python/

### (Ryact and Breact omitted)

### Tangential Products
#### Reacton
Reacton implements the React API in Python, [overcoming the same problems as web applications in the jQuery era (state transitions being the biggest issue).](https://www.reddit.com/r/Python/comments/zkxq1j/reacton_a_pure_python_port_of_react_for_ipywidgets/). It has a web framework built on top of it - [Solara](https://solara.dev).


#### py-react
py-react supports running Python in the browser via Pyodide. That being said, it does not appear to be aspiring to be a web application toolkit like other python-in-the-browser products (skulpt, brython, pyscript). Thus py-react is listed here in the tangential section. You may try it out here.

##### Discussion threads for this product:

“Python code running in the browser using react-py“


## Performance

Python is the second best language for any task and it's rarely the ideal choice for something that needs to run fast in a single process. That being said, there still need to be some minimum levels of responsiveness to remain useable.

### Rendering large dataframes

Large dataframes [appear to be a common performance bottleneck](https://www.reddit.com/r/Python/comments/13fegbp/comment/jjxntwe/?utm_source=share&utm_medium=web2x&context=3) in the pure python web app space.


## Discussion Threads

Though this survey was designed to summarize available options, sometimes it is useful to go back to the discussion threads and see what everyone has to say:

["NiceGUI vs Plotly/Dash"](https://www.reddit.com/r/nicegui/comments/13c23l8/nicegui_vs_plotlydash/)

"After tearing my hair out writing JavaScript the last few days [how close are we to Python in the browser?](https://www.reddit.com/r/Python/comments/13ccenx/after_tearing_my_hair_out_writing_javascript_the/)"