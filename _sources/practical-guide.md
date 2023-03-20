# Practical Guide
The practical guide is divided into “classes”. In many cases a Class B solution can be just as good as a Class A solution. Class A solutions are complete solutions to any functionality you might have to tackle in a world-class webapp serving hundreds of thousands of hits for thousands if not millions of users. Class B solutions solve a particular problem and do it well.

There was a recent post to reddit Python where a person needed a simple UI for uploading files and then running a process. I recommended the Class B solution Gradio and in a few lines of Python he had a nice-looking application that fulfilled the needs for him and his professor.

So Class A and Class B are excellent solutions. Class C and Class D are lacking in some facet but may still find some use.

## Requirements of a Class A System

that it is fully featured either directly or by easy integration with another framework that is fully featured. This requirements is in place so that people don’t get burned with a shiny short-term solution that cannot scale out to evolving requirements. Streamlit, Gradio and others are great for single-user web apps, but they do not provide a path for evolution into full-blown industrial strength web applications. In short: unless a product can directly, or with easy integration do everything in Miguel Grinberg’s Flask Mega-tutorial it is not fully featured.
well-maintained – anything with no source code updates in more than 1 year cannot be considered well-maintained. If there are serious outstanding issues and pull requests this also factors in.
well-documented – Ideally all major forms of documentation exist – FAQ, tutorial, Guide and Reference.
Good support channels – rapid accurate response to community questions is a must.
(New soft criteria) It must scale to handle 1 million requests per second or more. Cute little toy apps running on your personal Macbook pro are nice, but the world’s top 100 web properties have much higher demands for seamlessly handling large amounts of traffic. If the web solution cannot produce a site like amazon.com and handle the web traffic like amazon.com then it might be OK for building a toy app for your local barber, but it will never survive at the top level in demanding industrial situations.