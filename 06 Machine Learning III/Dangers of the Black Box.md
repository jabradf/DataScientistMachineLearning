# Dangers of the Black Box

Deep learning models have deep implications.

# What Makes Deep Learning Models Dangerous?
When talking about machine learning, deep learning, and artificial intelligence, people tend to focus on the progress and amazing feats we could potentially achieve. While it is true that these disciplines have the potential to change the world we live in and allow us to perform otherwise impossible feats, there are often unintended consequences.

We live in an imperfect world, and the learning algorithms we design are not immune to these imperfections. Before we dive into creating our models, we must review some of the issues and implications that they can have on people’s lives. Deep Learning models can be especially scary as they are some of the most powerful, and they are becoming more commonplace in society. They are also most often black boxes (hard for users to understand as to why and how specific results occur). 

![black box](./img/Black-box-diagram.svg)

# When to Use Them

Due to this nature of deep learning models, we should only ever use them if there is an apparent, significant reason for using one. If there is not a clear reason, we can use basic machine learning or statistical analysis approaches depending on what suffices.

When choosing solutions to a problem, we have to juggle many numerous factors, including

* speed
* accuracy
* training time
* interpretability
* maintenance
* enhancement
* size of the trained model

along with even more before beginning to prototype. Asking questions along these lines is vital because we design learning algorithms that can harm individuals or even entire communities in their daily lives if we do not craft them with care and awareness.

# Misconceptions
There are often misconceptions about AI and deep learning models and what implications they have on our world. Science fiction has illustrated the dangers as some sort of robot apocalypse where humans are outsmarted and overpowered. This depiction does not reflect the real risks that are already present from the growing dependence on learning models in our everyday lives. Healthcare, banking, and the criminal justice system have all seen a massive rise in the reliance on learning algorithms to make decisions in recent years. While these have led to increased efficiency and developments, trusting these systems to make high-risk decisions has also led to various risks.

# Key Issues
There are some key things to address about machine learning models that can lead to potentially problematic implications. Let’s dive into this through the lens of healthcare.

