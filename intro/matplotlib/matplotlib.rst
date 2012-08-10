===================================
Matplotlib tutorial
===================================
-----------------------------------
Nicolas P. Rougier - Euroscipy 2012
-----------------------------------

.. contents::
   :local:
   :depth: 2

This tutorial is based on Mike Müller `tutorial
<http://scipy-lectures.github.com/intro/matplotlib/matplotlib.html>`_ available
from the `scipy lecture notes <http://scipy-lectures.github.com>`_.

Sources are available from `here <matplotlib.rst>`_. Figures are in the `figures
<figures/>`_ directory and all scripts are located in the `scripts <scripts/>`_
directory.


Introduction
============

matplotlib is probably the single most used Python package for 2D-graphics. It
provides both a very quick way to visualize data from Python and
publication-quality figures in many formats.  We are going to explore
matplotlib in interactive mode covering most common cases.

IPython and the pylab mode
--------------------------

`IPython <http://ipython.org/>`_ is an enhanced interactive Python shell that
has lots of interesting features including named inputs and outputs, access to
shell commands, improved debugging and many more. When we start it with the
command line argument -pylab (--pylab since IPython version 0.12), it allows
interactive matplotlib sessions that has Matlab/Mathematica-like functionality.

pylab
-----

pylab provides a procedural interface to the matplotlib object-oriented
plotting library. It is modeled closely after Matlab(TM). Therefore, the
majority of plotting commands in pylab has Matlab(TM) analogs with similar
arguments.  Important commands are explained with interactive examples.




Simple plot
===========

In this section, we want to draw the cosine and sine functions on the same
plot. Starting from the default settings, we'll enrich the figure step by step
to make it nicer.

First step is to get the data for the sine and cosine functions:

::

   from pylab import *

   X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
   C,S = np.cos(X), np.sin(X)


X is now a numpy array with 256 values ranging from -pi to +pi (included). C is
the cosine (256 values) and S is the sine (256 values).

For running example, you can type them in an IPython interactive session

    $ ipython -pylab

This brings us to the IPython prompt:

::

    IPython 0.8.1 -- An enhanced Interactive Python.
    ?       -> Introduction to IPython's features.
    %magic  -> Information about IPython's 'magic' % functions.
    help    -> Python's own help system.
    object? -> Details about 'object'. ?object also works, ?? prints more.
    
    Welcome to pylab, a matplotlib-based Python environment.
    For more information, type 'help(pylab)'.


or you can download each of the example and run it using regular python:

    $ python exercice_1.py



Using defaults
--------------

.. image:: figures/exercice_1.png
   :align: right
   :target: scripts/exercice_1.py

.. admonition:: Documentation

   * `plot tutorial <http://matplotlib.sourceforge.net/users/pyplot_tutorial.html>`_
   * `plot() command <http://matplotlib.sourceforge.net/api/pyplot_api.html#matplotlib.pyplot.plot>`_

Matplotlib comes with a set of default settings that allow to customize all
kinds of properties. You can control the defaults of almost every property in
matplotlib: figure size and dpi, line width, color and style, axes, axis and
grid properties, text and font properties and so on. While matplotlib defaults
are rather good in most cases, you may want to modify some properties for
specific cases.



::

   from pylab import *

   X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
   C,S = np.cos(X), np.sin(X)

   plot(X,C)
   plot(X,S)

   show()





Instantiating defaults
----------------------

.. image:: figures/exercice_2.png
   :align: right
   :target: scripts/exercice_2.py

.. admonition:: Documentation

   *  `Customizing matplotlib <http://matplotlib.sourceforge.net/users/customizing.html>`_


In the script below, we've instantiated (and commented) all figure settings
such that it shows what are the default settings that influence the
rendering. We obtain the exact same figure but now you can play with the
different parameters to explore how they affect rendering (see `Line
properties`_ and `Line styles`_ below).

::

   # Import everything from matplotlib (numpy is accessible via 'np' alias)
   from pylab import *

   # Create a new figure of size 8x6 points, using 100 dots per inch
   figure(figsize=(8,6), dpi=80)

   # Create a new subplot from a grid of 1x1
   subplot(1,1,1)

   X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
   C,S = np.cos(X), np.sin(X)

   # Plot cosine using blue color with a continuous line of width 1 (pixels)
   plot(X, C, color="blue", linewidth=1.0, linestyle="-")

   # Plot sine using green color with a continuous line of width 1 (pixels)
   plot(X, S, color="green", linewidth=1.0, linestyle="-")

   # Set x limits
   xlim(-4.0,4.0)

   # Set x ticks
   xticks(np.linspace(-4,4,9,endpoint=True))

   # Set y limits
   ylim(-1.0,1.0)

   # Set y ticks
   yticks(np.linspace(-1,1,5,endpoint=True))

   # Save figure using 72 dots per inch
   # savefig("exercice_2.png",dpi=72)

   # Show result on screen
   show()


Changing colors and line widths
--------------------------------

.. image:: figures/exercice_3.png
   :align: right
   :target: scripts/exercice_3.py

