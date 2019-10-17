# deeplearning_advancedDD2412

1. Install pytorch with: pip3 install torch torchvision
2. Run pytorch_test.py in the repo to see if pytorch is correctly installed
3. Set the project root folder to ZeroShotKnowledgeTransfer
4. Change the paths in scripts/main1.sh 


This is how it looks on my computer

```python

EXECUTABLE_FILE=/Users/niclashedberg/code/deeplearning_advancedDD2412/ZeroShotKnowledgeTransfer/main.py
LOG_DIR=/Users/niclashedberg/code/deeplearning_advancedDD2412/logs
PRETRAINED_MODELS_DIR=/Users/niclashedberg/code/deeplearning_advancedDD2412/Pretrained
DATASETS_DIR=/Users/niclashedberg/code/deeplearning_advancedDD2412/Datasets/


```

5. Switch 'python' to 'python3' in scripts/main1.sh 
6. Ändra path i main.py motsvarande
```python
parser.add_argument('--pretrained_models_path', nargs="?", type=str, default='/Users/niclashedberg/code/deeplearning_advancedDD2412/Pretrained')
parser.add_argument('--datasets_path', type=str, default="/Users/niclashedberg/code/deeplearning_advancedDD2412/Datasets/")
parser.add_argument('--log_directory_path', type=str, default="/Users/niclashedberg/code/deeplearning_advancedDD2412/logs/")
```
