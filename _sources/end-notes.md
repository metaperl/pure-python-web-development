# End Notes


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

## Let's talk Streamlit

Streamlit is by far the most widely used pure Python web application framework. But it has serious drawbacks:

### It collects a lot of data by default without advance notice

https://www.reddit.com/r/Python/comments/121pvdy/warning_streamlit_collects_a_lot_of_data/

### NiceGUI passed on it

https://github.com/zauberzeug/nicegui/discussions/21

### Solara improved on it

https://solara.dev/docs/tutorial/streamlit

## Performance

Python is the second best language for any task and it's rarely the ideal choice for something that needs to run fast in a single process. That being said, there still need to be some minimum levels of responsiveness to remain useable.

### Rendering large dataframes

Large dataframes [appear to be a common performance bottleneck](https://www.reddit.com/r/Python/comments/13fegbp/comment/jjxntwe/?utm_source=share&utm_medium=web2x&context=3) in the pure python web app space.


## Discussion Threads

Though this survey was designed to summarize available options, sometimes it is useful to go back to the discussion threads and see what everyone has to say:

["NiceGUI vs Plotly/Dash"](https://www.reddit.com/r/nicegui/comments/13c23l8/nicegui_vs_plotlydash/)

"After tearing my hair out writing JavaScript the last few days [how close are we to Python in the browser?](https://www.reddit.com/r/Python/comments/13ccenx/after_tearing_my_hair_out_writing_javascript_the/)"