.. admonition:: Documentation

   * `Controlling line properties <http://matplotlib.sourceforge.net/users/pyplot_tutorial.html#controlling-line-properties>`_
   * `Line API <http://matplotlib.sourceforge.net/api/artist_api.html#matplotlib.lines.Line2D>`_


First step, we want to have the cosine in blue and the sine in red and a
slighty thicker line for both of them. We'll also slightly alter the figure
size to make it more horizontal.

::

   ...
   figure(figsize=(10,6), dpi=80)
   plot(X, C, color="blue", linewidth=2.5, linestyle="-")
   plot(X, S, color="red",  linewidth=2.5, linestyle="-")
   ...



Setting limits
--------------

.. image:: figures/exercice_4.png
   :align: right
   :target: scripts/exercice_4.py

.. admonition:: Documentation

   * `xlim() command <http://matplotlib.sourceforge.net/api/pyplot_api.html#matplotlib.pyplot.xlim>`_
   * `ylim() command <http://matplotlib.sourceforge.net/api/pyplot_api.html#matplotlib.pyplot.ylim>`_


Current limits of the figure are a bit too tight and we want to make some space
in order to clearly see all data points.

::

   ...
   xlim(X.min()*1.1, X.max()*1.1)
   ylim(C.min()*1.1, C.max()*1.1)
   ...



Setting ticks
-------------

.. image:: figures/exercice_5.png
   :align: right
   :target: scripts/exercice_5.py

.. admonition:: Documentation

   * `xticks() command <http://matplotlib.sourceforge.net/api/pyplot_api.html#matplotlib.pyplot.xticks>`_
   * `yticks() command <http://matplotlib.sourceforge.net/api/pyplot_api.html#matplotlib.pyplot.yticks>`_
   * `Tick container <http://matplotlib.sourceforge.net/users/artists.html#axis-container>`_
   * `Tick locating and formatting <http://matplotlib.sourceforge.net/api/ticker_api.html>`_

Current ticks are not so good because they do not show interesting values
(+/-pi,+/-pi/2) for sine and cosine. We'll change them such that they show only
these values.

::

   ...
   xticks( [-np.pi, -np.pi/2, 0, np.pi/2, np.pi])
   yticks([-1, 0, +1])
   ...




Setting tick labels
-------------------

.. image:: figures/exercice_6.png
   :align: right
   :target: scripts/exercice_6.py

.. admonition:: Documentation

   * `Working with text <http://matplotlib.sourceforge.net/users/index_text.html>`_
   * `xticks() command <http://matplotlib.sourceforge.net/api/pyplot_api.html#matplotlib.pyplot.xticks>`_
   * `yticks() command <http://matplotlib.sourceforge.net/api/pyplot_api.html#matplotlib.pyplot.yticks>`_
   * `set_xticklabels() <http://matplotlib.sourceforge.net/api/axes_api.html?#matplotlib.axes.Axes.set_xticklabels>`_
   * `set_yticklabels() <http://matplotlib.sourceforge.net/api/axes_api.html?#matplotlib.axes.Axes.set_yticklabels>`_

Ticks are now properly placed but their label is not very explicit. We could
guess that 3.142 is pi but it would be better to make it explicit. When we set
ticks values, we can also provide a corresponding label in the second argument
list. Note that we'll use latex to allow for nice rendering of the label.

::

   ...
   xticks( [-np.pi,    -np.pi/2,    0,      np.pi/2,     np.pi],
           [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])

   yticks( [-1,  0,   +1],
           [r'$-1$', r'$0$', r'$+1$'])
   ...


*Complete source*: `exercice_6.py <scripts/exercice_6.py>`_




Moving spines
-------------

.. image:: figures/exercice_7.png
   :align: right
   :target: scripts/exercice_7.py

.. admonition:: Documentation

   * `Spines <http://matplotlib.sourceforge.net/api/spines_api.html#matplotlib.spines>`_
   * `Axis container <http://matplotlib.sourceforge.net/users/artists.html#axis-container>`_
   * `Transformations tutorial <http://matplotlib.sourceforge.net/users/transforms_tutorial.html>`_

Spines are the lines connecting the axis tick marks and noting the boundaries
of the data area. They can be placed at arbitrary positions and until now, they
were on the border of the axis. We'll change that since we want to have them in
the middle. Since there are four of them (top/bottom/left/right), we'll discard
the top and right by setting their color to none and we'll move the bottom and
left ones to coordinate 0 in data space coordinates.


::

   ...
   ax = gca()
   ax.spines['right'].set_color('none')
   ax.spines['top'].set_color('none')
   ax.xaxis.set_ticks_position('bottom')
   ax.spines['bottom'].set_position(('data',0))
   ax.yaxis.set_ticks_position('left')
   ax.spines['left'].set_position(('data',0))
   ...



Adding a legend
---------------

.. image:: figures/exercice_8.png
   :align: right
   :target: scripts/exercice_8.py


