# Practical Guide
The practical guide is divided into “classes”. In many cases a Class B solution can be just as good as a Class A solution. Class A solutions are complete solutions to any functionality you might have to tackle in a world-class webapp serving hundreds of thousands of hits for thousands if not millions of users. Class B solutions solve a particular problem and do it well.

There was a recent post to reddit Python where a person needed a simple UI for uploading files and then running a process. I recommended the Class B solution Gradio and in a few lines of Python he had a nice-looking application that fulfilled the needs for him and his professor.

So Class A and Class B are excellent solutions. Class C and Class D are lacking in some facet but may still find some use.

## Requirements of a Class A System

1. that it is FULLY featured either directly or by easy integration with another framework that is fully featured. This requirements is in place so that people don’t get burned with a shiny short-term solution that cannot scale out to evolving requirements. Streamlit, Gradio and others are great for single-user web apps, but they do not provide a path for evolution into full-blown industrial strength web applications. **In short: unless a product can directly, or with easy integration do everything in [Miguel Grinberg’s Flask Mega-tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) it is not fully featured.**
1. well-maintained. anything with no source code updates in more than 1 year cannot be considered well-maintained. If there are serious outstanding issues and pull requests this also factors in.
1. well-documented – Ideally all major forms of documentation exist – FAQ, tutorial, Guide and Reference.
1. Good support channels – rapid accurate response to community questions is a must.
1. (New soft criteria) It must efficiently render pages so that it does not present a bottleneck as throughput demands increase. To be a top-100 web property and deal with that amount of traffic requires a complete and efficient hardware and software infrastructure. The web framework itself must only not present a performance bottleneck. (e.g. if it re-computes the whole page on a small change, then it may present a bottleneck)