1. __Machine learning algorithms can only be as good as the data it is trained on.__ If we train the data on a model that does not match environmental data well, accuracy will not translate into the real world. A good example is this [study](https://academic.oup.com/jamia/article/24/6/1052/3096776) on personalized risk assessments for acute kidney injury. While patient data evolved and disease patterns changed, the predictive model became less accurate and, therefore, much less useful. It is crucial for developers to monitor outputs periodically and account for data-shift problems over time. The work is not complete after we deploy a model; it must be managed and continuously refined to account for continuous environmental developments.

    There is also a history of the health industry not including enough women and people of color in medical studies. Different demographics can have unique manifestations and risk factors with diseases. If training data is not diverse and representative of all potential sample individuals, inaccuracies and misdiagnoses could occur. It is vital to have orthogonal data in that it is both high in volume and diversity. Without attention to this, social health disparities that are already present could become widened.

2. __Machine learning models do not understand the impact of a false negative vs. a false positive diagnostic__ (at least not like humans can). When diagnosing patients, doctor’s often “err on the side of caution.” For example, being falsely diagnosed with a malignant tumor (false positive) is much less dangerous than being incorrectly diagnosed with a benign tumor (false negative). Further testing would occur in the former situation, whereas the latter could cause much scarier consequences with a malignant tumor being unaddressed.

    Models may not have this “err on the side of caution” attitude, especially if we do not design them with this implication in mind. If we solely train it to be as accurate as possible, it is at the expense of missing malignant diagnoses. Developers can create custom loss functions that can account for the implications of false negatives vs. false positives. However, to do this, they must understand the domain well.

3. __For many of the clinicians and the patients, the models are a black box__. Stakeholders only can make decisions based on the outcome, and the predictions are not open to inspection. Therefore, it is hard for anyone to determine that there are patterns of inaccurate predictions until prolonged use has already occurred. For example, imagine an X-ray analysis model that is inaccurate under certain conditions because it was not present in the training data. The doctor would not identify this until continuously observing incorrect diagnoses because the only aspect of the model focuses on is the outcome.

![black box](./img/interpretability_cartoon.webp)
(Source: [Christoph Molnar](https://christophm.github.io/))

# More Examples
This is just the tip of the iceberg for concerns about the use of learning models in the healthcare industry, and we have yet to even go into implications within other sectors. Facial recognition has shown implicit bias within Google’s algorithm, which [incorrectly identified a woman and her friend as gorillas](https://web.archive.org/web/20201004111743/https://www.wnycstudios.org/podcasts/notetoself/episodes/deep-problem-deep-learning). An error like this leads to emotional harm, and it shows that learning models are not immune to social issues and can reproduce or even exacerbate them.

Employing black box technology becomes more of an issue when used in contexts without transparency. For example, in criminal justice or banking, biased data is used to deny people of color loans at a higher rate or label them as “high risk” repeat offenders. A real-life example of this is a machine learning questionnaire algorithm known as COMPAS (Correctional Offender Management Profiling for Alternative Sanctions). It was used to determine the risk of whether an arrestee would being a repeat offender. A [study](https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing) showed that this algorithm was racially-biased despite never explicitly asking about race. Individuals were asked questions that modeled existing social inequalities, and minorities, particularly blacks, were more likely to be labeled “high-risk” repeat offenders. The graph below shows the distribution of risk scores for black defendants and white defendants. You can read more about the analysis of this report [here](https://www.propublica.org/article/how-we-analyzed-the-compas-recidivism-algorithm). 

[defendant scores](./img/defendant_scores.webp)
(Source: [ProPublica](https://www.propublica.org/))

Models like these can even go beyond mirroring existing inequity. They can go onto perpetuate them and contribute to vicious cycles. For example, if we were to use systems like these to determine patrol routes, this could bias crime data for individuals in those communities. As we add more data to the learning model, the problem is exacerbated. What is even scarier about these models is that they are often beyond dispute or appeal. Given the result of a mathematical formula, we usually take it as fact. Someone who ends up negatively affected by this cannot argue against it or reason with a machine. They cannot explain the full reality to a computer. Instead, a machine will define its own reality to justify its results. While an outside observer can question, “why did this individual get a high-risk score despite only a minor crime?” a machine is merely operating under its historical data and findings.

# Personal Responsibility
This is not to say that we should not use machine learning models in ways that impact everyday lives. It is meant to outline some of the issues that can arise when used to make high-stakes decisions and how they can cause harm. As you move forward to developing your own neural networks, consider the social implications of what you have made. As developers, we must work to ensure that our models are free from bias and will not misrepresent certain populations. The Institute for Ethical AI and Machine Learning has a [framework for developing responsible machine learning](https://ethical.institute/principles.html) that we encourage you to read up on.

# Interpretability and Transparency
It is also imperative that the models we build are used in ways that are transparent to potential stakeholders. If someone is impacted due to the output of a learning model, they should understand:

* why the model is being used
* how their personal data is being used
* what personal data is being used

The final thing to consider is making your model’s inner workings understandable for your users, also known as interpretable machine learning. Making the inner workings of a model understandable allows users to identify inaccuracies earlier and explain results to potential stakeholders. A great example of this is a simple classifier model that identifies huskies vs. wolves. In the case below, a husky in incorrectly classified as a wolf. With the implementation of a system called [LIME](https://arxiv.org/pdf/1602.04938.pdf), predictions are explained and can be understood by users. In this case, the explanation is that if a picture contains snow, it will be classified as a wolf. This information gives developers an indicator of why their model contains inaccuracies and clarifies how to improve it. 

[husky wolf](./img/husky_wolf.webp)
(Source: [arXiv.org](https://arxiv.org/abs/1602.04938))

# In Conclusion
There is no doubt that machine learning can help us make waves of progress. However, in a world riddled with inequity, developers must attempt design systems so that no one is left behind. By designing learning models that account for limitations of interpretability and likelihood of bias, we can take strides to ensure that individuals and communities are not unjustly harmed.