.. admonition:: Documentation

   * `Legend guide <http://matplotlib.sourceforge.net/users/legend_guide.html>`_
   * `legend() command <http://matplotlib.sourceforge.net/api/pyplot_api.html#matplotlib.pyplot.legend>`_
   * `Legend API <http://matplotlib.sourceforge.net/api/legend_api.html#matplotlib.legend.Legend>`_


Let's add a legend in the upper left corner. This only requires to give each
plot a label that will be used in the legend box.


::

   ...
   plot(X, C, color="blue", linewidth=2.5, linestyle="-", label="cosine")
   plot(X, S, color="red", linewidth=2.5, linestyle="-",  label="sine")

   legend(loc='upper left')
   ...



Annotate some points
--------------------

.. image:: figures/exercice_9.png
   :align: right
   :target: scripts/exercice_9.py

.. admonition:: Documentation

   * `Annotating axis <http://matplotlib.sourceforge.net/users/annotations_guide.html>`_
   * `annotate() command <http://matplotlib.sourceforge.net/api/pyplot_api.html#matplotlib.pyplot.annotate>`_


Let's annotate some interesting point using the annotate command. We chose then
2pi/3 angle and we want to annotate both the sine and the cosine. We'll first
draw a marker on the curve as well as a straight dotted line. Then, we'll use
the annotate command to display some text with an arrow.

::

   ...

   t = 2*np.pi/3
   plot([t,t],[0,np.cos(t)], color ='blue', linewidth=2.5, linestyle="--")
   scatter([t,],[np.cos(t),], 50, color ='blue')

   annotate(r'$sin(\frac{2\pi}{3})=-\frac{\sqrt{3}}{2}$', xy=(t, np.sin(t)),  xycoords='data',
            xytext=(+10, +30), textcoords='offset points', fontsize=16,
            arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

   plot([t,t],[0,np.sin(t)], color ='red', linewidth=2.5, linestyle="--")
   scatter([t,],[np.sin(t),], 50, color ='red')

   annotate(r'$cos(\frac{2\pi}{3})=-\frac{1}{2}$', xy=(t, np.cos(t)),  xycoords='data',
            xytext=(-90, -50), textcoords='offset points', fontsize=16,
            arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
   ...



Devil is in the details
------------------------

.. image:: figures/exercice_10.png
   :align: right
   :target: scripts/exercice_10.py

.. admonition:: Documentation

   * `Artists <http://matplotlib.sourceforge.net/api/artist_api.html>`_
   * `BBox <http://matplotlib.sourceforge.net/api/artist_api.html#matplotlib.text.Text.set_bbox>`_



Tick labels are now hardly visible because of the blue and red lines. We can
make them bigger and we can also adjust their properties such that they'll be
rendered on a semi-transparent white background. This will allow us to see both
the data and the labels.

::

   ...
   for label in ax.get_xticklabels() + ax.get_yticklabels():
       label.set_fontsize(16)
       label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.65 ))
   ...




Figures, Subplots, Axes and Ticks
=================================

So far we have used implicit figure and axes creation.  This is handy for fast
plots. We can have more control over the display using figure, subplot, and
axes explicitly. A figure in matplotlib means the whole window in the user
interface. Within this figure there can be subplots. While subplot positions
the plots in a regular grid, axes allows free placement within the figure. Both
can be useful depending on your intention. We've already work with figures and
subplots without explicitly calling them. When we call plot matplotlib calls
gca() to get the current axes and gca in turn calls gcf() to get the current
figure. If there is none it calls figure() to make one, strictly speaking, to
make a subplot(111). Let's look at the details.

Figures
-------

A figure is the windows in the GUI that has "Figure #" as title. Figures
are numbered starting from 1 as opposed to the normal Python way starting
from 0. This is clearly MATLAB-style.  There are several parameters that
determine how the figure looks like:

==============  ======================= ============================================
Argument        Default                 Description
==============  ======================= ============================================
num             1                       number of figure
figsize         figure.figsize          figure size in in inches (width, height)
dpi             figure.dpi              resolution in dots per inch
facecolor       figure.facecolor        color of the drawing background
edgecolor       figure.edgecolor        color of edge around the drawing background
frameon         True                    draw figure frame or not
==============  ======================= ============================================

The defaults can be specified in the resource file and will be used most of the
time. Only the number of the figure is frequently changed.

When you work with the GUI you can close a figure by clicking on the x in the
upper right corner. But you can close a figure programmatically by calling
close. Depending on the argument it closes (1) the current figure (no
argument), (2) a specific figure (figure number or figure instance as
argument), or (3) all figures (all as argument).

As with other objects, you can set figure properties also setp or with the
set_something methods.


Subplots
--------

With subplot you can arrange plots in regular grid. You need to specify the
number of rows and columns and the number of the plot. Note that the `gridspec
<http://matplotlib.sourceforge.net/users/gridspec.html>`_ command is a more
powerful alternative.

.. image:: figures/subplot-horizontal.png
   :target: scripts/subplot-horizontal.py
.. image:: figures/subplot-vertical.png
   :target: scripts/subplot-vertical.py
.. image:: figures/subplot-grid.png
   :target: scripts/subplot-grid.py
