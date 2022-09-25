
# Bias and Fairness in NLP, Benchmark Datasets as Evaluation Tools

This is intended as a documneted archive of my senior research project.

# Summery
There are some serious ethical implications when machine learning models carry out human biases, whether intended or not. There are many ways in which bias can creep into our model. To evaluate bias models, we explored fairness metrics in a natural language processing (NLP) setting using a BERT model. Specifically, in the context of hate speech classification. This allows us to explore the limitations of these metrics. Through experimental testing, we compare the explanatory power of the balanced accuracy metric as compared to F1 scores and accuracy. These metricts where evaluated against the hateXplain benchmarking dataset and hate speech and offensive language dataset. 


# Folders
~~~
./BERT                  --> Contains the notbooks for model training and inferance
./BERT/outputs          --> Contains the raw classificaiton outputs and analysis
./BERT/hate_speech_bert --> Contains the model chackpoint of BERT train on the "hate speech and offensive language dataset"
~~~


# Datasets Used

## HateSpeech and offensive language

  Thomas Davidson, Dana Warmsley, Michael Macy, and Ingmar Weber. 2017. "Automated Hate Speech Detection and the Problem of Offensive Language." ICWSM

https://github.com/t-davidson/hate-speech-and-offensive-language

@inproceedings{hateoffensive,
  title = {Automated Hate Speech Detection and the Problem of Offensive Language},
  author = {Davidson, Thomas and Warmsley, Dana and Macy, Michael and Weber, Ingmar}, 
  booktitle = {Proceedings of the 11th International AAAI Conference on Web and Social Media},
  series = {ICWSM '17},
  year = {2017},
  location = {Montreal, Canada},
  pages = {512-515}
  }

## HateXplain

  Binny Mathew, Punyajoy Saha, Seid Muhie Yimam, Chris Biemann, Pawan Goyal, and Animesh Mukherjee "HateXplain: A Benchmark Dataset for Explainable Hate Speech Detection". Accepted at AAAI 2021.
  
 https://github.com/hate-alert/HateXplain

@inproceedings{mathew2021hatexplain,
  title={HateXplain: A Benchmark Dataset for Explainable Hate Speech Detection},
  author={Mathew, Binny and Saha, Punyajoy and Yimam, Seid Muhie and Biemann, Chris and Goyal, Pawan and Mukherjee, Animesh},
  booktitle={Proceedings of the AAAI Conference on Artificial Intelligence},
  volume={35},
  number={17},
  pages={14867--14875},
  year={2021}
}
