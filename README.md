# Classifying Medical Notes using Multiple Approaches

## Authors

- Calvin Bell
- Dip Kiran Pradhan Newar
- Teja Vuppala


## Dataset
1. Download the dataset from [this site](https://github.com/sebischair/Medical-Abstracts-TC-Corpus/tree/main)
2. Create a new folder named "data" and add the three csv files downloaded from the site above.

## Installation
1. Install all packages from requirements.txt.
2. We used Python3.12 for our project.

## Running

1. Run all cells from KNN.ipynb. [For K-Nearest Neighbor]
2. Run all cells from NN.ipynb. [For Neural Network]
3. Run all cells from RNN.ipynb. [For Recurrant Neural Network using LSTM]

## CHAT GPT
1. For CHATGPT, we did not run using the api but we just pass the prompt to [ChatGPT chatbox] (https://chatgpt.com/)
2. We used three conditions, where in each conditions we had total of 100 medical notes passed to GPT. 
    2.1. First, we used balanced dataset where we had 20 notes of each of the 5 categories randomly grouped in size of 10.
    2.2. Second, we used unbalanced dataset where we had different number of notes of each of the 5 categories randomly grouped in size of 10.
    2.3. Third, we used unbalanced dataset (Similar to 2.2.) but passed two examples of each category as a part of the prompt.
3. You can view more in details in GPT_prompts. It also has the text we used in the prompt.
4. Since the prompt is manually passed to the CHATGPT and output are also manually collected so we have commented the option to save the prompt. The folders prompts has three subfolders where you can see the prompts we have used to pass to ChatGPT. Similarly, output is in the folder chat_gpt_output.
5. Run all cells from GPT.ipynb. [For ChatGPT analysis]