.. image:: figures/gridspec.png
   :target: scripts/gridspec.py



Axes
----

Axes are very similar to subplots but allow placement of plots at any location
in the figure. So if we want to put a smaller plot inside a bigger one we do
so with axes.

.. image:: figures/axes.png
   :target: scripts/axes.py
.. image:: figures/axes-2.png
   :target: scripts/axes-2.py


Ticks
-----

Well formatted ticks are an important part of publishing-ready
figures. Matplotlib provides a totally configurable system for ticks. There are
tick locators to specify where ticks should appear and tick formatters to make
ticks look like the way you want. Major and minor ticks can be located and
formatted independently from each other. Per default minor ticks are not shown,
i.e. there is only an empty list for them because it is as NullLocator (see
below).

Tick Locators
.............

There are several locators for different kind of requirements:


.. list-table::
   :widths: 20 70
   :header-rows: 1

   * - Class
     - Description


   * - ``NullLocator``
     - No ticks.

       .. image:: figures/ticks-NullLocator.png
     
   * - ``IndexLocator``
     - Place a tick on every multiple of some base number of points plotted.

       .. image:: figures/ticks-IndexLocator.png

   * - ``FixedLocator``
     - Tick locations are fixed.

       .. image:: figures/ticks-FixedLocator.png

   * - ``LinearLocator``
     - Determine the tick locations.

       .. image:: figures/ticks-LinearLocator.png

   * - ``MultipleLocator``
     - Set a tick on every integer that is multiple of some base.

       .. image:: figures/ticks-MultipleLocator.png

   * - ``AutoLocator``
     - Select no more than n intervals at nice locations.

       .. image:: figures/ticks-AutoLocator.png

   * - ``LogLocator``
     - Determine the tick locations for log axes.

       .. image:: figures/ticks-LogLocator.png

All of these locators derive from the base class matplotlib.ticker.Locator.
You can make your own locator deriving from it. Handling dates as ticks can be
especially tricky. Therefore, matplotlib provides special locators in
matplotlib.dates.




Other Types of Plots
====================


.. image:: figures/plot.png
   :target: `Regular Plots`_

.. image:: figures/scatter.png
   :target: `Scatter Plots`_

.. image:: figures/bar.png
   :target: `Bar Plots`_

.. image:: figures/contour.png
   :target: `Contour Plots`_

.. image:: figures/imshow.png
   :target: `Imshow`_

.. image:: figures/quiver.png
   :target: `Quiver Plots`_

.. image:: figures/pie.png
   :target: `Pie Charts`_

.. image:: figures/grid.png
   :target: `Grids`_

.. image:: figures/multiplot.png
   :target: `Multi Plots`_

.. image:: figures/polar.png
   :target: `Polar Axis`_

.. image:: figures/plot3d.png
   :target: `3D Plots`_

.. image:: figures/text.png
   :target: `Text`_


Regular Plots
-------------

.. image:: figures/plot_ex.png
   :align: right
   :target: scripts/plot_ex.py

.. admonition:: Hints

   You need to use the `fill_between
   <http://matplotlib.sourceforge.net/api/pyplot_api.html#matplotlib.pyplot.fill_between>`_
   command.

Starting from the code below, try to reproduce the graphic on the right taking
care of filled areas::

   from pylab import *

   n = 256
   X = np.linspace(-np.pi,np.pi,n,endpoint=True)
   Y = np.sin(2*X)

   plot (X, Y+1, color='blue', alpha=1.00)
   plot (X, Y-1, color='blue', alpha=1.00)
   show()

Click on figure for solution.



Scatter Plots
-------------

.. image:: figures/scatter_ex.png
   :align: right
   :target: scripts/scatter_ex.py

.. admonition:: Hints

   Color is given by angle of (X,Y).


Starting from the code below, try to reproduce the graphic on the right taking
care of marker size, color and transparency.

::

   from pylab import *

   n = 1024
   X = np.random.normal(0,1,n)
   Y = np.random.normal(0,1,n)

   scatter(X,Y)
   show()

Click on figure for solution.




Bar Plots
---------

.. image:: figures/bar_ex.png
   :align: right
   :target: scripts/bar_ex.py

.. admonition:: Hints

   You need to take care of text alignment.


Starting from the code below, try to reproduce the graphic on the right by
adding labels for red bars.

::

   from pylab import *

   n = 12
   X = np.arange(n)
   Y1 = (1-X/float(n)) * np.random.uniform(0.5,1.0,n)
   Y2 = (1-X/float(n)) * np.random.uniform(0.5,1.0,n)

   bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
   bar(X, -Y2, facecolor='#ff9999', edgecolor='white')

   for x,y in zip(X,Y1):
       text(x+0.4, y+0.05, '%.2f' % y, ha='center', va= 'bottom')

   ylim(-1.25,+1.25)
   show()

Click on figure for solution.


Contour Plots
-------------

.. image:: figures/contour_ex.png
   :align: right

.. admonition:: Hints

   You need to use the `clabel
   <http://matplotlib.sourceforge.net/api/pyplot_api.html#matplotlib.pyplot.clabel>`_
   command.

