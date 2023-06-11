# Text_summarizer
This repo is all about an implementation of Text summarization using hugging face api

>**Note**
>According to [PEP 8](https://peps.python.org/pep-0008/#package-and-module-names), python style guide :  
>```Modules should have short, all-lowercase names. Underscores can be used in the module name if it improves readability. Python packages should also have short, all-lowercase names, although the use of underscores is discouraged.```
>
>However, I tried to use the name : Project_text_summarizer in `src` which acts as my local package and it **`totally works`**, however, it is a possibility that it may fail sometime while running the setup, so either you can delete the cache and logging files etc, and re-run the setup or change the src_repo name in the `template.py` file to something easy that abides the above rule as per your preference.


## Workflows

1. Update config.yaml
2. params.yaml
3. update entity
4. Update Configuration manager in src/config
5. Update Components
6. Update Pipeline
7. update Main.py
8. Update app.py


Tasks List:

- [x] Template Creation
- [x] Creating Requirements file and setup
- [x] Logging, exception and utils files
- [x] Working on notebooks
- [x] Creating and Following project workflows
- [x] Dockerfile creation
- [ ] deployment on AWS
