#  365 Days Challenge — AI × Astrophysics 

> “Somewhere, something incredible is waiting to be known.” — Carl Sagan  

Welcome to my **365 Days of GitHub Challenge**, where I’ll combine my passion for **Machine Learning** 🤖 and **Astrophysics** 🌠 to learn, build, and share projects every single day for one year!

---

##  Challenge Goal

-  Learn and apply **AI/ML concepts** daily  
-  Explore **real astrophysics datasets** (NASA, ESA, etc.)  
-  Build, document, and publish **projects** on GitHub  
-  Maintain **1 commit per day** for 365 days  
-  Share progress and inspire others to learn AI for space!

**Start Date:** November 8, 2025  
**End Date:** November 7, 2026  

---

##  Yearly Roadmap (12-Month Plan)

| Month | Theme | Focus | Status |
|-------|--------|--------|--------|
| **Nov 2025** |  Foundations | Python, Git, ML basics | 🟢 Ongoing |
| **Dec 2025** |  Core ML Projects | Classification, clustering | ⬜ Pending |
| **Jan 2026** |  Deep Learning | CNNs, PyTorch | ⬜ Pending |
| **Feb 2026** |  Astronomy Data 101 | FITS files, AstroPy, AstroML | ⬜ Pending |
| **Mar 2026** |  Galaxy Classifier | Galaxy Zoo, CNN | ⬜ Pending |
| **Apr 2026** |  Exoplanet & Signal ML | Kepler data, time series | ⬜ Pending |
| **May 2026** |  Solar Flare Prediction | LSTM, forecasting | ⬜ Pending |
| **Jun 2026** |  Generative Space | GANs, diffusion models | ⬜ Pending |
| **Jul 2026** |  AI for Physics Simulations | N-body & particle data | ⬜ Pending |
| **Aug 2026** |  Open Source Month | Contribute to AstroML / Astropy | ⬜ Pending |
| **Sep 2026** |  Research + Visualization | Space analytics dashboards | ⬜ Pending |
| **Oct 2026** |  Capstone Build | AI-Powered Astronomy Explorer | ⬜ Pending |

---

##  Monthly Focus (Example Breakdown)

###  Month 3: Galaxy Classification Project
**Goal:** Build a CNN to classify galaxies (spiral, elliptical, irregular).  
**Dataset:** [Galaxy Zoo](https://www.kaggle.com/c/galaxy-zoo-the-galaxy-challenge/data)  
**Tools:** PyTorch, AstroPy, Matplotlib  
**Tasks:**
- Week 1: Load & clean dataset  
- Week 2: Train CNN  
- Week 3: Tune hyperparameters  
- Week 4: Visualize & deploy results  

---

##  Daily Log

| Day | Date | Activity | Notes |
|-----|------|-----------|-------|
| 1 | Nov 8, 2025 | Initialized repo, created README | Set up challenge plan |
| 2 | Nov 9, 2025 | Reviewed Python and Git basics | Installed AstroPy, TensorFlow |
| 3 | Nov 10, 2025 | Practiced linear regression | Started simple ML notebooks |
| 4 | Nov 11, 2025 | Visualized galaxy dataset | Used Matplotlib & Pandas |
| ... | ... | ... | ... |


---

##  Tools & Libraries

- **Languages:** Python  
- **Frameworks:** PyTorch, TensorFlow, Scikit-learn  
- **Astronomy Tools:** AstroPy, AstroML, FITS I/O  
- **Visualization:** Matplotlib, Plotly, Seaborn  
- **Dev Tools:** Git, GitHub, Jupyter, VS Code  

---

##  Progress Tracker

| Milestone | Goal | Status |
|------------|------|--------|
|  30 Days | Complete daily commits for 1 month | ⬜ |
|  100 Days | Finish 3 AI mini-projects | ⬜ |
|  200 Days | Publish 1 AstroML project | ⬜ |
|  300 Days | Contribute to open source | ⬜ |
|  365 Days | Complete Capstone & Reflect | ⬜ |

---

## 🧭 Connect & Collaborate

If you’re also into **AI + Space**, feel free to collaborate or share ideas!  
🌐 **GitHub:** [Kritimbist](https://github.com/Kritimbist)  
  
---

### ⭐ Support

If you like this challenge or find it inspiring, **star this repo** ⭐ to support the journey!








## Day 001 : Data Distribution using python

Today i learn about the concept of data distribution and some of it's examples .  Data distribution show how data values are spread out and it helps in :

- Detect outliers
- See if your data is balanced or skewed
- Decide whether you need normalization or transformation
- Detect imbalanced classes in classification problems

I've use  python module Numpy, where we can create random data sets of any size.
# some of the examples  of data distribution

<img width="964" height="770" alt="image" src="https://github.com/user-attachments/assets/57749f77-cf2c-46f3-b43a-44510f7004f1" />




## Day 002 : Visualizing Data Distribution using python

Today i learn about how to visualize the distributed data . 


## 📈 Visualization Types


###  Histogram
A **histogram** shows how data is distributed by grouping values into bins.
We will use the Python module Matplotlib to draw a histogram.
# sample example of histogram:
<img width="846" height="702" alt="image" src="https://github.com/user-attachments/assets/ccce542b-ba96-441a-b9a3-e128832cc591" />



##  Normal Distribution 

A **normal distribution** is characterized by:
- A **mean (μ)** — the center of the curve  
- A **standard deviation (σ)** — controls how spread out the data is  

The formula for the probability density function is:

A Probability Density Function (PDF) is a mathematical function that tells you how likely a continuous outcome (like height, time, or temperature) is to fall within a certain range.

$$
f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2}
$$

# Simple example of visualizing noram distribution:
<img width="762" height="689" alt="image" src="https://github.com/user-attachments/assets/cfdae9be-9ef1-4375-934f-958fc60c7149" />



##  scatter plot
A scatter plot is a diagram where each value in the data set is represented by a dot.
<img width="640" height="480" alt="image" src="https://github.com/user-attachments/assets/168d08ea-cf6f-43cb-aa75-625004600152" />

The Matplotlib module has a method for drawing scatter plots, it needs two arrays of the same length, one for the values of the x-axis, and one for the values of the y-axis:
- x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
- y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

Use the scatter() method to draw a scatter plot diagram.

# Simple example of scatter plot :

<img width="907" height="726" alt="image" src="https://github.com/user-attachments/assets/c2e18951-9daf-44a9-8334-456b80893b05" />

## Random Data Distributions
In Machine Learning the data sets can contain thousands-, or even millions, of values.
You might not have real world data when you are testing an algorithm, you might have to use randomly generated values.

Let us create two arrays that are both filled with 1000 random numbers from a normal data distribution.
The first array will have the mean set to 5.0 with a standard deviation of 1.0.
The second array will have the mean set to 10.0 with a standard deviation of 2.0:

simple examples of random data distribution :
<img width="904" height="705" alt="image" src="https://github.com/user-attachments/assets/eb810ce1-a45e-417d-a215-b7a58628f7ad" />