Starting from the code below, try to reproduce the graphic on the right taking
care of the colormap (see `Colormaps`_ below). 

::

   from pylab import *

   def f(x,y): return (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)

   n = 256
   x = np.linspace(-3,3,n)
   y = np.linspace(-3,3,n)
   X,Y = np.meshgrid(x,y)

   contourf(X, Y, f(X,Y), 8, alpha=.75, cmap='jet')
   C = contour(X, Y, f(X,Y), 8, colors='black', linewidth=.5)
   show()

Click on figure for solution.



Imshow
------

.. image:: figures/imshow_ex.png
   :align: right
   :target: scripts/imshow_ex.py

.. admonition:: Hints

   You need to take care of the ``origin`` of the image in the imshow command and
   use a `colorbar
   <http://matplotlib.sourceforge.net/api/pyplot_api.html#matplotlib.pyplot.colorbar>`_


Starting from the code below, try to reproduce the graphic on the right taking
care of colormap, image interpolation and origin.

::

   from pylab import *

   def f(x,y): return (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)

   n = 10
   x = np.linspace(-3,3,4*n)
   y = np.linspace(-3,3,3*n)
   X,Y = np.meshgrid(x,y)
   imshow(f(X,Y)), show()

Click on figure for solution.


Pie Charts
----------

.. image:: figures/pie_ex.png
   :align: right
   :target: scripts/pie_ex.py

.. admonition:: Hints

   You need to modify Z.

Starting from the code below, try to reproduce the graphic on the right taking
care of colors and slices size.

::

   from pylab import *

   n = 20
   Z = np.random.uniform(0,1,n)
   pie(Z), show()

Click on figure for solution.



Quiver Plots
------------

.. image:: figures/quiver_ex.png
   :align: right
   :target: scripts/quiver_ex.py

.. admonition:: Hints

   You need to draw arrows twice.

Starting from the code above, try to reproduce the graphic on the right taking
care of colors and orientations.

::

   from pylab import *

   n = 8
   X,Y = np.mgrid[0:n,0:n]
   quiver(X,Y), show()

Click on figure for solution.



Grids
-----

.. image:: figures/grid_ex.png
   :align: right
   :target: scripts/grid_ex.py


Starting from the code below, try to reproduce the graphic on the right taking
care of line styles.

::

   from pylab import *

   axes = gca()
   axes.set_xlim(0,4)
   axes.set_ylim(0,3)
   axes.set_xticklabels([])
   axes.set_yticklabels([])

   show()

Click on figure for solution.


Multi Plots
-----------

.. image:: figures/multiplot_ex.png
   :align: right
   :target: scripts/multiplot_ex.py

.. admonition:: Hints

   You can use several subplots with different partition.


Starting from the code below, try to reproduce the graphic on the right.

::

   from pylab import *

   subplot(2,2,1)
   subplot(2,2,3)
   subplot(2,2,4)

   show()

Click on figure for solution.


Polar Axis
----------

.. image:: figures/polar_ex.png
   :align: right
   :target: scripts/polar_ex.py

.. admonition:: Hints

   You only need to modify the ``axes`` line


Starting from the code below, try to reproduce the graphic on the right.

::

   from pylab import *

   axes([0,0,1,1])

   N = 20
   theta = np.arange(0.0, 2*np.pi, 2*np.pi/N)
   radii = 10*np.random.rand(N)
   width = np.pi/4*np.random.rand(N)
   bars = bar(theta, radii, width=width, bottom=0.0)

   for r,bar in zip(radii, bars):
       bar.set_facecolor( cm.jet(r/10.))
       bar.set_alpha(0.5)

   show()

Click on figure for solution.


3D Plots
--------

.. image:: figures/plot3d_ex.png
   :align: right
   :target: scripts/plot3d_ex.py

.. admonition:: Hints

   You need to use `contourf
   <http://matplotlib.sourceforge.net/api/pyplot_api.html#matplotlib.pyplot.contourf>`_


Starting from the code below, try to remove reproduce the graphic on the right.

::

   from pylab import *
   from mpl_toolkits.mplot3d import Axes3D

   fig = figure()
   ax = Axes3D(fig)
   X = np.arange(-4, 4, 0.25)
   Y = np.arange(-4, 4, 0.25)
   X, Y = np.meshgrid(X, Y)
   R = np.sqrt(X**2 + Y**2)
   Z = np.sin(R)

   ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='hot')

   show()

Click on figure for solution.



Text
----

.. image:: figures/text_ex.png
  :align: right
  :target: scripts/text_ex.py

.. admonition:: Hints

   Have a look at the `matplotlib logo
   <http://matplotlib.sourceforge.net/examples/api/logo2.html>`_.

Try to do the same from scratch !

Click on figure for solution.


Beyond this tutorial
====================

Matplotlib benefits from an extensive documentation as well as a large
community of users and developpers. Here are some links of interests:

Tutorials
---------

* `Pyplot tutorial <http://matplotlib.sourceforge.net/users/pyplot_tutorial.html>`_

  - Introduction
  - Controlling line properties
  - Working with multiple figures and axes
  - Working with text
  - 

