# TLCC: Transfer Learning Colony Count

The accuracy of the quantification of the effect of cellular treatments
in many bioassays depends on accurate colony counting.
However, such colony counting processes tend to be tedious, slow, and error prone.
Thus, the pursue of a much-improved colony counting technique is ongoing,
and this has led to the progression from manual colony counting to partly
automated and fully automated techniques.
The fully automated techniques were developed using deep learning (DL).
A significant problem faced in applying DL to this task is the lack of sizeable collections
of annotated plate images.
For this reason, we here propose a transfer learning technique
that can overcome this problem by exploiting models trained for other tasks.
To demonstrate the feasibility of this idea, we show how, using a small dataset,
and a DL model for counting objects in congested scenes can be adapted
to cell colony counting to achieve better performance than existing, more widely used models.

## Requirements

- Model run on linux machines
- Anaconda Python 2.7 or later

## Usage

We propose a transfer learning model to count colonies, TLCC.
It takes image of colonies and predict the count.
To use TLCC model, please git clone it and make sure you have
*[Installing Git Large File Storage](https://help.github.com/en/articles/installing-git-large-file-storage)*

To successfully run TLCC model we recomend you to create a virtul environment
based on requirements.txt:

```bash
conda create --name tlcc --file requirements.txt
# Activate your virtual environment:
source activate tlcc  #  or 'conda activate tlcc'
conda install pytorch torchvision cpuonly -c pytorch

python setup.py install
./tlcc/predict.py colony-count ./data/1.jpg

```
