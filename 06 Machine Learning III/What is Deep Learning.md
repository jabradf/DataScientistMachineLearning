# What Is Deep Learning?

A quick overview of deep learning and its applications

# What is Deep Learning?
Have you ever wondered what powers ChatGPT? What technology developers are using to create self-driving cars? How your phone can recognize faces? Why it seems like your photos app is better at recognizing your friends’ faces than even you can? What is behind all of this? Is it magic? Well, not exactly; it is a powerful technology called deep learning (DL). Let’s dive in and see what this is all about!

![splash](./img/dive_gif.webp)

# Deep Learning vs. Machine Learning

First, let’s focus on learning. If you have come across [machine learning](https://www.codecademy.com/paths/machine-learning/tracks/introduction-to-machine-learning-skill-path/modules/introduction-to-machine-learning-skill-path/lessons/why-machine-learning/exercises/introduction) before, you might be familiar with the concept of a learning model. Learning describes the process by which models analyze data and finds patterns. A machine learning algorithm learns from patterns to find the best representation of this data, which it then uses to make predictions about new data that it has never seen before.

Deep learning is a subfield of machine learning, and the concept of learning is pretty much the same.

* We create our model carefully
* Throw relevant data at it
* Train it on this data
* Have it make predictions for data it has never seen

Deep learning models are used with many different types of data, such as text, images, audio, and more, making them applicable to many different domains.

# What does “deep” mean?
That leaves the question: what is this “deep” aspect of deep learning? It separates deep learning from typical machine learning models and why it is a powerful tool that is becoming more prevalent in today’s society.

The deep part of deep learning refers to the numerous “layers” that transform data. This architecture mimics the structure of the brain, where each successive layer attempts to learn progressively complex patterns from the data fed into the model. This may seem a bit abstract, so let’s look at a concrete example, such as facial recognition. With facial recognition, a deep learning model takes in a photo as an input, and numerous layers perform specific steps to identify whose face is in the picture. The steps taken by each layer might be the following:

1. Find the face within the image using edge detection.
2. Analyze the facial features (eyes, nose, mouth, etc.).
3. Compare against faces within a repository.
4. Output a prediction!

![facial recognition](./img/facial_rec.webp)

This structure of many abstract layers makes deep learning incredibly powerful. Feeding high volumes of data into the model makes the connections between layers more intricate. Deep learning models tend to perform better with more massive amounts of data than other learning algorithms.

# High Volume of Data
Notice that without large amounts of data, deep learning models are no more powerful (and maybe even less accurate) than less complex learning models. However, with large amounts of data, deep learning models can improve performance to the point that they outperform humans in tasks such as classifying objects or faces in images or driving. Deep learning is fundamentally a future learning system (also known as representation learning). It learns from raw data without human intervention. Hence, given massive amounts of data, a deep learning system will perform better than traditional machine learning systems that rely on feature extractions from developers. 

![classic vs deep](./img/Deep-learning-intro.webp)

Autonomous vehicles, such as Tesla, have to process thousands, even millions of stop signs, to understand that cars are supposed to stop when they see a red hexagon with “Stop” written on them (and this is only for U.S. stop signs!). Think about the enormous number of situations a self-driving vehicle must train on to ensure safety.

# With Deep Learning Comes Deep Responsibility
Even beyond identifying objects, deep learning models can generate audio and visual content that is deceivingly real. They can modify existing images, such as in [this cool applet](https://ganpaint.io/#) that allows you to add in trees or alter buildings in a set of photos. However, they can have a darker side. DL models can produce artificial media in which the identity of someone in an image, video, or audio is replaced with someone else. These are known as [deepfakes](https://en.wikipedia.org/wiki/Deepfake), and they can have scary implications, such as [financial fraud](https://web.archive.org/web/20200924073208if_/https://www.forbes.com/sites/jessedamiani/2019/09/03/a-voice-deepfake-was-used-to-scam-a-ceo-out-of-243000/#7d86f8d82241) and the distribution of fake news and hoaxes. 

![Deepfake example](./img/Deepfake_example.webp)

# Graphics Processing Units
One final thing to note about deep learning is that with large amounts of data and layers of complexity, you may imagine that this takes a lot of time and processing power. That intuition would be correct. These models often require high-performance GPUs (graphics processing units) to run in a reasonable amount of time. These processors have a large memory bandwidth and can process multiple computations simultaneously. CPUs can run deep learning models as well; however, they will be much slower.

The development of GPUs has been critical to the success of deep learning. It is interesting to note that one of the driving factors for this development was not the need for better deep learning tools, but the [demand for better video game graphics](https://techcrunch.com/2017/10/27/how-video-game-tech-makes-neural-networks-possible/). It just so happened that GPUs are perfect for processing large datasets. This makes them a perfect tool for learning models and has put deep learning specifically at the forefront of machine learning conversations. 

We have only just begun our dive into deep learning. Let’s keep digging in and see where our journey takes us! 