* `Image tutorial <http://matplotlib.sourceforge.net/users/image_tutorial.html>`_

  - Startup commands
  - Importing image data into Numpy arrays
  - Plotting numpy arrays as images
  - 

* `Text tutorial <http://matplotlib.sourceforge.net/users/index_text.html>`_

  - Text introduction
  - Basic text commands
  - Text properties and layout
  - Writing mathematical expressions
  - Text rendering With LaTeX
  - Annotating text
  - 

* `Artist tutorial <http://matplotlib.sourceforge.net/users/artists.html>`_

  - Introduction
  - Customizing your objects
  - Object containers
  - Figure container
  - Axes container
  - Axis containers
  - Tick containers
  - 

* `Path tutorial <http://matplotlib.sourceforge.net/users/path_tutorial.html>`_

  - Introduction
  - Bézier example
  - Compound paths
  - 

* `Transforms tutorial <http://matplotlib.sourceforge.net/users/transforms_tutorial.html>`_

  - Introduction
  - Data coordinates
  - Axes coordinates
  - Blended transformations
  - Using offset transforms to create a shadow effect
  - The transformation pipeline
  - 



Matplotlib documentation
------------------------

* `User guide <http://matplotlib.sourceforge.net/users/index.html>`_

* `FAQ <http://matplotlib.sourceforge.net/faq/index.html>`_

  - Installation
  - Usage
  - How-To
  - Troubleshooting
  - Environment Variables
  - 

* `Screenshots <http://matplotlib.sourceforge.net/users/screenshots.html>`_


Code documentation
------------------

The code is fairly well documented and you can quickly access a specific
command from within a python session:

::

   >>> from pylab import *
   >>> help(plot)
   Help on function plot in module matplotlib.pyplot:

   plot(*args, **kwargs)
      Plot lines and/or markers to the
      :class:`~matplotlib.axes.Axes`.  *args* is a variable length
      argument, allowing for multiple *x*, *y* pairs with an
      optional format string.  For example, each of the following is
      legal::
    
          plot(x, y)         # plot x and y using default line style and color
          plot(x, y, 'bo')   # plot x and y using blue circle markers
          plot(y)            # plot y using x as index array 0..N-1
          plot(y, 'r+')      # ditto, but with red plusses
    
      If *x* and/or *y* is 2-dimensional, then the corresponding columns
      will be plotted.
      ...

Galleries
---------

The `matplotlib gallery <http://matplotlib.sourceforge.net/gallery.html>`_ is
also incredibly useful when you search how to render a given graphics. Each
example comes with its source.

A smaller gallery is also available `here <http://www.loria.fr/~rougier/coding/gallery/>`_.


Mailing lists
--------------

Finally, there is a `user mailing list
<https://lists.sourceforge.net/lists/listinfo/matplotlib-users>`_ where you can
ask for help and a `developers mailing list
<https://lists.sourceforge.net/lists/listinfo/matplotlib-devel>`_ that is more
technical.



Quick references
================

Here is a set of tables that show main properties and styles.

Line properties
----------------

.. list-table::
   :widths: 15 30 50
   :header-rows: 1

   * - Property
     - Description
     - Appearance

   * - alpha (or a)
     - alpha transparency on 0-1 scale
     - .. image:: figures/alpha.png

   * - antialiased
     - True or False - use antialised rendering
     - .. image:: figures/aliased.png
       .. image:: figures/antialiased.png

   * - color (or c)
     - matplotlib color arg
     - .. image:: figures/color.png

   * - linestyle (or ls)
     - see `Line properties`_
     -

   * - linewidth (or lw)
     - float, the line width in points
     - .. image:: figures/linewidth.png

   * - solid_capstyle
     - Cap style for solid lines
     - .. image:: figures/solid_capstyle.png

   * - solid_joinstyle
     - Join style for solid lines
     - .. image:: figures/solid_joinstyle.png

   * - dash_capstyle
     - Cap style for dashes
     - .. image:: figures/dash_capstyle.png

   * - dash_joinstyle
     - Join style for dashes
     - .. image:: figures/dash_joinstyle.png

   * - marker
     - see `Markers`_
     -

   * - markeredgewidth (or mew)
     - line width around the marker symbol
     - .. image:: figures/mew.png

   * - markeredgecolor (or mec)
     - edge color if a marker is used
     - .. image:: figures/mec.png

   * - markerfacecolor (or mfc)
     - face color if a marker is used
     - .. image:: figures/mfc.png

   * - markersize (or ms)
     - size of the marker in points
     - .. image:: figures/ms.png



Line styles
-----------

