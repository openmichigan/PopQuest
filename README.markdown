# PopQuest
### an open, lightweight tool for displaying annotated, captioned educational videos
 
 ---

## the what

This is an MVP (Minimum Viable Product, improvements to come) demo of a tool to display annotated educational videos. With this, one can search in a properly annotated video by subtitle, follow along with captions, and interact with multiple-choice questions that occur within the video, which have feedback on the correctness of the user's response. 

There are scripts to convert ``` .srt ``` caption files and text files with the assets (the video file, the question content) to ``` .JSON ``` for input into the micro-framework.

Written primarily in JavaScript and HTML, with helper Python scripts, built on top of Mozilla's [Popcorn.js](http://popcornjs.org/).

## the dependencies 

* [Popcorn.js](http://popcornjs.org/)
* [jQuery](http://jquery.com/)
* [MediaElement](http://mediaelementjs.com/) video player
* Python 2.7
* a local web server (Tomcat, Apache, whatever you've got)

The MediaElement video player files are included in this GitHub repository in, unsurprisingly, the ``` mediaelement ``` directory, so separate download is not necessary. If you use this directory structure, little alteration is needed within ``` start.html ```. If you change anything about the directory structure or need a different version of jQuery for further development, you may need to make your own changes.

## the who

This was built at the University of Michigan's [MSIS Hack Day](http://msishackday.com) by a team including [Dave Malicke](https://github.com/dmalicke), Sashidhar Guduri, [Jackie Cohen](http://github.com/aerenchyma), Karen Kost, Margaret Ann Murphy, [Trisha Paul](http://illnessnarratives.com), and Johmarx Patton.

## the how

*n.b. some of these directions (the questions text file in particular) is not yet implemented in the current version*

* Clone the repository in the proper folder to be run on a web server (local or otherwise). Make sure the dependencies are in place. 

* Save an ``` .srt ``` file of captions in the root directory. Call it ``` captions.srt ``` (or alter the ``` parse_srt.py ``` file to accommodate your new filename).

* Create a text file of questions formatted as such. (All questions must be multiple choice, single-answer-only.)
	
		Question text
		Answer one that is wrong
		Answer two that is also wrong
		Correct answer*
		Answer three that is not right

		Another question text
		True
		False*

And so on.

Put an asterisk next to the _correct_ answer for each question. 
Make sure there is one empty line between each question block and only one line. See ``` questionfile_example.txt ``` for a template.

Save that file as a ``` .txt ``` file, and put that filename in place in the ``` add_popquest_assets.py ``` script.

* Create another ``` .txt ``` file called ``` videourl.txt ```. Put the appropriate URL or path of an ``` .mp4 ``` video in this file, and nothing else.

* In the console, run the Python scripts: ``` python parse_srt.py ``` and ``` python add_popquest_assets.py ```.

**Without hard-coding and tinkering with the JavaScript, more development is necessary for this point in the process**

* Run the web server.

* There you go.

## features

* Video automatically pauses when questions occur in panel below video.
* Video can be navigated by subtitle (click on the part of the captions in the left sidebar to go to that part of the video).
* Automatic scrolling and highlighting of the proper captions as the video plays.
* Easy addition of resources (links, etc) to go along with the video content.
* Access to the search and interactive learning capabilities without diving into the heavier-weight [MOOC](http://en.wikipedia.org/wiki/Mooc) platforms such as [EdX](https://github.com/edx/edx-platform) (also open source) or [Coursera](https://www.coursera.org/).

## notes

* TODOs include an admin interface and ease of asset addition and video annotation, and further integration between the produced JSON files and the framework itself.
* Hard-coded values in the code here are not also provided in-repo at the moment.
* License of content (e.g. video content) may vary (of course, [Open.Michigan](http://open.umich.edu) encourages the use of [openly licensed](http://open.umich.edu/share/license) content.)

## the [license](/license.md)

[Popcorn.js](http://popcornjs.org/) is licensed under the [MIT License](http://opensource.org/licenses/MIT), Copyright (c) 2010, 2011 Mozilla Foundation. 

The remainder of this product as a whole is &copy; the Regents of the University of Michigan 2013 and is also **licensed under the [MIT License](http://opensource.org/licenses/MIT):**

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.