.. list-table::
   :widths: 15 30 50
   :header-rows: 1

   * - Symbol
     - Description
     - Appearance

   * - ``-``
     - solid line
     - .. image:: figures/linestyle--.png

   * - ``--``
     - dashed line
     - .. image:: figures/linestyle---.png

   * - ``-.``
     - dash-dot line
     - .. image:: figures/linestyle--dot.png

   * - ``:``
     - dotted line
     - .. image:: figures/linestyle-:.png

   * - ``.``
     - points
     - .. image:: figures/linestyle-dot.png

   * - ``,``
     - pixels
     - .. image:: figures/linestyle-,.png
     
   * - ``o``
     - circle
     - .. image:: figures/linestyle-o.png

   * - ``^``
     - triangle up
     - .. image:: figures/linestyle-^.png

   * - ``v``
     - triangle down
     - .. image:: figures/linestyle-v.png

   * - ``<``
     - triangle left
     - .. image:: figures/linestyle-<.png

   * - ``>``
     - triangle right
     - .. image:: figures/linestyle->.png

   * - ``s``
     - square
     - .. image:: figures/linestyle-s.png

   * - ``+``
     - plus
     - .. image:: figures/linestyle-+.png

   * - ``x``
     -  cross
     - .. image:: figures/linestyle-x.png

   * - ``D``
     - diamond
     - .. image:: figures/linestyle-dd.png

   * - ``d``
     - thin diamond
     - .. image:: figures/linestyle-d.png

   * - ``1``
     - tripod down
     - .. image:: figures/linestyle-1.png

   * - ``2``
     - tripod up
     - .. image:: figures/linestyle-2.png

   * - ``3``
     - tripod left
     - .. image:: figures/linestyle-3.png

   * - ``4``
     - tripod right
     - .. image:: figures/linestyle-4.png

   * - ``h``
     - hexagon
     - .. image:: figures/linestyle-h.png

   * - ``H``
     - rotated hexagon
     - .. image:: figures/linestyle-hh.png

   * - ``p``
     -  pentagon
     - .. image:: figures/linestyle-p.png

   * - ``|``
     - vertical line
     - .. image:: figures/linestyle-|.png

   * - ``_``
     - horizontal line
     - .. image:: figures/linestyle-_.png


Markers
-------


.. list-table::
   :widths: 15 30 50
   :header-rows: 1

   * - Symbol
     - Description
     - Appearance

   * - 0
     - tick left
     - .. image:: figures/marker-i0.png

   * - 1
     - tick right
     - .. image:: figures/marker-i1.png

   * - 2
     - tick up
     - .. image:: figures/marker-i2.png

   * - 3
     - tick down
     - .. image:: figures/marker-i3.png

   * - 4
     - caret left
     - .. image:: figures/marker-i4.png

   * - 5
     - caret right
     - .. image:: figures/marker-i5.png

   * - 6
     - caret up
     - .. image:: figures/marker-i6.png

   * - 7
     - caret down
     - .. image:: figures/marker-i7.png

   * - ``o``
     - circle
     - .. image:: figures/marker-o.png

   * - ``D``
     - diamond
     - .. image:: figures/marker-dd.png

   * - ``h``
     - hexagon 1
     - .. image:: figures/marker-h.png

   * - ``H``
     - hexagon 2
     - .. image:: figures/marker-hh.png

   * - ``_``
     - horizontal line
     - .. image:: figures/marker-_.png

   * - ``1``
     - tripod down
     - .. image:: figures/marker-1.png

   * - ``2``
     - tripod up
     - .. image:: figures/marker-2.png

   * - ``3``
     - tripod left
     - .. image:: figures/marker-3.png

   * - ``4``
     - tripod right
     - .. image:: figures/marker-4.png

   * - ``8``
     - octagon
     - .. image:: figures/marker-8.png

   * - ``p``
     - pentagon
     - .. image:: figures/marker-p.png

   * - ``^``
     - triangle up
     - .. image:: figures/marker-^.png

   * - ``v``
     - triangle down
     - .. image:: figures/marker-v.png

   * - ``<``
     - triangle left
     - .. image:: figures/marker-<.png

   * - ``>``
     - triangle right
     - .. image:: figures/marker->.png

   * - ``d``
     - thin diamond
     - .. image:: figures/marker-d.png

   * - ``,``
     - pixel
     - .. image:: figures/marker-,.png

   * - ``+``
     - plus
     - .. image:: figures/marker-+.png

   * - ``.``
     - point
     - .. image:: figures/marker-dot.png

   * - ``s``
     - square
     - .. image:: figures/marker-s.png

   * - ``*``
     - star
     - .. image:: figures/marker-*.png

   * - ``|``
     - vertical line
     - .. image:: figures/marker-|.png

   * - ``x``
     - cross
     - .. image:: figures/marker-x.png

   * - ``r'$\sqrt{2}$'``
     - any latex expression
     - .. image:: figures/marker-latex.png




Colormaps
---------

All colormaps can be reversed by appending ``_r``. For instance, ``gray_r`` is
the reverse of ``gray``.

If you want to know more about colormaps, checks `Documenting the matplotlib
colormaps <https://gist.github.com/2719900>`_.


Base
....

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Name
     - Appearance

   * - autumn
     - .. image:: figures/cmap-autumn.png

   * - bone
     - .. image:: figures/cmap-bone.png

   * - cool
     - .. image:: figures/cmap-cool.png

   * - copper
     - .. image:: figures/cmap-copper.png

   * - flag
     - .. image:: figures/cmap-flag.png

   * - gray
     - .. image:: figures/cmap-gray.png

   * - hot
     - .. image:: figures/cmap-hot.png

   * - hsv
     - .. image:: figures/cmap-hsv.png

   * - jet
     - .. image:: figures/cmap-jet.png

   * - pink
     - .. image:: figures/cmap-pink.png

   * - prism
     - .. image:: figures/cmap-prism.png

   * - spectral
     - .. image:: figures/cmap-spectral.png

   * - spring
     - .. image:: figures/cmap-spring.png

   * - summer
     - .. image:: figures/cmap-summer.png

   * - winter
     - .. image:: figures/cmap-winter.png


GIST
....

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Name
     - Appearance

   * - gist_earth
     - .. image:: figures/cmap-gist_earth.png

   * - gist_gray
     - .. image:: figures/cmap-gist_gray.png

   * - gist_heat
     - .. image:: figures/cmap-gist_heat.png

   * - gist_ncar
     - .. image:: figures/cmap-gist_ncar.png

   * - gist_rainbow
     - .. image:: figures/cmap-gist_rainbow.png

   * - gist_stern
     - .. image:: figures/cmap-gist_stern.png

   * - gist_yarg
     - .. image:: figures/cmap-gist_yarg.png


Sequential
..........

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Name
     - Appearance

   * - BrBG
     - .. image:: figures/cmap-BrBG.png

   * - PiYG
     - .. image:: figures/cmap-PiYG.png

   * - PRGn
     - .. image:: figures/cmap-PRGn.png

   * - PuOr
     - .. image:: figures/cmap-PuOr.png

   * - RdBu
     - .. image:: figures/cmap-RdBu.png

   * - RdGy
     - .. image:: figures/cmap-RdGy.png

   * - RdYlBu
     - .. image:: figures/cmap-RdYlBu.png

   * - RdYlGn
     - .. image:: figures/cmap-RdYlGn.png

   * - Spectral
     - .. image:: figures/cmap-Spectral.png



Diverging
.........

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Name
     - Appearance

   * - Blues
     - .. image:: figures/cmap-Blues.png

   * - BuGn
     - .. image:: figures/cmap-BuGn.png

   * - BuPu
     - .. image:: figures/cmap-BuPu.png

   * - GnBu
     - .. image:: figures/cmap-GnBu.png

   * - Greens
     - .. image:: figures/cmap-Greens.png

   * - Greys
     - .. image:: figures/cmap-Greys.png

   * - Oranges
     - .. image:: figures/cmap-Oranges.png

   * - OrRd
     - .. image:: figures/cmap-OrRd.png

   * - PuBu
     - .. image:: figures/cmap-PuBu.png

   * - PuBuGn
     - .. image:: figures/cmap-PuBuGn.png

   * - PuRd
     - .. image:: figures/cmap-PuRd.png

   * - Purples
     - .. image:: figures/cmap-Purples.png

   * - RdPu
     - .. image:: figures/cmap-RdPu.png

   * - Reds
     - .. image:: figures/cmap-Reds.png

   * - YlGn
     - .. image:: figures/cmap-YlGn.png

   * - YlGnBu
     - .. image:: figures/cmap-YlGnBu.png

   * - YlOrBr
     - .. image:: figures/cmap-YlOrBr.png

   * - YlOrRd
     - .. image:: figures/cmap-YlOrRd.png


Qualitative
...........

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Name
     - Appearance

   * - Accent
     - .. image:: figures/cmap-Accent.png

   * - Dark2
     - .. image:: figures/cmap-Dark2.png

   * - Paired
     - .. image:: figures/cmap-Paired.png

   * - Pastel1
     - .. image:: figures/cmap-Pastel1.png

   * - Pastel2
     - .. image:: figures/cmap-Pastel2.png

   * - Set1
     - .. image:: figures/cmap-Set1.png

   * - Set2
     - .. image:: figures/cmap-Set2.png

   * - Set3
     - .. image:: figures/cmap-Set3.png



Miscellaneous
.............

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Name
     - Appearance


   * - afmhot
     - .. image:: figures/cmap-afmhot.png


   * - binary
     - .. image:: figures/cmap-binary.png

   * - brg
     - .. image:: figures/cmap-brg.png

   * - bwr
     - .. image:: figures/cmap-bwr.png

   * - coolwarm
     - .. image:: figures/cmap-coolwarm.png

   * - CMRmap
     - .. image:: figures/cmap-CMRmap.png

   * - cubehelix
     - .. image:: figures/cmap-cubehelix.png

   * - gnuplot
     - .. image:: figures/cmap-gnuplot.png

   * - gnuplot2
     - .. image:: figures/cmap-gnuplot2.png

   * - ocean
     - .. image:: figures/cmap-ocean.png

   * - rainbow
     - .. image:: figures/cmap-rainbow.png

   * - seismic
     - .. image:: figures/cmap-seismic.png

   * - terrain
     - .. image:: figures/cmap-terrain.png
